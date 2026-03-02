#!/usr/bin/env python3
"""
check_progress.py - Analyze progress and suggest next steps

Usage:
    python check_progress.py [path/to/features.json]

Shows:
- Completion percentage
- Next recommended features to work on
- Features that should be prioritized
"""

import json
import sys
from pathlib import Path
from datetime import datetime


def load_features(filepath: Path) -> dict | None:
    """Load features.json file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading features: {e}")
        return None


def suggest_next_features(data: dict, count: int = 3) -> list[dict]:
    """Suggest the next features to work on."""
    features = data.get('features', [])
    
    # Filter incomplete features
    incomplete = [f for f in features if not f.get('passes', False)]
    
    # Sort by category priority (setup first, then functional, etc.)
    priority_order = ['setup', 'functional', 'api', 'auth', 'ui', 'data', 'testing', 'deployment']
    
    def get_priority(f):
        cat = f.get('category', 'uncategorized')
        try:
            return priority_order.index(cat)
        except ValueError:
            return 99
    
    incomplete.sort(key=get_priority)
    return incomplete[:count]


def print_recommendations(data: dict) -> None:
    """Print recommendations for next steps."""
    features = data.get('features', [])
    
    if not features:
        print("No features defined!")
        return
    
    total = len(features)
    passing = sum(1 for f in features if f.get('passes', False))
    incomplete = total - passing
    
    print(f"\n🎯 Progress Check: {data.get('project', 'Unnamed')}")
    print(f"   {passing}/{total} features complete ({passing/total*100:.1f}%)")
    
    if incomplete == 0:
        print("\n🎉 All features complete! Project is ready.")
        return
    
    # Suggest next features
    suggestions = suggest_next_features(data)
    
    print(f"\n📋 Recommended Next Steps ({incomplete} remaining):")
    for i, feat in enumerate(suggestions, 1):
        status = "🔴" if not feat.get('passes') else "🟢"
        cat = feat.get('category', 'uncategorized')
        desc = feat.get('description', 'No description')[:60]
        print(f"   {i}. {status} [{cat}] {desc}...")
        print(f"      ID: {feat.get('id', 'N/A')}")
    
    # Show by category
    categories = {}
    for f in features:
        if not f.get('passes'):
            cat = f.get('category', 'uncategorized')
            categories[cat] = categories.get(cat, 0) + 1
    
    if categories:
        print(f"\n📊 Incomplete by Category:")
        for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            print(f"   - {cat}: {count} remaining")


def main():
    # Determine file path
    if len(sys.argv) > 1:
        filepath = Path(sys.argv[1])
    else:
        filepath = Path('features.json')
    
    if not filepath.exists():
        print(f"Features file not found: {filepath}")
        print("Usage: python check_progress.py [path/to/features.json]")
        sys.exit(1)
    
    data = load_features(filepath)
    if data is None:
        sys.exit(1)
    
    print_recommendations(data)


if __name__ == '__main__':
    main()
