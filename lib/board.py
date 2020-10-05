from typing import List
import lib.piece as piece
'''
Board coordinate system
     |   |   |   |   |   |
     |   |   |   |   |   |
y=3  |   |   |   |   |   |
y=1  |   |   |   |   |   |
y=0  |   |   |   |   |   |
      x=0 x=1 x=2                                              
'''
class Board:
    def __init__(self, width=10, height=20):
        super().__init__()
        self._width = width
        self._height = height
        # grid is represented as one dimensional list
        self._grid = []
        self.row_stats = []
        for _ in range(height * width):
            self._grid.append(0)
        for i in range(height):
            self.row_stats.append(0)
        
    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width

    def set_piece(self, x: int, y: int, piece: piece.Piece) -> None:
        for point in piece.getBody():
            self.set_grid(x + point.getX(), y +  point.getY(), piece.getColor())

    def is_piece_out_of_bound(self, x: int, y: int, piece: piece.Piece) -> bool:
        for p in piece.getBody():
            if (x + p.getX() < 0 or x + p.getX() >= self._width):
                return True
            if (y + p.getY() < 0 or y + p.getY() >= self._height):
                return True
        return False

    def did_piece_collided_with_body(self, x: int, y: int, piece: piece.Piece) -> bool:
        for p in piece.getBody():
            p_x = x + p.getX()
            p_y = y + p.getY()
            if (self.get_grid(p_x, p_y) != 0):
                return True
        return False

    def set_grid(self, x: int, y: int, color: int) -> None:
        if (x >= 0 or x < self._width) and (y >= 0 or y < self._height):
            self._grid[y * self._width + x] = color
            self.row_stats[y] = self.row_stats[y] + 1
    
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