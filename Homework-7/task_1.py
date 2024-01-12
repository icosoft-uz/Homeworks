class Person:
    def __init__(self, name, birthday, phone, address):
        self.name = name
        self.birthday = birthday
        self.phone = phone
        self.address = address


class Student(Person):
    def __init__(self, name, birthday, phone, address, course):
        super().__init__(name, birthday, phone, address)
        self.course = course


def display_student_info(student):
    print(f"Name: {student.name}")
    print(f"Birthday: {student.birthday}")
    print(f"Phone: {student.phone}")
    print(f"Address: {student.address}")
    print(f"Course: {student.course}")


def main():
    student_name = input("Enter student name: ")
    student_birthday = input("Enter student birthday: ")
    student_phone = input("Enter student phone: ")
    student_address = input("Enter student address: ")
    student_course = input("Enter student course: ")

    student = Student(student_name, student_birthday, student_phone, student_address, student_course)

    print("\nStudent Information:")
    display_student_info(student)


if __name__ == "__main__":
    main()
