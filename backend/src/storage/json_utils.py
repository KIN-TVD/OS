import json
import os
from typing import Dict, Any

def save_json(filepath: str, data: Dict[str, Any]) -> None:
    """Save a dictionary to a JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_json(filepath: str) -> Dict[str, Any]:
    """Load a dictionary from a JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
