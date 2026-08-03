# Student Grade Calculator
def calculate_grade():
    print("Student Grade Calculator")
    
    name = input("Enter student name: ")
    marks = float(input("Enter marks (out of 100): "))
    
    if marks >= 90:
        grade = 'A+'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    elif marks >= 50:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"\nStudent: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    
    if grade == 'F':
        print("Status: Fail")
    else:
        print("Status: Pass")

calculate_grade()
