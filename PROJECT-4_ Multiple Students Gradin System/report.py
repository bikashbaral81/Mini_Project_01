import json
import os

def load_data(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as file:
        return json.load(file)

def save_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def validate_marks(mark):
    return 0 <= mark <= 100

def student_exists(name, data):
    return name in data

def save_report(name, subjects, marks, filename):
    data = load_data(filename)
    data[name] = {}
    for i in range(len(subjects)):
        data[name][subjects[i]] = marks[i]
    save_data(data, filename)

def generate_report_card(name, subjects, marks):
    print("\n--- Report Card ---")
    print("Name:", name)
    total = 0
    for i in range(len(subjects)):
        print(subjects[i] + ":", marks[i])
        total += marks[i]
    average = total / len(marks)
    print("Average:", round(average, 2))
    print("Result:", "Pass" if average >= 40 else "Fail")

def display_all_students(filename):
    data = load_data(filename)
    if not data:
        print("No students found.")
        return
    for name, subjects in data.items():
        print("\nStudent:", name)
        total = 0
        count = 0
        for sub, mark in subjects.items():
            print(f"{sub}: {mark}")
            total += mark
            count += 1
        avg = total / count if count else 0
        print("Average:", round(avg, 2))
        print("Result:", "Pass" if avg >= 40 else "Fail")

def update_student(name, filename):
    data = load_data(filename)
    if name not in data:
        print("Student not found.")
        return

    print("Enter updated marks:")
    for sub in data[name]:
        try:
            mark = int(input(f"{sub} (old: {data[name][sub]}): "))
            if validate_marks(mark):
                data[name][sub] = mark
            else:
                print("Invalid marks! Skipping.")
        except:
            print("Invalid input! Skipping.")

    save_data(data, filename)
    print("Marks updated successfully.")
