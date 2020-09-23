from typing import List

class Board:
    def __init__(self, width=10, height=20):
        super().__init__()
        self._width = width
        self._height = height
        # grid is represented as one dimensional list
        self._grid = []
        for _ in range(height * width):
            self._grid.append(0)
        
    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width

    def set_piece(self, x: int, y: int, type: int) -> None:
        pass

    def set_grid(self, x: int, y: int, color: int) -> None:
        if x < 0 or x > self._width:
            raise Exception("X is out of range")
        if y < 0 or y > self._height:
            raise Exception("Y is out of range")
        self._grid[y * self._width + x] = color
    
    def get_grid(self, x: int, y: int) -> int:
        if x < 0 or x > self._width:
            raise Exception("X is out of range")
        if y < 0 or y > self._height:
            raise Exception("Y is out of range")
        return self._grid[y * self._width + x]
