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
from datetime import datetime
from pathlib import Path
from typing import Optional

# Check if notebooklm-py is installed
try:
    from notebooklm import NotebookLMClient
    from notebooklm.models import Notebook, Source
except ImportError:
    print("Error: notebooklm-py not installed.")
    print("Run: pip install 'notebooklm-py[browser]'")
    print("Then: playwright install chromium")
    sys.exit(1)


class NotebookLMManager:
    """Manager for NotebookLM operations."""
    
    def __init__(self, data_dir: str = "docs/data/conference-papers"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.client: Optional[NotebookLMClient] = None
    
    async def __aenter__(self):
        """Async context manager entry."""
        self.client = await NotebookLMClient.from_storage()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.client:
            await self.client.close()
    
    async def list_notebooks(self) -> list[Notebook]:
        """List all accessible notebooks."""
        notebooks = await self.client.notebooks.list()
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
        
        # Create notebook
        print(f"Creating notebook: {name}")
        notebook = await self.client.notebooks.create(name, description=description)
        print(f"Created notebook: {notebook.id}")
        
        # Add PDFs as sources
        for i, pdf in enumerate(pdfs, 1):
            print(f"  Adding PDF {i}/{len(pdfs)}: {pdf.name}")
            try:
                await self.client.sources.add_file(
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
        
        # Generate mind map
        result = await self.client.artifacts.generate_mind_map(notebook_id)
        print(f"  Mind map generation started: {result.task_id}")
        
        # Wait for completion
        await self.client.artifacts.wait_for_completion(
            notebook_id, 
            result.task_id
        )
        print("  Mind map generation complete")
        
        # Download mind map
        if output_path:
            await self.client.artifacts.download_mind_map(
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
        # Extract title from mind map data
        title = mindmap_raw.get('title', mindmap_raw.get('topic', notebook_name))
        
        # Extract themes from mind map structure
        themes = []
        nodes = mindmap_raw.get('nodes', [])
        
        # First-level nodes are main themes
        for i, node in enumerate(nodes):
            theme_id = f"theme-{i+1}"
            theme_name = node.get('label', f'Theme {i+1}')
            theme_description = node.get('description', '')
            
            # Second-level nodes are subtopics
            subtopics = []
            children = node.get('children', [])
            for child in children:
                subtopic_label = child.get('label', '')
                subtopic_desc = child.get('description', '')
                if subtopic_desc:
                    subtopics.append(f"{subtopic_label} - {subtopic_desc}")
                else:
                    subtopics.append(subtopic_label)
            
            themes.append({
                "id": theme_id,
                "theme": theme_name,
                "description": theme_description,
                "subtopics": subtopics,
                "key_papers": []
            })
        
        return {
            "notebook": f"{conference}_{year}",
            "year": year,
            "conference": conference,
            "sources_count": sources_count,
            "mind_map_title": title,
            "main_themes": themes,
            "generated_date": datetime.utcnow().isoformat() + "Z",
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
        notebook = await self.client.notebooks.get(notebook_id)
        sources = await self.client.sources.list(notebook_id)
        sources_count = len(sources)
        
        print(f"  Notebook: {notebook.name}")
        print(f"  Sources: {sources_count}")
        
        # Generate and download mind map
        mindmap_raw = await self.generate_and_download_mindmap(
            notebook_id, 
            str(temp_mindmap_path)
        )
        
        # Transform to schema
        formatted_data = self.transform_to_schema(
            notebook_id=notebook_id,
            notebook_name=notebook.name,
            year=year,
            conference=conference,
            mindmap_raw=mindmap_raw,
            sources_count=sources_count
        )
        
        # Save formatted JSON
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(formatted_data, f, indent=2, ensure_ascii=False)
        print(f"  Saved: {output_path}")
        
        # Clean up temp file
        if temp_mindmap_path.exists():
            temp_mindmap_path.unlink()
        
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
        
        notebooks = config.get('notebooks', [])
        print(f"Found {len(notebooks)} notebooks in config")
        
        for nb_config in notebooks:
            notebook_id = nb_config['id']
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
                nb_config['extracted_date'] = datetime.utcnow().isoformat()
            except Exception as e:
                print(f"  Error extracting {conference} {year}: {e}")
                nb_config['error'] = str(e)
        
        # Save updated config
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"\nUpdated config: {config_path}")


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
    
    args = parser.parse_args()
    
    if args.command == 'create-config':
        create_sample_config()
        return
    
    if args.command is None:
        parser.print_help()
        return
    
    # All other commands need the client
    async with NotebookLMManager() as manager:
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


if __name__ == '__main__':
    asyncio.run(main())
