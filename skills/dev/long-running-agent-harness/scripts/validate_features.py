#!/usr/bin/env python3
"""
validate_features.py - Validate features.json format and integrity

Usage:
    python validate_features.py [path/to/features.json]

If no path provided, looks for features.json in current directory.
"""

import json
import sys
from pathlib import Path


def validate_features(filepath: Path) -> tuple[bool, list[str]]:
    """Validate a features.json file."""
    errors = []
    
    # Check file exists
    if not filepath.exists():
        return False, [f"File not found: {filepath}"]
    
    # Try to parse JSON
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"]
    except Exception as e:
        return False, [f"Error reading file: {e}"]
    
    # Check required top-level fields
    required_fields = ['project', 'features']
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")
    
    # Check features array
    if 'features' in data:
        if not isinstance(data['features'], list):
            errors.append("'features' must be an array")
        else:
            # Validate each feature
            feature_ids = set()
            for i, feature in enumerate(data['features']):
                if not isinstance(feature, dict):
                    errors.append(f"Feature {i}: must be an object")
                    continue
                
                # Check feature fields
                if 'id' not in feature:
                    errors.append(f"Feature {i}: missing 'id'")
                elif feature['id'] in feature_ids:
                    errors.append(f"Feature {i}: duplicate id '{feature['id']}'")
                else:
                    feature_ids.add(feature['id'])
                
                if 'description' not in feature:
                    errors.append(f"Feature {i}: missing 'description'")
                
                if 'passes' not in feature:
                    errors.append(f"Feature {i}: missing 'passes'")
                elif not isinstance(feature['passes'], bool):
                    errors.append(f"Feature {i}: 'passes' must be boolean")
                
                # Check steps if present
                if 'steps' in feature and not isinstance(feature['steps'], list):
                    errors.append(f"Feature {i}: 'steps' must be an array")
    
    return len(errors) == 0, errors


def print_summary(data: dict) -> None:
    """Print a summary of the features file."""
    features = data.get('features', [])
    total = len(features)
    passing = sum(1 for f in features if f.get('passes', False))
    
    # Group by category
    categories = {}
    for f in features:
        cat = f.get('category', 'uncategorized')
        categories[cat] = categories.get(cat, 0) + 1
    
    print(f"\n📊 Features Summary")
    print(f"   Project: {data.get('project', 'Unnamed')}")
    print(f"   Total: {total}")
    print(f"   Passing: {passing} ({passing/total*100:.1f}%)" if total > 0 else "   Passing: 0")
    print(f"   Remaining: {total - passing}")
    
    if categories:
        print(f"\n   By Category:")
        for cat, count in sorted(categories.items()):
            cat_passing = sum(1 for f in features if f.get('category') == cat and f.get('passes'))
            print(f"     - {cat}: {cat_passing}/{count}")


def main():
    # Determine file path
    if len(sys.argv) > 1:
        filepath = Path(sys.argv[1])
    else:
        filepath = Path('features.json')
    
    print(f"Validating: {filepath.absolute()}")
    
    # Validate
    is_valid, errors = validate_features(filepath)
    
    if not is_valid:
        print("\n❌ Validation Failed")
        for error in errors:
            print(f"   ✗ {error}")
        sys.exit(1)
    
    # Load and print summary
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    print_summary(data)
    print("\n✅ Features file is valid")


if __name__ == '__main__':
    main()
