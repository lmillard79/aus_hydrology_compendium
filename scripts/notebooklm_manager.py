#!/usr/bin/env python3
"""
NotebookLM Manager for Australian Hydrology Compendium

This script provides automated extraction of mind maps from NotebookLM notebooks
and creation of new notebooks from folders of PDFs.

Requirements:
    pip install "notebooklm-py[browser]"
    playwright install chromium

Usage:
    # Extract mind maps from existing notebooks
    python notebooklm_manager.py extract --config notebooks_config.json
    
    # Create new notebook from PDF folder
    python notebooklm_manager.py create --name "FMA 2025" --pdf-folder ./pdfs/fma_2025
    
    # Extract all pending notebooks from config
    python notebooklm_manager.py extract-pending
"""

import asyncio
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# Import notebooklm-py (installed as notebooklm_py, imported as notebooklm)
try:
    from notebooklm import NotebookLMClient
except ImportError as e:
    print(f"Error importing notebooklm-py: {e}")
    print("The package may be installed with a different import path.")
    print("Attempting alternative import...")
    try:
        # Alternative: try direct import
        import notebooklm
        from notebooklm.client import NotebookLMClient
    except ImportError:
        print("Error: notebooklm-py not properly installed.")
        print("Run: pip install 'notebooklm-py[browser]'")
        print("Then: playwright install chromium")
        sys.exit(1)


class NotebookLMManager:
    """Manager for NotebookLM operations."""
    
    def __init__(self, data_dir: str = "docs/data/conference-papers"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    async def _get_client(self):
        """Get an initialized NotebookLMClient."""
        return await NotebookLMClient.from_storage()
    
    async def list_notebooks(self) -> list:
        """List all accessible notebooks."""
        async with await self._get_client() as client:
            notebooks = await client.notebooks.list()
            # Print raw notebook data for debugging
            print("\nAccessible Notebooks:")
            for nb in notebooks:
                # Try different possible attribute names
                nb_id = getattr(nb, 'id', str(nb))
                nb_title = getattr(nb, 'title', None) or getattr(nb, 'name', None) or 'Unknown'
                print(f"  - {nb_title}: {nb_id}")
            return notebooks
    
    async def create_notebook_from_pdfs(
        self, 
        name: str, 
        pdf_folder: str,
        description: str = ""
    ) -> str:
        """
        Create a new notebook and add all PDFs from a folder.
        
        Args:
            name: Notebook name
            pdf_folder: Path to folder containing PDFs
            description: Optional notebook description
            
        Returns:
            notebook_id: The created notebook's ID
        """
        pdf_path = Path(pdf_folder)
        if not pdf_path.exists():
            raise ValueError(f"PDF folder not found: {pdf_folder}")
        
        # Find all PDFs
        pdfs = list(pdf_path.glob("*.pdf"))
        if not pdfs:
            raise ValueError(f"No PDFs found in {pdf_folder}")
        
        print(f"Found {len(pdfs)} PDFs in {pdf_folder}")
        
        async with await self._get_client() as client:
            # Create notebook
            print(f"Creating notebook: {name}")
            notebook = await client.notebooks.create(name, description=description)
            print(f"Created notebook: {notebook.id}")
            
            # Add PDFs as sources
            for i, pdf in enumerate(pdfs, 1):
                print(f"  Adding PDF {i}/{len(pdfs)}: {pdf.name}")
                try:
                    await client.sources.add_file(
                        notebook.id, 
                        str(pdf), 
                        wait=True
                    )
                    print(f"    ✓ Added: {pdf.name}")
                except Exception as e:
                    print(f"    ✗ Failed to add {pdf.name}: {e}")
            
            return notebook.id
    
    async def generate_and_download_mindmap(
        self, 
        notebook_id: str, 
        output_path: Optional[str] = None
    ) -> dict:
        """
        Generate mind map and download as JSON.
        
        Args:
            notebook_id: The notebook ID
            output_path: Optional output file path
            
        Returns:
            mindmap_data: The mind map JSON data
        """
        print(f"Generating mind map for notebook: {notebook_id}")
        
        async with await self._get_client() as client:
            # Generate mind map
            result = await client.artifacts.generate_mind_map(notebook_id)
            
            # Handle both dict and object return types
            if isinstance(result, dict):
                task_id = result.get('task_id') or result.get('id')
            else:
                task_id = getattr(result, 'task_id', None) or getattr(result, 'id', None)
            
            if not task_id:
                print("  Warning: Could not get task ID, mind map may already be ready")
                task_id = "unknown"
            else:
                print(f"  Mind map generation started: {task_id}")
                
                # Wait for completion
                try:
                    await client.artifacts.wait_for_completion(
                        notebook_id, 
                        task_id
                    )
                    print("  Mind map generation complete")
                except Exception as e:
                    print(f"  Warning during wait: {e}")
                    # Continue anyway, mind map might be ready
        
        # Download mind map
        if output_path:
            async with await self._get_client() as client:
                await client.artifacts.download_mind_map(
                    notebook_id, 
                    output_path
                )
                print(f"  Downloaded to: {output_path}")
                
                # Read and return the JSON
                with open(output_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        
        return {}
    
    def transform_to_schema(
        self,
        notebook_id: str,
        notebook_name: str,
        year: int,
        conference: str,
        mindmap_raw: dict,
        sources_count: int
    ) -> dict:
        """
        Transform raw mind map data to compendium JSON schema.
        
        Args:
            notebook_id: NotebookLM notebook ID
            notebook_name: Name of the notebook
            year: Conference year
            conference: Conference code (FMA, HWRS, etc.)
            mindmap_raw: Raw mind map data from NotebookLM
            sources_count: Number of sources in notebook
            
        Returns:
            Formatted dict matching schema.json
        """
        # Debug: Print raw structure keys
        print(f"  Raw mind map keys: {list(mindmap_raw.keys())}")
        
        # Extract title from mind map data - try multiple possible keys
        title = mindmap_raw.get('title') or mindmap_raw.get('topic') or mindmap_raw.get('name') or notebook_name
        
        # Extract themes from mind map structure - try multiple possible structures
        themes = []
        
        # Try different possible keys for the main content
        nodes = mindmap_raw.get('nodes') or mindmap_raw.get('themes') or mindmap_raw.get('children') or mindmap_raw.get('items') or []
        
        if not nodes:
            # If no nodes found, check if the whole thing is a list
            if isinstance(mindmap_raw, list):
                nodes = mindmap_raw
            # Or look for nested structure
            elif 'root' in mindmap_raw:
                nodes = mindmap_raw['root'].get('children', [])
        
        print(f"  Found {len(nodes)} top-level items")
        
        # First-level nodes are main themes
        for i, node in enumerate(nodes):
            if isinstance(node, dict):
                theme_id = f"theme-{i+1}"
                theme_name = node.get('label') or node.get('name') or node.get('title') or f'Theme {i+1}'
                theme_description = node.get('description') or node.get('desc', '')
                
                # Second-level nodes are subtopics
                subtopics = []
                children = node.get('children') or node.get('nodes') or node.get('items') or []
                for child in children:
                    if isinstance(child, dict):
                        subtopic_label = child.get('label') or child.get('name') or child.get('title', '')
                        subtopic_desc = child.get('description') or child.get('desc', '')
                        if subtopic_desc:
                            subtopics.append(f"{subtopic_label} - {subtopic_desc}")
                        else:
                            subtopics.append(subtopic_label)
                    elif isinstance(child, str):
                        subtopics.append(child)
                
                themes.append({
                    "id": theme_id,
                    "theme": theme_name,
                    "description": theme_description,
                    "subtopics": subtopics,
                    "key_papers": []
                })
            elif isinstance(node, str):
                # Simple string list
                themes.append({
                    "id": f"theme-{i+1}",
                    "theme": node,
                    "description": "",
                    "subtopics": [],
                    "key_papers": []
                })
        
        return {
            "notebook": f"{conference}_{year}",
            "year": year,
            "conference": conference,
            "sources_count": sources_count,
            "mind_map_title": title,
            "main_themes": themes,
            "generated_date": datetime.now(timezone.utc).isoformat(),
            "notebooklm_url": f"https://notebooklm.google.com/notebook/{notebook_id}"
        }
    
    async def extract_and_save_mindmap(
        self,
        notebook_id: str,
        year: int,
        conference: str,
        force: bool = False
    ) -> Path:
        """
        Extract mind map from a notebook and save as JSON.
        
        Args:
            notebook_id: NotebookLM notebook ID
            year: Conference year
            conference: Conference code
            force: Overwrite existing files
            
        Returns:
            Path to saved JSON file
        """
        filename = f"{conference.lower()}_{year}.json"
        output_path = self.data_dir / filename
        temp_mindmap_path = self.data_dir / f"{conference.lower()}_{year}_raw_mindmap.json"
        
        # Check if already exists
        if output_path.exists() and not force:
            print(f"  Skipping {filename} (already exists, use --force to overwrite)")
            return output_path
        
        # Get notebook info
        async with await self._get_client() as client:
            sources = await client.sources.list(notebook_id)
            sources_count = len(sources)
        
        notebook_name = f"{conference} {year}"
        print(f"  Notebook: {notebook_name}")
        print(f"  Sources: {sources_count}")
        
        # Generate and download mind map
        mindmap_raw = await self.generate_and_download_mindmap(
            notebook_id, 
            str(temp_mindmap_path)
        )
        
        # Transform to schema
        formatted_data = self.transform_to_schema(
            notebook_id=notebook_id,
            notebook_name=notebook_name,
            year=year,
            conference=conference,
            mindmap_raw=mindmap_raw,
            sources_count=sources_count
        )
        
        # Save formatted JSON
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(formatted_data, f, indent=2, ensure_ascii=False)
        print(f"  Saved: {output_path}")
        
        # Keep raw file for inspection (commented out cleanup)
        # if temp_mindmap_path.exists():
        #     temp_mindmap_path.unlink()
        
        print(f"  Raw mind map preserved: {temp_mindmap_path}")
        
        return output_path
    
    async def batch_extract_from_config(self, config_path: str, force: bool = False):
        """
        Batch extract mind maps from a configuration file.
        
        Config format (JSON):
        {
            "notebooks": [
                {
                    "id": "58b99d93-4101-4e11-93d6-a377158f5a18",
                    "year": 2024,
                    "conference": "FMA",
                    "extracted": true
                },
                ...
            ]
        }
        """
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Process both FMA and HWRS notebooks
        all_notebooks = []
        all_notebooks.extend(config.get('notebooks', []))
        all_notebooks.extend(config.get('hwrs_notebooks', []))
        
        print(f"Found {len(all_notebooks)} notebooks in config")
        print(f"  - FMA: {len(config.get('notebooks', []))}")
        print(f"  - HWRS: {len(config.get('hwrs_notebooks', []))}")
        
        for nb_config in all_notebooks:
            notebook_id = nb_config.get('id', '')
            if not notebook_id or 'PLACEHOLDER' in notebook_id:
                print(f"\nSkipping {nb_config.get('conference', 'Unknown')} {nb_config.get('year', '')} (no valid ID)")
                continue
                
            year = nb_config['year']
            conference = nb_config['conference']
            already_extracted = nb_config.get('extracted', False)
            
            if already_extracted and not force:
                print(f"\nSkipping {conference} {year} (already extracted)")
                continue
            
            print(f"\nExtracting {conference} {year}...")
            try:
                await self.extract_and_save_mindmap(
                    notebook_id, 
                    year, 
                    conference, 
                    force=force
                )
                nb_config['extracted'] = True
                nb_config['extracted_date'] = datetime.now(timezone.utc).isoformat()
                if 'error' in nb_config:
                    del nb_config['error']
            except Exception as e:
                print(f"  Error extracting {conference} {year}: {e}")
                nb_config['error'] = str(e)
        
        # Save updated config
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"\nUpdated config: {config_path}")
    
    async def query_topic(
        self, 
        notebook_id: str, 
        topic: str, 
        context: Optional[str] = None,
        save: bool = False,
        output_dir: str = 'docs/data/conference-papers',
        quiet: bool = False
    ) -> str:
        """
        Query NotebookLM about a specific topic (like clicking a mind map node).
        
        This mimics the 'Save to note' feature when clicking on a mind map node.
        
        Args:
            notebook_id: The notebook ID
            topic: The topic/node name to query
            context: Optional context (e.g., "Flood Management and Research 2024")
            save: Whether to save the response to a file
            output_dir: Directory to save response files
            
        Returns:
            The response text from NotebookLM
        """
        # Build the prompt like NotebookLM does for mind map nodes
        if context:
            prompt = f'Discuss what these sources say about {topic}, in the larger context of {context}.'
        else:
            prompt = f'Discuss what these sources say about {topic}.'
        
        if not quiet:
            print(f"Querying NotebookLM...")
            print(f"  Notebook: {notebook_id}")
            print(f"  Topic: {topic}")
            print(f"  Prompt: {prompt}")
        
        async with await self._get_client() as client:
            # Use the chat/ask functionality
            result = await client.chat.ask(
                notebook_id=notebook_id,
                question=prompt
            )
            
            # Extract text from AskResult object
            if hasattr(result, 'text'):
                response = result.text
            elif hasattr(result, 'answer'):
                response = result.answer
            elif hasattr(result, 'content'):
                response = result.content
            else:
                response = str(result)
        
        if not quiet:
            print(f"\n{'='*60}")
            print(f"RESPONSE:")
            print(f"{'='*60}")
            print(response)
            print(f"{'='*60}\n")
        
        # Save to file if requested
        if save:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Create filename from topic
            safe_topic = topic.replace(' ', '_').replace('/', '_').replace('\\', '_')[:50]
            filename = f"query_{safe_topic}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.txt"
            file_path = output_path / filename
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"Topic: {topic}\n")
                f.write(f"Context: {context or 'N/A'}\n")
                f.write(f"Notebook: {notebook_id}\n")
                f.write(f"Prompt: {prompt}\n")
                f.write(f"{'='*60}\n\n")
                f.write(response)
            
            print(f"Saved to: {file_path}")
        
        return response
    
    async def query_all_themes(
        self,
        json_file: str,
        notebook_id: str,
        output_dir: str = 'docs/data/conference-papers',
        delay: float = 2.0
    ) -> dict:
        """
        Query all themes from an extracted notebook and save detailed responses.
        
        This reads the extracted JSON file, queries NotebookLM for each theme,
        and builds an index of papers with citations.
        
        Args:
            json_file: Path to extracted JSON file
            notebook_id: Notebook ID to query
            output_dir: Directory to save outputs
            delay: Seconds between queries to avoid rate limiting
            
        Returns:
            Dictionary with all theme responses and source index
        """
        import asyncio
        
        # Load the extracted data
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        conference = data.get('conference', 'Unknown')
        year = data.get('year', 'Unknown')
        mind_map_title = data.get('mind_map_title', f'{conference} {year}')
        themes = data.get('main_themes', [])
        
        print(f"\nQuerying {len(themes)} themes from {conference} {year}...")
        print(f"Notebook: {notebook_id}")
        print(f"Context: {mind_map_title}")
        
        # Prepare output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Create safe filename prefix
        safe_prefix = f"{conference.lower()}_{year}"
        
        # Dictionary to store all responses
        all_responses = {
            "metadata": {
                "conference": conference,
                "year": year,
                "notebook_id": notebook_id,
                "mind_map_title": mind_map_title,
                "queried_date": datetime.now(timezone.utc).isoformat(),
                "total_themes": len(themes)
            },
            "themes": [],
            "source_index": {}  # Will aggregate all sources
        }
        
        # Query each theme
        for i, theme in enumerate(themes, 1):
            theme_name = theme.get('theme', f'Theme {i}')
            theme_id = theme.get('id', f'theme-{i}')
            
            print(f"\n[{i}/{len(themes)}] Querying: {theme_name}")
            
            try:
                # Query NotebookLM (quiet mode for batch) with retry
                max_retries = 2
                response = None
                
                for attempt in range(max_retries + 1):
                    try:
                        response = await self.query_topic(
                            notebook_id=notebook_id,
                            topic=theme_name,
                            context=mind_map_title,
                            save=False,  # We'll save aggregated version
                            quiet=True
                        )
                        break  # Success, exit retry loop
                    except Exception as e:
                        if "timed out" in str(e).lower() and attempt < max_retries:
                            print(f"  Timeout, retrying ({attempt + 1}/{max_retries})...")
                            await asyncio.sleep(5)  # Wait longer before retry
                        else:
                            raise  # Re-raise if not timeout or out of retries
                
                # Store response
                theme_data = {
                    "id": theme_id,
                    "theme": theme_name,
                    "description": theme.get('description', ''),
                    "subtopics": theme.get('subtopics', []),
                    "query_response": response,
                    "sources_mentioned": []  # Will parse from response
                }
                
                # Try to extract source citations from response
                # Look for patterns like "Author et al. (Year)" or "Source: ..." or [1], [2]
                import re
                
                # Pattern for various citation formats
                citation_patterns = [
                    # Numerical citations like [1], [2], [3]
                    r'\[(\d+)\]',
                    # Author-year citations like "Smith et al. (2024)"
                    r'([A-Z][a-z]+(?:\s+et\s+al\.)?)\s*\((\d{4})\)',
                    # Author-year in parentheses like "(Jones 2023)"
                    r'\(([A-Z][a-z]+\s+\d{4})\)',
                    # Source label
                    r'Source:\s*([^\n]+)',
                    # Quoted paper titles
                    r'from\s+"([^"]+)"',
                    # Reference to "Paper X" or "Document Y"
                    r'(?:paper|document|study|report)\s+(\d+)',
                ]
                
                sources_found = set()
                for pattern in citation_patterns:
                    matches = re.findall(pattern, response, re.IGNORECASE)
                    for match in matches:
                        if isinstance(match, tuple):
                            if len(match) == 2 and match[1].isdigit():
                                # Author (Year) format
                                sources_found.add(f"{match[0]} ({match[1]})")
                            else:
                                sources_found.add(str(match[0]))
                        else:
                            # Single value - could be [1] or a number
                            if match.isdigit():
                                sources_found.add(f"[{match}]")
                            else:
                                sources_found.add(match)
                
                theme_data["sources_mentioned"] = list(sources_found)
                
                # Add to aggregated source index
                for source in sources_found:
                    if source not in all_responses["source_index"]:
                        all_responses["source_index"][source] = {
                            "themes": [],
                            "first_mentioned_in": theme_name
                        }
                    all_responses["source_index"][source]["themes"].append(theme_name)
                
                all_responses["themes"].append(theme_data)
                
                # Save individual theme file
                theme_file = output_path / f"{safe_prefix}_theme_{i:02d}_{theme_id}.txt"
                with open(theme_file, 'w', encoding='utf-8') as f:
                    f.write(f"Theme: {theme_name}\n")
                    f.write(f"Conference: {conference} {year}\n")
                    f.write(f"Notebook: {notebook_id}\n")
                    f.write(f"Query: Discuss what these sources say about {theme_name}, in the larger context of {mind_map_title}.\n")
                    f.write(f"Sources Found: {', '.join(sources_found) if sources_found else 'None detected'}\n")
                    f.write(f"{'='*60}\n\n")
                    f.write(response)
                
                print(f"  ✓ Saved: {theme_file}")
                print(f"  Sources detected: {len(sources_found)}")
                
                # Delay between queries
                if i < len(themes):
                    await asyncio.sleep(delay)
                    
            except Exception as e:
                print(f"  ✗ Error querying {theme_name}: {e}")
                theme_data = {
                    "id": theme_id,
                    "theme": theme_name,
                    "error": str(e)
                }
                all_responses["themes"].append(theme_data)
        
        # Save aggregated JSON with all responses
        agg_file = output_path / f"{safe_prefix}_all_themes_detailed.json"
        with open(agg_file, 'w', encoding='utf-8') as f:
            json.dump(all_responses, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*60}")
        print(f"Complete! Processed {len(themes)} themes.")
        print(f"Aggregated data: {agg_file}")
        print(f"Source index: {len(all_responses['source_index'])} unique sources")
        print(f"{'='*60}\n")
        
        # Print source index summary
        if all_responses["source_index"]:
            print("Sources Index:")
            for source, info in sorted(all_responses["source_index"].items()):
                print(f"  - {source} (mentioned in {len(info['themes'])} themes)")
        
        return all_responses


def create_sample_config():
    """Create a sample configuration file."""
    config = {
        "notebooks": [
            {
                "id": "58b99d93-4101-4e11-93d6-a377158f5a18",
                "year": 2024,
                "conference": "FMA",
                "extracted": True
            },
            {
                "id": "b45571e2-ca22-49b4-ad5b-ab9094ddd245",
                "year": 2023,
                "conference": "FMA",
                "extracted": True
            },
            {
                "id": "1e7cf6a8-f79f-4e09-a150-7fc45fb97dd7",
                "year": 2019,
                "conference": "FMA",
                "extracted": True
            },
            {
                "id": "PLACEHOLDER_FMA_2025",
                "year": 2025,
                "conference": "FMA",
                "extracted": False
            },
            {
                "id": "PLACEHOLDER_FMA_2022",
                "year": 2022,
                "conference": "FMA",
                "extracted": False
            },
            {
                "id": "PLACEHOLDER_FMA_2020",
                "year": 2020,
                "conference": "FMA",
                "extracted": False
            }
        ],
        "hwrs_notebooks": [
            {"year": 2025, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2024, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2023, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2022, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2021, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2018, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2016, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2015, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2014, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2012, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2011, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False},
            {"year": 2005, "conference": "HWRS", "id": "PLACEHOLDER", "extracted": False}
        ]
    }
    
    config_path = Path("scripts/notebooks_config.json")
    config_path.parent.mkdir(exist_ok=True)
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"Created sample config: {config_path}")
    print("Edit this file to add your actual NotebookLM notebook IDs")


async def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="NotebookLM Manager for Australian Hydrology Compendium"
    )
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Create config command
    config_parser = subparsers.add_parser(
        'create-config', 
        help='Create sample configuration file'
    )
    
    # Extract command
    extract_parser = subparsers.add_parser(
        'extract', 
        help='Extract mind maps from notebooks in config'
    )
    extract_parser.add_argument(
        '--config', 
        default='scripts/notebooks_config.json',
        help='Path to config file'
    )
    extract_parser.add_argument(
        '--force', 
        action='store_true',
        help='Overwrite existing files'
    )
    
    # Create notebook command
    create_parser = subparsers.add_parser(
        'create', 
        help='Create new notebook from PDF folder'
    )
    create_parser.add_argument(
        '--name', 
        required=True,
        help='Notebook name'
    )
    create_parser.add_argument(
        '--pdf-folder', 
        required=True,
        help='Path to folder containing PDFs'
    )
    create_parser.add_argument(
        '--description', 
        default='',
        help='Optional notebook description'
    )
    
    # List notebooks command
    list_parser = subparsers.add_parser(
        'list', 
        help='List all accessible notebooks'
    )
    
    # Extract pending command
    pending_parser = subparsers.add_parser(
        'extract-pending',
        help='Extract only pending (not yet extracted) notebooks'
    )
    pending_parser.add_argument(
        '--config', 
        default='scripts/notebooks_config.json',
        help='Path to config file'
    )
    
    # Query topic command - get summary for a mind map node
    query_parser = subparsers.add_parser(
        'query-topic',
        help='Query NotebookLM about a specific topic (mind map node summary)'
    )
    query_parser.add_argument(
        '--notebook-id', 
        required=True,
        help='Notebook ID to query'
    )
    query_parser.add_argument(
        '--topic', 
        required=True,
        help='Topic/node name to query (e.g., "Infragravity Waves in Coastal Creeks")'
    )
    query_parser.add_argument(
        '--context', 
        default=None,
        help='Optional context (e.g., "Flood Management and Research 2024")'
    )
    query_parser.add_argument(
        '--save', 
        action='store_true',
        help='Save response to a file'
    )
    query_parser.add_argument(
        '--output-dir',
        default='docs/data/conference-papers',
        help='Directory to save query responses'
    )
    
    # Query all themes command - batch query all mind map themes
    query_all_parser = subparsers.add_parser(
        'query-all-themes',
        help='Query all themes from an extracted notebook and save detailed responses with source citations'
    )
    query_all_parser.add_argument(
        '--json-file', 
        required=True,
        help='Path to extracted JSON file (e.g., docs/data/conference-papers/fma_2024.json)'
    )
    query_all_parser.add_argument(
        '--notebook-id', 
        required=True,
        help='Notebook ID to query'
    )
    query_all_parser.add_argument(
        '--output-dir',
        default='docs/data/conference-papers',
        help='Directory to save query responses'
    )
    query_all_parser.add_argument(
        '--delay',
        type=float,
        default=2.0,
        help='Delay between queries in seconds (default: 2)'
    )
    
    args = parser.parse_args()
    
    if args.command == 'create-config':
        create_sample_config()
        return
    
    if args.command is None:
        parser.print_help()
        return
    
    # All other commands need the manager
    manager = NotebookLMManager()
    
    if args.command == 'list':
        notebooks = await manager.list_notebooks()
        print("\nAccessible Notebooks:")
        for nb in notebooks:
            print(f"  - {nb.name}: {nb.id}")
    
    elif args.command == 'create':
        notebook_id = await manager.create_notebook_from_pdfs(
            args.name,
            args.pdf_folder,
            args.description
        )
        print(f"\nCreated notebook: {notebook_id}")
        print(f"View at: https://notebooklm.google.com/notebook/{notebook_id}")
    
    elif args.command == 'extract':
        await manager.batch_extract_from_config(args.config, force=args.force)
    
    elif args.command == 'extract-pending':
        await manager.batch_extract_from_config(args.config, force=False)
    
    elif args.command == 'query-topic':
        response = await manager.query_topic(
            args.notebook_id,
            args.topic,
            args.context,
            save=args.save,
            output_dir=args.output_dir
        )
    
    elif args.command == 'query-all-themes':
        await manager.query_all_themes(
            json_file=args.json_file,
            notebook_id=args.notebook_id,
            output_dir=args.output_dir,
            delay=args.delay
        )


if __name__ == '__main__':
    asyncio.run(main())
