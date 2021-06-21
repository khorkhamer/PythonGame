import math


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        """
        return a normalized vector. it doesn't change a internal state of the vector.
        """
        return Vector2(round(self.x / self.length()), round(self.y / self.length()))

#    def __len__(self):
#        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def __str__(self):
        return "x: " + str(self.x) + " --- y: " + str(self.y)

    def tuple(self):
        return self.x, self.y
