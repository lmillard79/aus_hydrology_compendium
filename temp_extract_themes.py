import json

with open('docs/data/conference-papers/fma_2025_all_themes_detailed.json', 'r') as f:
    data = json.load(f)

theme_files = {
    'theme-1': 'docs/conference-papers/fma-2025/disaster-adaptation-plans-content.md',
    'theme-2': 'docs/conference-papers/fma-2025/modelling-analysis-content.md',
    'theme-3': 'docs/conference-papers/fma-2025/infrastructure-land-planning-content.md',
    'theme-4': 'docs/conference-papers/fma-2025/governance-programs-content.md',
}

for theme in data['themes']:
    theme_id = theme['id']
    if theme_id in theme_files:
        with open(theme_files[theme_id], 'w', encoding='utf-8') as f:
            f.write(theme['query_response'])
        print(f"Written: {theme_files[theme_id]}")

print("Done!")
