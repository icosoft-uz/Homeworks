import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        # Area = πr^2
        area = math.pi * self.radius ** 2
        return area

    def calculate_circumference(self):
        # circumference = 2πr
        circumference = 2 * math.pi * self.radius
        return circumference


def main():
    radius = float(input("Enter radius: "))

    circle_instance = Circle(radius)
    area_result = circle_instance.calculate_area()
    circumference_result = circle_instance.calculate_circumference()

    print("Radius:", radius)
    print("Area:", area_result)
    print("Circumference:", circumference_result)


if __name__ == "__main__":
    main()
