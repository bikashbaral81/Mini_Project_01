from report import (
    validate_marks, student_exists, save_report,
    generate_report_card, load_data, display_all_students,
    update_student
)

FILENAME = "report_data.json"

def add_student():
    name = input("Enter student name: ").strip()
    data = load_data(FILENAME)

    if student_exists(name, data):
        print("Student already exists!")
        return

    try:
        n = int(input("Enter number of subjects: "))
        subjects = []
        marks = []

        for _ in range(n):
            sub = input("Enter subject name: ").strip()
            try:
                mark = int(input(f"Enter marks for {sub} (0-100): "))
            except ValueError:
                print("Invalid input! Marks must be a number.")
                return

            if validate_marks(mark):
                subjects.append(sub)
                marks.append(mark)
            else:
                print("Invalid marks! Must be between 0 and 100.")
                return

        save_report(name, subjects, marks, FILENAME)
        generate_report_card(name, subjects, marks)

    except ValueError:
        print("Invalid input!")
    except Exception as e:
        print("Error:", e)

def menu():
    while True:
        print("\n--- Student Report Card System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Marks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students(FILENAME)
        elif choice == "3":
            name = input("Enter student name to update: ").strip()
            update_student(name, FILENAME)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
