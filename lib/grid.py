class Grid:
    def __init__(self, width=10, height=20):
        super().__init__()
        self._grid = []
        self.row_stats = []
        self.width = width
        self.height = height
        for _ in range(self.height * self.width):
            self._grid.append(0)
        for i in range(self.height):
            self.row_stats.append(0)