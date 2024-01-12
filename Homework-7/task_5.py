class FindMedian:
    def __init__(self, value1, value2, value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def get_median(self):
        values = [self.value1, self.value2, self.value3]
        values.sort()
        median = values[1]
        return median


def main():
    value1 = float(input("Enter 1-value: "))
    value2 = float(input("Enter 2-value: "))
    value3 = float(input("Enter 3-value: "))

    find_median_instance = FindMedian(value1, value2, value3)
    result = find_median_instance.get_median()

    print("Entered values:", (value1, value2, value3))
    print("Result:", result)


if __name__ == "__main__":
    main()
