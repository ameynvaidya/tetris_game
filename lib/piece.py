from typing import List
import lib.point as p
from enum import Enum


class PieceType(Enum):
    STICK = 0,
    INVERSE_L = 1,
    L = 2,
    SQUARE = 3,
    S = 4,
    PYRAMID = 5,
    INVERSE_S = 6


class Piece:
    def __init__(self, points: List[p.Point], color: int):
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
    def piece_color_map():
        return {
            1: (0, 255, 255),  # aqua Stick
            2: (0, 0, 255),   # blue  L Inverse
            3: (255, 165, 0),  # orange L
            4: (255, 255, 0),  # yellow Square
            5: (0, 255, 0),  # green S
            6: (217, 49, 255),  # purple Pyramid
            7: (255, 0, 0),  # red S Inverse
            0: (0, 0, 0),  # black blank
        }

    @staticmethod
    def get_pieces_map():
        p_0_a = Piece([p.Point(0, 1), p.Point(1, 1),
                       p.Point(2, 1), p.Point(3, 1)], 1)
        p_0_b = Piece([p.Point(2, 3), p.Point(2, 2),
                       p.Point(2, 1), p.Point(2, 0)], 1)
        p_0_b.setNextRotatedPiece(p_0_a)
        p_0_a.setNextRotatedPiece(p_0_b)

        p_1_a = Piece([p.Point(0, 1), p.Point(1, 1),
                       p.Point(2, 1), p.Point(2, 0)], 2)
        p_1_b = Piece([p.Point(0, 0), p.Point(1, 0),
                       p.Point(1, 1), p.Point(1, 2)], 2)
        p_1_c = Piece([p.Point(0, 2), p.Point(0, 1),
                       p.Point(1, 1), p.Point(2, 1)], 2)
        p_1_d = Piece([p.Point(1, 0), p.Point(1, 1),
                       p.Point(1, 2), p.Point(2, 2)], 2)
        p_1_d.setNextRotatedPiece(p_1_a)
        p_1_a.setNextRotatedPiece(p_1_b)
        p_1_b.setNextRotatedPiece(p_1_c)
        p_1_c.setNextRotatedPiece(p_1_d)

        p_2_a = Piece([p.Point(0, 0), p.Point(0, 1),
                       p.Point(1, 1), p.Point(2, 1)], 3)
        p_2_b = Piece([p.Point(0, 2), p.Point(1, 2),
                       p.Point(1, 1), p.Point(1, 0)], 3)
        p_2_c = Piece([p.Point(0, 1), p.Point(1, 1),
                       p.Point(2, 1), p.Point(2, 2)], 3)
        p_2_d = Piece([p.Point(1, 2), p.Point(1, 1),
                       p.Point(1, 0), p.Point(2, 0)], 3)
        p_2_d.setNextRotatedPiece(p_2_a)
        p_2_a.setNextRotatedPiece(p_2_b)
        p_2_b.setNextRotatedPiece(p_2_c)
        p_2_c.setNextRotatedPiece(p_2_d)

        p_3_a = Piece([p.Point(1, 1), p.Point(1, 2),
                       p.Point(2, 1), p.Point(2, 2)], 4)
        p_3_a.setNextRotatedPiece(p_3_a)

        p_4_a = Piece([p.Point(0, 0), p.Point(1, 0),
                       p.Point(1, 1), p.Point(2, 1)], 5)
        p_4_b = Piece([p.Point(1, 2), p.Point(1, 1),
                       p.Point(2, 1), p.Point(2, 0)], 5)
        p_4_b.setNextRotatedPiece(p_4_a)
        p_4_a.setNextRotatedPiece(p_4_b)

        p_5_a = Piece([p.Point(0, 1), p.Point(1, 1),
                       p.Point(1, 0), p.Point(2, 1)], 6)
        p_5_b = Piece([p.Point(0, 1), p.Point(1, 2),
                       p.Point(1, 1), p.Point(1, 0)], 6)
        p_5_c = Piece([p.Point(0, 1), p.Point(1, 1),
                       p.Point(1, 2), p.Point(2, 1)], 6)
        p_5_d = Piece([p.Point(1, 2), p.Point(1, 1),
                       p.Point(1, 0), p.Point(2, 1)], 6)
        p_5_d.setNextRotatedPiece(p_5_a)
        p_5_a.setNextRotatedPiece(p_5_b)
        p_5_b.setNextRotatedPiece(p_5_c)
        p_5_c.setNextRotatedPiece(p_5_d)

        p_6_a = Piece([p.Point(0, 1), p.Point(1, 1),
                       p.Point(1, 0), p.Point(2, 0)], 7)
        p_6_b = Piece([p.Point(1, 0), p.Point(1, 1),
                       p.Point(2, 1), p.Point(2, 2)], 7)
        p_6_b.setNextRotatedPiece(p_6_a)
        p_6_a.setNextRotatedPiece(p_6_b)

        return {
            PieceType.STICK: p_0_a,
            PieceType.INVERSE_L: p_1_a,
            PieceType.L: p_2_a,
            PieceType.SQUARE: p_3_a,
            PieceType.S: p_4_a,
            PieceType.PYRAMID: p_5_a,
            PieceType.INVERSE_S: p_6_a,
        }

    @staticmethod
    def get_pieces():
        map = Piece.get_pieces_map()
        return list(map.values())