"""
Student Grades

Create a dictionary where the keys are student names and the values are their grades. 
Allow the user to:
- Add a new student and grade.
- Update an existing student's grade.
- Print all student grades.

Used dictionary and basic operations. Using if else:
"""

def display_menu():
    """
    Function to display the menu options
    """
    print("\n--- Student Grades Menu ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    print("---------------------------")

def add_student(grades_dict):
    """
    Function to add a new student and grade
    """
    name = input("Enter student name: ").strip()
    if name in grades_dict:
        print(f"Student {name} already exists with grade {grades_dict[name]}. Use update option instead.")
    else:
        try:
            grade = float(input("Enter grade: "))
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
            else:
                grades_dict[name] = grade
                print(f"Added {name} with grade {grade}.")
        except ValueError:
            print("Please enter a valid number for the grade.")

def update_grade(grades_dict):
    """
    Function to update an existing student's grade
    """
    if not grades_dict:
        print("No students in the record.")
        return
    
    name = input("Enter student name to update: ").strip()
    if name in grades_dict:
        try:
            new_grade = float(input(f"Enter new grade for {name} (current: {grades_dict[name]}): "))
            if new_grade < 0 or new_grade > 100:
                print("Please enter a grade between 0 and 100.")
            else:
                grades_dict[name] = new_grade
                print(f"Updated {name}'s grade to {new_grade}.")
        except ValueError:
            print("Please enter a valid number for the grade.")
    else:
        print(f"Student {name} not found in records.")

def print_all_grades(grades_dict):
    """
    Function to print all student grades
    """
    if not grades_dict:
        print("No students in the record.")
        return
    
    print("\n--- All Student Grades ---")
    for name, grade in grades_dict.items():
        print(f"{name}: {grade}")
    print("--------------------------")

def main():
    """
    Main function to run the student grades program
    """
    # Initialize dictionary to store student names and grades
    student_grades = {}
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                add_student(student_grades)
            elif choice == 2:
                update_grade(student_grades)
            elif choice == 3:
                print_all_grades(student_grades)
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()