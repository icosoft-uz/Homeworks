import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)

    def __sub__(self, other_point):
        return self.distance(other_point)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    point_a = Point(41.26465, 69.21627)  # Tashkent
    point_b = Point(40.9983, 71.67257)  # Namangan

    distance_between_points = point_a - point_b

    print(f"The distance between {point_a} and {point_b} is: {distance_between_points}")
