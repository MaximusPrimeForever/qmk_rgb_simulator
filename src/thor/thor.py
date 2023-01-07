"""Light(n)ing simulator."""


from src.layout import Matrix

class Thor:
    def __init__(self, matrix: Matrix, pattern_file_path: str) -> None:
        self.matrix = matrix
        self._pattern_file_path = pattern_file_path

    def _intialize_animation_runner(self):
        pass

    def _step(self):
        """Render a single step in the pattern animation."""

    def run(self):
        pass
