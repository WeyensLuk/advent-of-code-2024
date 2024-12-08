class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if type(other) is Coordinate:
            return self.x == other.x and self.y == other.y
        if type(other) is tuple:
            return self.x == other[0] and self.y == other[1]
        
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def inverse(self):
        return Coordinate(self.x * -1, self.y * -1)

    def rotate_90degrees_clockwise(self):
        if self == Coordinate.north(): return Coordinate.east()
        if self == Coordinate.east(): return Coordinate.south()
        if self == Coordinate.south(): return Coordinate.west()
        if self == Coordinate.west(): return Coordinate.north()

    def as_tuple(self):
        return (self.x, self.y)

    @classmethod
    def west(cls):
        return Coordinate(-1, 0)
    
    @classmethod
    def east(cls):
        return Coordinate(1, 0)
    
    @classmethod
    def north(cls):
        return Coordinate(0, -1)

    @classmethod
    def south(cls):
        return Coordinate(0, 1)
    
    @classmethod
    def northwest(cls):
        return Coordinate(-1, -1)
    
    @classmethod
    def northeast(cls):
        return Coordinate(1, -1)
    
    @classmethod
    def southwest(cls):
        return Coordinate(-1, 1)
    
    @classmethod
    def southeast(cls):
        return Coordinate(1, 1)