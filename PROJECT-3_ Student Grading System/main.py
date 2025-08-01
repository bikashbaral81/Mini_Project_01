from report import validate_marks, student_exists, save_report, generate_report_card, load_data

FILENAME = "report_data.json"

def main():
    name = input("Enter student name: ").strip()
    data = load_data(FILENAME)

    if student_exists(name, data):
        print(" Student already exists!")
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
        print(" Invalid input! Marks must be integers.")
    except Exception as e:
        print(" Error:", e)

if __name__ == "__main__":
    main()
