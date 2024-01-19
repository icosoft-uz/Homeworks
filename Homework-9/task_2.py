from geopy.distance import geodesic


class Calculate:
    def __init__(self, a_point, b_point):
        self.point_a = a_point
        self.point_b = b_point

    def calculate_distance(self):
        distance_1 = geodesic(
            (self.point_a.lat, self.point_a.lon),
            (self.point_b.lat, self.point_b.lon)
        ).kilometers
        return distance_1


class Point:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


if __name__ == "__main__":
    point_a = Point(41.26465, 69.21627)  # Tashkent
    point_b = Point(40.9983, 71.67257)  # Namangan

    distance_calculator = Calculate(point_a, point_b)
    distance = distance_calculator.calculate_distance()

    print(f"Distance between San Namangan and Tashkent: {distance} kilometers")
