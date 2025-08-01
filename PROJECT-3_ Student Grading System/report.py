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
