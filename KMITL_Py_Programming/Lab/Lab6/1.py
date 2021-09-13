def compute_grade(score):
    if 0 <= score < 50:
        return "F"
    elif 50 <= score < 60:
        return "D"
    elif 60 <= score < 70:
        return "C"
    elif 70 <= score < 80:
        return "B"
    elif 80 <= score < 100:
        return "A"

grade = float(input("Grade: "))
print(f"Your grade is {compute_grade(grade)}.")