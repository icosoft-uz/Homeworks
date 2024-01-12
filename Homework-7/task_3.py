class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area


def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    rectangle_instance = Rectangle(length, width)
    area_result = rectangle_instance.calculate_area()

    print("Length:", length)
    print("Width:", width)
    print("Area:", area_result)


if __name__ == "__main__":
    main()
