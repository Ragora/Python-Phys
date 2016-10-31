import math

class Vector(object):
    x = None
    y = None

    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, rhs):
        return Vector(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector(self.x - rhs.x, self.y - rhs.y)

    def __mult__(self, rhs):
        if (type(rhs) is Vector):
            return Vector(self.x * rhs.x, self.y * rhs.y)
        return Vector(self.x * rhs, self.y * rhs)

    def __div__(self, rhs):
        if (type(rhs) is Vector):
            return Vector(self.x / rhs.x, self.y / rhs.y)
        return Vector(self.x / rhs, self.y / rhs)

    def __len__(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

    def length(self):
        return len(self)

    def magnitude(self):
        return len(self)

    def normal(self):
        length = len(self)
        return Vector(self.x / length, self.y / length)

    def distance(self, rhs):
        return math.sqrt(pow(self.x - rhs.x, 2) + pow(self.y - rhs.y, 2))

    def slope(self, rhs):
        divisor = (self.x - rhs.x)

        if (divisor == 0):
            return 0

        return (self.y - rhs.y) / divisor

    @staticmethod
    def average_distance(points, from_point):
        result = 0
        for point in points:
            result += point.distance(from_point)

        result /= len(points)
        return result

    def normalize(self):
        length = len(self)
        self.x /= length
        self.y /= length

    def rotate(self, theta):
        sine = math.sin(theta)
        cosine = math.cos(theta)

        return Vector(self.x * cosine - self.y * sine, self.x * sine + self.y * cosine)

    def __repr__(self):
        return "Vector(%f, %f)" % (self.x, self.y)

Vector.zero = Vector()
