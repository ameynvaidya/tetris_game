class Point:
    def __init__(self, x: int, y: int):
        super().__init__()
        self._x = x
        self._y = y
    
    def getX(self) -> int:
        return self._x
    
    def getY(self) -> int:
        return self._y

    def print(self) -> None:
        print(f" X = {self._x}, Y = {self._y}")