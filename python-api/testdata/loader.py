import json
import os

def load_json(filename: str):
    base_path = os.path.join(os.path.dirname(__file__), filename)
    with open(base_path, "r") as f:
        return json.load(f)