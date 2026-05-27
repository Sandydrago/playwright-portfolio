import json
import os

def load_config(env: str = None):
    env = env or os.getenv("TEST_ENV", "dev")
    config_path = os.path.join(os.path.dirname(__file__), f"{env}.json")

    with open(config_path, "r") as f:
        return json.load(f)
