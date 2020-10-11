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
        self._need_to_clear_rows = False
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
        if self._need_to_clear_rows:
            self.clear_rows()

    def clear_rows(self):
        to_row = 0
        temp_grid = []
        temp_row_stats = []
        for _ in range(self._height * self._width):
            temp_grid.append(0)
        for i in range(self._height):
            temp_row_stats.append(0)

        for from_row in range(self._height):
            if self.row_stats[from_row] != self._width:
                temp_row_stats[to_row] = self.row_stats[from_row]
                for i in range(self._width):
                    temp_grid[to_row * self._width + i] = self._grid[from_row * self._width + i]
                to_row = to_row + 1
        self._grid = temp_grid
        self.row_stats = temp_row_stats
        self._need_to_clear_rows = False


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

    def drop_height(self, x: int, current_y: int, piece: piece.Piece) -> int:
        for y in range(current_y, -4, -1):
            if (self.is_piece_out_of_bound(x, y, piece) or 
                self.did_piece_collided_with_body(x, y, piece)):
                return y + 1
        return self._height

    def set_grid(self, x: int, y: int, color: int) -> None:
        if (x >= 0 or x < self._width) and (y >= 0 or y < self._height):
            self._grid[y * self._width + x] = color
            self.row_stats[y] = self.row_stats[y] + 1
            if self.row_stats[y] == self._width:
                self._need_to_clear_rows = True
    
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