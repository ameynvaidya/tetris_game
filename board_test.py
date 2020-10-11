import unittest
import lib.board as b
import lib.piece as p

class BoardTest(unittest.TestCase):

    def test_drop_height(self):
        board  = b.Board(10, 20)
        piece = p.Piece.get_pieces_map()[p.PieceType.STICK]
        d = board.drop_height(0, piece)
        self.assertEqual(-1, d, "drop height mismatch")

if __name__ == '__main__':
    unittest.main()