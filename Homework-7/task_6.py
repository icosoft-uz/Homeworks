class Student:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address


def write_to_file(student_list, filename):
    with open(filename, 'w') as file:
        for student in student_list:
            file.write(f"Name: {student.name}, Phone: {student.phone}, Address: {student.address}\n")


def main():
    student_list = []

    while True:
        name = input("Enter student name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        phone = input("Enter student phone: ")
        address = input("Enter student address: ")

        student = Student(name, phone, address)
        student_list.append(student)

        add_more = input("Do you want to add more students? (yes/no): ")
        if add_more.lower() != 'yes':
            break

    filename = input("Enter the file name to save the information (e.g., student.txt): ")
    write_to_file(student_list, filename)

    print(f"Student information has been saved to {filename}.")


if __name__ == "__main__":
    main()
