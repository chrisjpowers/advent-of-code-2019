class Wire:
    pass

class WireVector():
    def __init__(self, point, direction, length):
        self.point = point
        self.direction = direction
        self.length = length
        self.points = self._build_points()

    def __len__(self):
        return self.length
    
    def __and__(self, other):
        return set(self.points) & set(other.points)

    @property
    def final_point(self):
        ps = self.points
        return ps[len(ps) - 1]
    
    def _build_points(self):
        switch = {
            "U": self._points_up,
            "R": self._points_right,
            "D": self._points_down,
            "L": self._points_left
        }
        return switch[self.direction]()
    
    def _points_right(self):
        p = self.point
        return [WirePoint(x, p.y) for x in range(p.x, p.x + self.length + 1)]
            
    def _points_up(self):
        p = self.point
        return [WirePoint(p.x, y) for y in range(p.y, p.y + self.length + 1)]
            
    def _points_left(self):
        p = self.point
        return [WirePoint(x, p.y) for x in reversed(range(p.x - self.length, p.x + 1))]
            
    def _points_down(self):
        p = self.point
        return [WirePoint(p.x, y) for y in reversed(range(p.y - self.length, p.y + 1))]

    @classmethod
    def parse(cls, point, vector_string):
        direction = vector_string[0]
        length = int(vector_string[1:])
        return cls(point, direction, length)

class WirePoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return abs(self.x) + abs(self.y)
    
    def __eq__(self, other):
        return (
            isinstance(other, WirePoint) and
            self.x == other.x and
            self.y == other.y
        )
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f'<WirePoint x={self.x} y={self.y}>'