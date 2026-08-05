from collections import defaultdict

class CountSquares:
    def __init__(self):
        self.pts = []
        self.pts_to_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.pts_to_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.pts:
            if(
                x == px
                or y == py
                or abs(px - x) != abs(py - y)
            ):
                continue
            
            res += self.pts_to_count[(x, py)] * self.pts_to_count[(px, y)]

        return res
