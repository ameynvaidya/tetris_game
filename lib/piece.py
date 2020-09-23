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
        return [p_0_a]