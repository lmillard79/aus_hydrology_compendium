#!/usr/bin/env python3
"""
Batch enhanced queries for ALL notebooks.
This runs bibliography, connections, gaps, and practitioner queries for each notebook.
"""

import asyncio
import json
import sys
import os
from pathlib import Path
from datetime import datetime, timezone

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

# Set up imports like notebooklm_manager does
try:
    from notebooklm import NotebookLMClient
except ImportError:
    try:
        from notebooklm_py import NotebookLMClient
    except ImportError:
        print("Error: notebooklm-py not installed.")
        print("Run: pip install 'notebooklm-py[browser]'")
        sys.exit(1)

# Now import our manager
from notebooklm_manager import NotebookLMManager


async def batch_enhanced_queries(
    config_path: str = 'scripts/notebooks_config.json',
    query_types: list = None,
    skip_existing: bool = True
):
    """
    Run enhanced queries on all notebooks from config.
    """
    
    if query_types is None:
        # Default priority order: bibliography first, then others
        query_types = ['bibliography', 'connections', 'gaps', 'practitioner', 'methods', 'timeline']
    
    # Load config
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Combine all notebooks
    all_notebooks = []
    all_notebooks.extend(config.get('notebooks', []))
    all_notebooks.extend(config.get('hwrs_notebooks', []))
    
    # Add conceptual notebooks (cross-cutting themes)
    conceptual_notebooks = config.get('conceptual_notebooks', [])
    for nb in conceptual_notebooks:
        # Normalize to same structure as conference notebooks
        nb['conference'] = 'Conceptual'
        nb['year'] = nb.get('name', 'Unknown')  # Use name as identifier
        nb['is_conceptual'] = True
    all_notebooks.extend(conceptual_notebooks)
    
    # Filter to only extracted notebooks
    extracted_notebooks = [
        nb for nb in all_notebooks 
        if nb.get('extracted', False) and not 'PLACEHOLDER' in nb.get('id', '')
    ]
    
    total = len(extracted_notebooks) * len(query_types)
    completed = 0
    failed = 0
    skipped = 0
    
    print("=" * 70)
    print("BATCH ENHANCED QUERIES")
    print("=" * 70)
    print(f"Notebooks: {len(extracted_notebooks)}")
    print(f"Query types: {len(query_types)} ({', '.join(query_types)})")
    print(f"Total queries: {total}")
    print(f"Skip existing: {skip_existing}")
    print("=" * 70)
    print()
    
    manager = NotebookLMManager()
    
    for nb_config in extracted_notebooks:
        notebook_id = nb_config.get('id', '')
        year = nb_config.get('year', 0)
        conference = nb_config.get('conference', 'Unknown')
        
        # Find the JSON file
        json_file = f"docs/data/conference-papers/{conference.lower()}_{year}.json"
        json_path = Path(json_file)
        
        if not json_path.exists():
            print(f"\n[!] JSON not found: {json_file}")
            failed += len(query_types)
            continue
        
        print(f"\n{'='*70}")
        print(f"[{completed + skipped + failed + 1}/{total}] {conference} {year}")
        print(f"{'='*70}")
        
        for query_type in query_types:
            # Check if already exists
            safe_prefix = f"{conference.lower()}_{year}"
            output_file = Path(f"docs/data/conference-papers/{safe_prefix}_{query_type}.txt")
            
            if output_file.exists() and skip_existing:
                print(f"  [SKIP] {query_type} already exists")
                skipped += 1
                continue
            
            try:
                print(f"  [QUERY] {query_type}...")
                
                result = await manager.query_enhanced(
                    json_file=json_file,
                    notebook_id=notebook_id,
                    query_type=query_type,
                    output_dir='docs/data/conference-papers',
                    delay=3.0
                )
                
                # Check for actual error in response
                response_text = result.get('response', '') if result else ''
                has_real_error = (
                    response_text.startswith('Error querying NotebookLM:') or
                    'Authentication expired' in response_text or
                    'Authentication required' in response_text or
                    response_text == 'Error: Empty response from NotebookLM' or
                    not response_text.strip()
                )
                
                # Check if it's just a partial error (some content but error message somewhere)
                has_partial_error = 'Error:' in response_text and len(response_text) < 200
                
                if not has_real_error and not has_partial_error:
                    content_preview = response_text[:100].replace('\n', ' ')
                    print(f"  [OK] {query_type} complete ({len(response_text)} chars)")
                    completed += 1
                elif has_partial_error:
                    print(f"  [FAIL] {query_type} - API error (file saved with error message)")
                    failed += 1
                else:
                    # Real error - file was saved but contains error message
                    print(f"  [FAIL] {query_type} - {response_text[:100]}...")
                    failed += 1
                    
            except Exception as e:
                print(f"  [ERROR] {query_type}: {e}")
                failed += 1
            
            # Delay between queries
            await asyncio.sleep(5)
        
        # Save progress after each notebook
        progress = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "completed": completed,
            "failed": failed,
            "skipped": skipped,
            "last_notebook": f"{conference} {year}",
            "query_types": query_types
        }
        
        with open('docs/data/conference-papers/enhanced_progress.json', 'w') as f:
            json.dump(progress, f, indent=2)
        
        print(f"  [PROGRESS] Saved: {completed} completed, {failed} failed, {skipped} skipped")
        
        # Delay between notebooks
        await asyncio.sleep(10)
    
    print("\n" + "=" * 70)
    print("BATCH ENHANCED QUERIES COMPLETE")
    print("=" * 70)
    print(f"Completed: {completed}")
    print(f"Failed: {failed}")
    print(f"Skipped: {skipped}")
    print(f"Total: {completed + failed + skipped}")
    print("=" * 70)


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Batch enhanced queries for all notebooks')
    parser.add_argument('--config', default='scripts/notebooks_config.json', help='Config file path')
    parser.add_argument('--types', nargs='+', default=['bibliography', 'connections', 'gaps', 'practitioner'], 
                       help='Query types to run (default: bibliography connections gaps practitioner)')
    parser.add_argument('--force', action='store_true', help='Overwrite existing files')
    
    args = parser.parse_args()
    
    asyncio.run(batch_enhanced_queries(
        config_path=args.config,
        query_types=args.types,
        skip_existing=not args.force
    ))
