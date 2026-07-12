print("Welcome to Student Management System")
students = []

def add_student():
    print("\n----- Add Student -----")

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)

    print("\n✅ Student added successfully!\n")


def view_students():

    print("\n----- Student List -----")

    if len(students) == 0:
        print("No students found.\n")
        return

    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}")
        print(f"Name   : {student['name']}")
        print(f"Roll   : {student['roll']}")
        print(f"Course : {student['course']}")

    print()


while True:

    print("========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice.\n")