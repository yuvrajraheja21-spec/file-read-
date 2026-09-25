import builtins
from pathlib import Path

file_path = Path(__file__).resolve().parent / "outcast.txt"

try:
    with file_path.open("r", encoding="utf-8") as file:
        newlist = [line.rstrip("\n") for line in file]
    builtins.print(newlist)
except FileNotFoundError:
    builtins.print(f"File not found: {file_path}")

student_file = Path(__file__).resolve().parent / "students.txt"

while True:
    builtins.print("\nEnter student details:")
    name = input("Student Name: ")
    roll_number = input("Roll Number: ")
    age = input("Age: ")
    class_name = input("Class: ")

    with student_file.open("a", encoding="utf-8") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Roll Number: {roll_number}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Class: {class_name}\n\n")

    builtins.print("Student details saved to students.txt")

    choice = input("Do you want to enter another student? (y/n): ").strip().lower()
    if choice != "y":
        builtins.print("Exiting the program.")
        break
