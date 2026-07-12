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

def search_student():
    print("\n----- Search Student -----")
    roll = input("Enter roll no. to search: ")
    for student in students:
        if student["roll"] == roll:
            print(f"\nStudent found!")
            print("------------------------")
            print(f"Name   : {student['name']}")
            print(f"Roll   : {student['roll']}")
            print(f"Course : {student['course']}")
            print()
            return
    print("\n❌ Student not found.\n")


def delete_student():

    print("\n----- Delete Student -----")

    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("\n✅ Student deleted successfully!\n")
            return

    print("\n❌ Student not found.\n")
while True:

    print("========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice.\n")