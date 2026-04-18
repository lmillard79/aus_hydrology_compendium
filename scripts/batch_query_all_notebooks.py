#!/usr/bin/env python3
"""
Batch query all themes from ALL notebooks.
This script processes all conferences with detailed themes and saves progress.
Run this and let it work - it will take several hours but handles errors gracefully.
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


async def batch_process_all_notebooks(config_path: str = 'scripts/notebooks_config.json'):
    """
    Process all notebooks from config, querying all themes for each.
    """
    
    # Load config
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Get all notebooks
    all_notebooks = []
    all_notebooks.extend(config.get('notebooks', []))  # FMA
    all_notebooks.extend(config.get('hwrs_notebooks', []))  # HWRS
    
    # Filter to only those with valid IDs and extracted JSON files
    to_process = []
    for nb in all_notebooks:
        notebook_id = nb.get('id', '')
        if not notebook_id or 'PLACEHOLDER' in notebook_id:
            continue
        
        year = nb['year']
        conference = nb['conference']
        json_file = Path(f'docs/data/conference-papers/{conference.lower()}_{year}.json')
        
        if json_file.exists():
            # Load JSON to check if it has themes
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            themes = data.get('main_themes', [])
            if themes:
                to_process.append({
                    'year': year,
                    'conference': conference,
                    'id': notebook_id,
                    'json_file': str(json_file),
                    'theme_count': len(themes)
                })
    
    print(f"\n{'='*70}")
    print(f"BATCH PROCESSING: {len(to_process)} notebooks")
    print(f"{'='*70}")
    print(f"\nQueue:")
    for i, nb in enumerate(to_process, 1):
        print(f"  {i}. {nb['conference']} {nb['year']} - {nb['theme_count']} themes")
    print(f"\nEstimated time: ~{len(to_process) * 2} minutes (with 5s delay)")
    print(f"{'='*70}\n")
    
    # Process each notebook
    manager = NotebookLMManager()
    results = {
        'started_at': datetime.now(timezone.utc).isoformat(),
        'completed': [],
        'failed': [],
        'skipped': []
    }
    
    for i, nb in enumerate(to_process, 1):
        print(f"\n[{i}/{len(to_process)}] Processing {nb['conference']} {nb['year']}...")
        print(f"  Notebook ID: {nb['id']}")
        print(f"  JSON File: {nb['json_file']}")
        print(f"  Themes: {nb['theme_count']}")
        
        try:
            # Check if already has theme files
            theme_pattern = f"docs/data/conference-papers/{nb['conference'].lower()}_{nb['year']}_theme_*.txt"
            existing_themes = list(Path('.').glob(theme_pattern))
            
            if existing_themes:
                print(f"  ⚠ Already has {len(existing_themes)} theme files, skipping...")
                results['skipped'].append({
                    'conference': nb['conference'],
                    'year': nb['year'],
                    'reason': f'Already has {len(existing_themes)} theme files'
                })
                continue
            
            # Query all themes
            await manager.query_all_themes(
                json_file=nb['json_file'],
                notebook_id=nb['id'],
                output_dir='docs/data/conference-papers',
                delay=5.0  # 5 second delay between themes
            )
            
            results['completed'].append({
                'conference': nb['conference'],
                'year': nb['year'],
                'themes': nb['theme_count']
            })
            
            print(f"  ✓ Completed {nb['conference']} {nb['year']}")
            
            # Save progress after each notebook
            progress_file = f'docs/data/conference-papers/batch_progress_{datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")}.json'
            with open(progress_file, 'w') as f:
                json.dump(results, f, indent=2)
            
            # Longer delay between notebooks to avoid rate limits
            if i < len(to_process):
                print(f"  Waiting 30s before next notebook...")
                await asyncio.sleep(30)
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
            results['failed'].append({
                'conference': nb['conference'],
                'year': nb['year'],
                'error': str(e)
            })
            # Continue to next notebook
            print(f"  Continuing to next notebook...")
            await asyncio.sleep(10)
    
    # Final summary
    results['completed_at'] = datetime.now(timezone.utc).isoformat()
    
    print(f"\n{'='*70}")
    print(f"BATCH PROCESSING COMPLETE")
    print(f"{'='*70}")
    print(f"Completed: {len(results['completed'])}")
    print(f"Failed: {len(results['failed'])}")
    print(f"Skipped: {len(results['skipped'])}")
    print(f"\nCompleted notebooks:")
    for item in results['completed']:
        print(f"  ✓ {item['conference']} {item['year']} ({item['themes']} themes)")
    
    if results['failed']:
        print(f"\nFailed notebooks:")
        for item in results['failed']:
            print(f"  ✗ {item['conference']} {item['year']}: {item['error']}")
    
    # Save final results
    final_file = f'docs/data/conference-papers/batch_results_{datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")}.json'
    with open(final_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to: {final_file}")
    print(f"{'='*70}\n")
    
    return results


if __name__ == '__main__':
    print("\n" + "="*70)
    print("NOTEBOOKLM BATCH THEME QUERY")
    print("Processing all conference notebooks with detailed theme queries")
    print("="*70 + "\n")
    
    # Run the batch process
    results = asyncio.run(batch_process_all_notebooks())
    
    # Exit with appropriate code
    sys.exit(0 if not results['failed'] else 1)
