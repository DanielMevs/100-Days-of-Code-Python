student_grades = {}

student_scores = {

    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,

}


for student in student_scores:
    # print(student)
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Exceeds Expectations"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# - Don't change the code below
print(student_grades)
