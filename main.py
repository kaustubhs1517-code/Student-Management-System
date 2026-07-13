import json


print("\n" + "=" * 65)
print("🎓 WELCOME TO STUDENT MANAGEMENT SYSTEM 🎓".center(65))
print("=" * 65)
print("📚 Add | 🔍 Search | ✏️ Update | 🗑️ Delete | 👀 View".center(65))
print("💾 JSON Data Storage Enabled".center(65))
print("=" * 65)
students = []




def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []





def save_students():

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)





def add_student():

    print("\n----- Add Student -----")

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    # Check if roll number already exists
    for student in students:
        if student["roll"] == roll:
            print("\n❌ Roll number already exists!\n")
            return

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)
    save_students()

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
            save_students()
            print("\n✅ Student deleted successfully!\n")
            return

    print("\n❌ Student not found.\n")






def update_student():

    print("\n----- Update Student -----")

    roll = input("Enter roll number to update: ")

    for student in students:

        if student["roll"] == roll:

            print("\nCurrent Details")
            print("----------------")
            print(f"Name   : {student['name']}")
            print(f"Course : {student['course']}")

            new_name = input("\nEnter new name: ")
            new_course = input("Enter new course: ")

            student["name"] = new_name
            student["course"] = new_course

            save_students()

            print("\n✅ Student updated successfully!\n")
            return

    print("\n❌ Student not found.\n")

def main():

    load_students()

    while True:

        print("\n📋 MAIN MENU")
        print("-" * 30)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        print("-" * 30)
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
            update_student()

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()