import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elenor', 'Rodger', 'Freddie']

student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student:student_score for student, student_score in student_scores.items() if student_score > 70}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}
print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 35 for day, temp in weather_c.items()}
print(weather_f)