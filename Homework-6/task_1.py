class Student:
    def __init__(self, name, birthday, course_level, phone, address):
        self.name = name
        self.birthday = birthday
        self.course_level = course_level
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Student Information:\nName: {self.name}\nBirthday: {self.birthday}\nCourse Level: {self.course_level}\nPhone: {self.phone}\nAddress: {self.address}"


if __name__ == "__main__":
    student_instance = Student(
        name="Muhammad",
        birthday="28.01.2006",
        course_level="2",
        phone="+1(385)349-2209",
        address="Tashkent, Yunusobod")

    print(student_instance)
