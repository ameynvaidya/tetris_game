import lib.board as b
import lib.piece as pc

class Brain:
    def __init__(self, board: b.Board):
        super().__init__()
        self._board = board

    def find_best_position(self, piece: pc.Piece, piece_x: int, piece_y: int) -> (int, int, pc.Piece):
        best_x = piece_x
        best_y = piece_y
        best_piece = piece
        max_score = -1000
        temp_piece = piece
        for r in range(4):
            for x in range(-4, self._board.width(), 1):
                drop_piece_y = self._board.drop_height(x, piece_y, temp_piece)
                if (self._board.is_piece_out_of_bound(x, drop_piece_y, temp_piece)):
                    continue
                if (self._board.did_piece_collided_with_body(x, drop_piece_y, temp_piece)):
                    continue
                self._board.set_piece(x, drop_piece_y, temp_piece)
                score = self.find_score(drop_piece_y)
                if score > max_score:
                    best_x = x
                    best_y = drop_piece_y
                    best_piece = temp_piece
                    max_score = score
                self._board.revert_transaction()
            temp_piece = temp_piece.nextRotation()
        print(f"BEST SCORE: {max_score}")
        return (best_x, best_y, best_piece)

    def find_score(self, y: int) -> int:
        return -20 * self._board.get_hole_count() - 1 * y
