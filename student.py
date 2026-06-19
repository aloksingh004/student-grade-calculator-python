import os

RECORDS_FILE = "student_records.txt"


class Student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks 

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self):
        total_possible = len(self.marks) * 100
        return (self.total_marks() / total_possible) * 100

    def grade(self):
        pct = self.percentage()
        if pct >= 90:
            return "A+"
        elif pct >= 80:
            return "A"
        elif pct >= 70:
            return "B"
        elif pct >= 60:
            return "C"
        elif pct >= 50:
            return "D"
        else:
            return "F"

    def summary(self):
        return (
            f"Name: {self.name}\n"
            f"Roll No: {self.roll_number}\n"
            f"Marks: {self.marks}\n"
            f"Total: {self.total_marks()}\n"
            f"Percentage: {self.percentage():.2f}%\n"
            f"Grade: {self.grade()}\n"
        )

    def to_record_line(self):
        marks_str = ";".join(f"{subj}:{score}" for subj, score in self.marks.items())
        return (
            f"{self.roll_number}|{self.name}|{marks_str}|"
            f"{self.total_marks()}|{self.percentage():.2f}|{self.grade()}"
        )


def get_student_input():
    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()

    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects > 0:
                break
            print("Number of subjects must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    marks = {}
    for i in range(num_subjects):
        subject = input(f"Enter subject {i + 1} name: ").strip()
        while True:
            try:
                score = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= score <= 100:
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
        marks[subject] = score

    return Student(name, roll_number, marks)


def save_record(student):
    with open(RECORDS_FILE, "a") as f:
        f.write(student.to_record_line() + "\n")
    print("Record saved successfully.\n")


def view_all_records():
    if not os.path.exists(RECORDS_FILE):
        print("No records found yet.\n")
        return

    with open(RECORDS_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        print("No records found yet.\n")
        return

    print("\n--- All Student Records ---")
    for line in lines:
        roll, name, marks_str, total, pct, grade = line.strip().split("|")
        print(
            f"Roll No: {roll} | Name: {name} | Total: {total} | "
            f"Percentage: {pct}% | Grade: {grade}"
        )
    print()


def search_record():
    roll_to_find = input("Enter roll number to search: ").strip()
    if not os.path.exists(RECORDS_FILE):
        print("No records found yet.\n")
        return

    with open(RECORDS_FILE, "r") as f:
        for line in f:
            roll, name, marks_str, total, pct, grade = line.strip().split("|")
            if roll == roll_to_find:
                print(
                    f"\nName: {name}\nRoll No: {roll}\nTotal: {total}\n"
                    f"Percentage: {pct}%\nGrade: {grade}\n"
                )
                return
    print("No record found for that roll number.\n")


def main_menu():
    while True:
        print("===== Student Grade Calculator =====")
        print("1. Add new student record")
        print("2. View all records")
        print("3. Search record by roll number")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            student = get_student_input()
            print("\n" + student.summary())
            save_record(student)
        elif choice == "2":
            view_all_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()
