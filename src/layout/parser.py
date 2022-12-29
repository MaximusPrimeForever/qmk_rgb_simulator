"""A keyboard .json parser."""
import os
import json


class KeyboardLayout:
    def __init__(self, path_to_json: str) -> None:
        if not os.path.exists(path_to_json):
            raise FileNotFoundError("Path to keyboard layout json was not found.")

        self.json = None
        with open(path_to_json, 'r') as f:
            self.json = json.load(f)
