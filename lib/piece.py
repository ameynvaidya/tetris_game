from typing import List
import lib.point

class Piece:
    def __init__(self, points : List[point.Point]):
        super().__init__()
        self._points = points
    
    def getBody(self) -> List[point.Point]:
        return self._points