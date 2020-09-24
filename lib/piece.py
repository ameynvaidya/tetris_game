from typing import List
import lib.point as p

class Piece:
    def __init__(self, points : List[p.Point], color: int):
        super().__init__()
        self._points = points
        self._next = None
        self._color = color

    def setNextRotatedPiece(self, nxt) -> None:
        self._next = nxt
    
    def getBody(self) -> List[p.Point]:
        return self._points

    def getColor(self) -> int:
        return self._color

    def nextRotation(self):
        return self._next

    @staticmethod
    def get_pieces():
        p_0_a = Piece([p.Point(0, 1), p.Point(1, 1), p.Point(2, 1), p.Point(3, 1)], 1)
        p_0_b = Piece([p.Point(2, 3), p.Point(2, 2), p.Point(2, 1), p.Point(2, 0)], 1)
        p_0_b.setNextRotatedPiece(p_0_a)
        p_0_a.setNextRotatedPiece(p_0_b)

        p_1_a = Piece([p.Point(0, 1), p.Point(1, 1), p.Point(2, 1), p.Point(2, 0)], 2)
        p_1_b = Piece([p.Point(0, 0), p.Point(1, 0), p.Point(1, 1), p.Point(1, 2)], 2)
        p_1_c = Piece([p.Point(0, 2), p.Point(0, 1), p.Point(1, 1), p.Point(2, 1)], 2)
        p_1_d = Piece([p.Point(1, 0), p.Point(1, 1), p.Point(1, 2), p.Point(2, 2)], 2)
        p_1_d.setNextRotatedPiece(p_1_a)
        p_1_a.setNextRotatedPiece(p_1_b)
        p_1_b.setNextRotatedPiece(p_1_c)
        p_1_c.setNextRotatedPiece(p_1_d)

        p_2_a = Piece([p.Point(0, 0), p.Point(0, 1), p.Point(1, 1), p.Point(2, 1)], 3)
        p_2_b = Piece([p.Point(0, 2), p.Point(1, 2), p.Point(1, 1), p.Point(1, 0)], 3)
        p_2_c = Piece([p.Point(0, 1), p.Point(1, 1), p.Point(2, 1), p.Point(2, 2)], 3)
        p_2_d = Piece([p.Point(1, 2), p.Point(1, 1), p.Point(1, 0), p.Point(2, 0)], 3)
        p_2_d.setNextRotatedPiece(p_2_a)
        p_2_a.setNextRotatedPiece(p_2_b)
        p_2_b.setNextRotatedPiece(p_2_c)
        p_2_c.setNextRotatedPiece(p_2_d)

        p_3_a = Piece([p.Point(1, 1), p.Point(1, 2), p.Point(2, 1), p.Point(2, 2)], 4)
        p_3_a.setNextRotatedPiece(p_3_a)

        p_4_a = Piece([p.Point(0, 0), p.Point(1, 0), p.Point(1, 1), p.Point(2, 1)], 5)
        p_4_b = Piece([p.Point(1, 2), p.Point(1, 1), p.Point(2, 1), p.Point(2, 0)], 5)
        p_4_b.setNextRotatedPiece(p_4_a)
        p_4_a.setNextRotatedPiece(p_4_b)

        p_5_a = Piece([p.Point(0, 1), p.Point(1, 1), p.Point(1, 0), p.Point(2, 1)], 6)
        p_5_b = Piece([p.Point(0, 1), p.Point(1, 2), p.Point(1, 1), p.Point(1, 0)], 6)
        p_5_c = Piece([p.Point(0, 1), p.Point(1, 1), p.Point(1, 2), p.Point(2, 1)], 6)
        p_5_d = Piece([p.Point(1, 2), p.Point(1, 1), p.Point(1, 0), p.Point(2, 1)], 6)
        p_5_d.setNextRotatedPiece(p_5_a)
        p_5_a.setNextRotatedPiece(p_5_b)
        p_5_b.setNextRotatedPiece(p_5_c)
        p_5_c.setNextRotatedPiece(p_5_d)
        
        p_6_a = Piece([p.Point(0, 1), p.Point(1, 1), p.Point(1, 0), p.Point(2, 0)], 7)
        p_6_b = Piece([p.Point(1, 0), p.Point(1, 1), p.Point(2, 1), p.Point(2, 2)], 7)
        p_6_b.setNextRotatedPiece(p_6_a)
        p_6_a.setNextRotatedPiece(p_6_b)

        return [p_0_a, p_1_a, p_2_a, p_3_a, p_4_a, p_5_a, p_6_a]