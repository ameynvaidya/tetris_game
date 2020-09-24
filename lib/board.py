from typing import List
import lib.piece as piece

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

    def set_piece(self, x: int, y: int, piece: piece.Piece) -> None:
        for point in piece.getBody():
            self.set_grid(x + point.getX(), y +  point.getY(), piece.getColor())

    def set_grid(self, x: int, y: int, color: int) -> None:
        if (x >= 0 or x < self._width) and (y >= 0 or y < self._height):
            self._grid[y * self._width + x] = color
    
    def get_grid(self, x: int, y: int) -> int:
        if (x >= 0 or x < self._width) and (y >= 0 or y < self._height):
            return self._grid[y * self._width + x]
        return 0

    def fill_fake_data(self) -> None:
        self.set_piece(0, -1, piece.Piece.get_pieces()[0])
        self.set_piece(0, 0, piece.Piece.get_pieces()[1].nextRotation().nextRotation())
        self.set_piece(2, 1, piece.Piece.get_pieces()[2].nextRotation().nextRotation().nextRotation())
        self.set_piece(4, -1, piece.Piece.get_pieces()[5].nextRotation().nextRotation())
        self.set_piece(6, 0, piece.Piece.get_pieces()[6])
        self.set_piece(4, 1, piece.Piece.get_pieces()[3])
        self.set_piece(-1, 2, piece.Piece.get_pieces()[4].nextRotation())