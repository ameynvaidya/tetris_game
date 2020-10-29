from typing import List
import lib.piece as piece
import lib.grid as g
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

        self._committed_grid = g.Grid(width, height)
        self._uncommitted_grid = g.Grid(width, height)

        self._uncommitted_score = 0
        self._uncommitted_lines = 0

        self.score = 0
        self.lines = 0

        self._need_to_clear_rows = False

        self._points_table = {
            1: 40,
            2: 100,
            3: 300,
            4: 1200,
        }
        
    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width

    def set_piece(self, x: int, y: int, piece: piece.Piece, grid: g.Grid = None) -> None:
        if grid is None:
            grid = self._uncommitted_grid
        for point in piece.getBody():
            self.set_grid(x + point.getX(), y +  point.getY(), piece.getColor(), grid)
        if self._need_to_clear_rows:
            self.clear_rows(grid)

    def clear_rows(self, grid: g.Grid):
        to_row = 0
        t_grid = g.Grid(grid.width, grid.height)
        line_counter = 0
        for from_row in range(self._height):
            if grid.row_stats[from_row] != self._width:
                t_grid.row_stats[to_row] = grid.row_stats[from_row]
                for i in range(self._width):
                    t_grid._grid[to_row * self._width + i] = grid._grid[from_row * self._width + i]
                to_row = to_row + 1
            else:
                line_counter = line_counter + 1
        
        self._uncommitted_lines = self._uncommitted_lines + line_counter
        self._uncommitted_score = self._uncommitted_score + self._points_table[line_counter]
        self._uncommitted_grid = t_grid
        self._need_to_clear_rows = False

    def commit_transaction(self) -> None:
        for i in range(self._width * self._height):
            self._committed_grid._grid[i] = self._uncommitted_grid._grid[i]
        for i in range(self._height):
            self._committed_grid.row_stats[i] = self._uncommitted_grid.row_stats[i]
        self.score = self._uncommitted_score
        self.lines = self._uncommitted_lines

    def revert_transaction(self) -> None:
        for i in range(self._width * self._height):
            self._uncommitted_grid._grid[i] = self._committed_grid._grid[i]
        for i in range(self._height):
            self._uncommitted_grid.row_stats[i] = self._committed_grid.row_stats[i]
        self._uncommitted_score = self.score
        self._uncommitted_lines = self.lines

    def is_piece_out_of_bound(self, x: int, y: int, piece: piece.Piece) -> bool:
        for p in piece.getBody():
            if (x + p.getX() < 0 or x + p.getX() >= self._width):
                return True
            if (y + p.getY() < 0 or y + p.getY() >= self._height):
                return True
        return False

    def did_piece_collided_with_body(self, x: int, y: int, piece: piece.Piece, grid: g.Grid = None) -> bool:
        if grid is None:
            grid = self._uncommitted_grid
        for p in piece.getBody():
            p_x = x + p.getX()
            p_y = y + p.getY()
            if (self.get_grid(p_x, p_y, grid) != 0):
                return True
        return False

    def drop_height(self, x: int, current_y: int, piece: piece.Piece, grid: g.Grid = None) -> int:
        if grid is None:
            grid = self._uncommitted_grid
        for y in range(current_y, -4, -1):
            if (self.is_piece_out_of_bound(x, y, piece) or 
                self.did_piece_collided_with_body(x, y, piece, grid)):
                return y + 1
        return self._height

    def set_grid(self, x: int, y: int, color: int, grid: g.Grid) -> None:
        if (x >= 0 or x < self._width) and (y >= 0 or y < self._height):
            grid._grid[y * self._width + x] = color
            grid.row_stats[y] = grid.row_stats[y] + 1
            if grid.row_stats[y] == self._width:
                self._need_to_clear_rows = True
    
    def get_grid(self, x: int, y: int, grid: g.Grid = None) -> int:
        if grid is None:
            grid = self._committed_grid
        if (x >= 0 or x < self._width) and (y >= 0 or y < self._height):
            return grid._grid[y * self._width + x]
        return 0

    def fill_fake_data(self) -> None:
        self.set_piece(0, -1, piece.Piece.get_pieces()[0])
        self.set_piece(0, 0, piece.Piece.get_pieces()[1].nextRotation().nextRotation())
        self.set_piece(2, 1, piece.Piece.get_pieces()[2].nextRotation().nextRotation().nextRotation())
        self.set_piece(4, -1, piece.Piece.get_pieces()[5].nextRotation().nextRotation())
        self.set_piece(6, 0, piece.Piece.get_pieces()[6])
        self.set_piece(4, 1, piece.Piece.get_pieces()[3])
        self.set_piece(-1, 2, piece.Piece.get_pieces()[4].nextRotation())

    def get_hole_count(self) -> int:
        hole_count = 0
        for x in range(self._width):
            hole_count_in_col = 0
            detect_skyline = False
            for y in range(self._height - 1, -1, -1):
                if not detect_skyline and self.get_grid(x, y, self._uncommitted_grid) != 0:
                    detect_skyline = True
                elif detect_skyline and self.get_grid(x, y, self._uncommitted_grid) == 0:
                    hole_count_in_col = hole_count_in_col + 1
            hole_count = hole_count + hole_count_in_col
        return hole_count

    def get_empty_pillar_count(self) -> int:
        pillar_count = 0
        for x in range(self._width):
            pillar_count_in_col = 0
            for y in range(self._height - 1, -1, -1):
                if self.get_grid(x, y, self._uncommitted_grid) != 0:
                    break
                if x == 0:
                    if self.get_grid(x + 1, y, self._uncommitted_grid) != 0:
                        pillar_count_in_col = pillar_count_in_col + 1
                elif x == self._width - 1:
                    if self.get_grid(x - 1, y, self._uncommitted_grid) != 0:
                        pillar_count_in_col = pillar_count_in_col + 1
                elif self.get_grid(x + 1, y, self._uncommitted_grid) != 0 and self.get_grid(x - 1, y, self._uncommitted_grid) != 0:
                    pillar_count_in_col = pillar_count_in_col + 1
                if pillar_count_in_col > 3:
                    pillar_count = pillar_count + pillar_count_in_col - 3
        return pillar_count
