"""
Grade Checker

Take a score as input and print the grade based on the following:
90+ : "A"
80-89 : "B"
70-79 : "C"
60-69 : "D"
Below 60 : "F"

Here we used a basic if else statement to carry out marks and all.
"""

def get_grade(score):
    """
    Function to determine the grade based on the score
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    """
    Main function to get user input and display grade
    """
    try:
        score = float(input("Enter the score: "))
        
        # Check if score is valid (between 0 and 100)
        if score < 0 or score > 100:
            print("Please enter a score between 0 and 100.")
        else:
            grade = get_grade(score)
            print(f"Grade: {grade}")
    except ValueError:
        print("Please enter a valid number for the score.")

if __name__ == "__main__":
    main()