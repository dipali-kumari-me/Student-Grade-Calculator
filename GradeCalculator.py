# Student Grade Calculator
# Takes marks of 5 subjects and calculates Total, Percentage and Grade

def grade_calculator():
    name = input("Enter Student Name: ")
    marks = []
    total = 0
    
    print("Enter marks of 5 subjects out of 100:")
    for i in range(5):
        m = float(input(f"Subject {i+1}: "))
        marks.append(m)
        total += m
    
    percentage = total / 5
    
    print("\n===== RESULT =====")
    print(f"Name: {name}")
    print(f"Total Marks: {total}/500")
    print(f"Percentage: {percentage}%")
    
    # Grading
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F - Fail"
    
   
    print(f"Grade: {grade}")


grade_calculator()


