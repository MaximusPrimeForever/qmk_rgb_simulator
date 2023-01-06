"""A keyboard .json parser."""
import os
import json
from typing import List

from src.exceptions.io import JSONError
from src.layout.key import Key


class Matrix:
    """Parse keyboard info.json file, and load into python objects."""

    def __init__(self, path_to_json: str) -> None:
        if not os.path.exists(path_to_json):
            raise FileNotFoundError("Path to keyboard layout json was not found.")

        self._json = {}
        with open(path_to_json, 'r') as f:
            self._json = json.load(f)

        if not self._json:
            raise JSONError("Failed to read info.json file.")

        if not self.verify_json_format(self._json):
            raise JSONError("Given file is not a valid info.json file.")

        # Get first layout
        first_layout = next(iter(self._json["layouts"].values()))
        json_layout = first_layout["layout"]

        # Build matrix as a 2D array
        max_row, max_col = self._get_max_row_and_column(json_layout)
        self._array = [[None] * max_col for _ in range(max_row)]
        self.width = max_col
        self.height = max_row

        for row in json_layout:
            x, y = row['matrix']
            key_width = 1
            if 'w' in row:
                key_width = row['w']

            self._array[x][y] = Key(x=row['x'], y=row['y'], width=key_width)

        self.height_total, self.width_total = self.compute_keyboard_size(
            self._array
        )
        pass

    def __getitem__(self, *args):
        self._array.__getitem__(*args)

    @staticmethod
    def verify_json_format(parsed_json: dict) -> bool:
        """Verify the read json is a info.json file."""
        return True

    @staticmethod
    def _get_max_row_and_column(keyboard_matrix: dict):
        """Return the max row and column indices from the matrix layout."""
        x_max, y_max = 0, 0
        for row in keyboard_matrix:
            row_x, row_y = row["matrix"]

            if row_x > x_max:
                x_max = row_x

            if row_y > y_max:
                y_max = row_y

        return x_max + 1, y_max + 1

    def get_keys_in_row(self, row_index: int) -> list:
        """Return a list of keys in a given row."""
        if not 0 <= row_index < self.height:
            raise IndexError(
                f"Given row index {row_index} is out of bounds: 0-{self.height}."
            )
        return self._array[row_index]

    def get_keys_in_column(self, col_index: int) -> list:
        """Return a list of keys in a given column."""
        if not 0 <= col_index < self.width:
            raise IndexError(
                f"Given row index {col_index} is out of bounds: 0-{self.width}."
            )
        keys = []

        for row in self._array:
            keys.append(row[col_index])

        return keys

    @staticmethod
    def compute_keyboard_size(matrix: List[List[Key]]):
        """Iterate rows and columns to get full size of keyboard."""
        keyboard_height, keyboard_width = 0, 0

        # find keyboard height by finding how low the biggest key
        # on the last row reaches
        for key in matrix[-1]:
            # skip non existing keys
            if key is None:
                continue

            key_reach = key.y + key.height
            if key_reach > keyboard_height:
                keyboard_height = key.y + key.height

        # reset key reach just in case
        key_reach = 0

        # iterate the keys in the right most column, and find the largest key
        for row in matrix:
            # find last key in each row
            key = None
            for key in reversed(row):
                if key is not None:
                    break

            # if key is still somehow None, skip the row
            if key is None:
                continue

            key_reach = key.x + key.width

            if key_reach > keyboard_width:
                keyboard_width = key_reach

        # compute gaps between keys
        return keyboard_height, keyboard_width
