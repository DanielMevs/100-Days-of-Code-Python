import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
for (key, value) in student_dict.items():
    print(value)

student_df = pandas.DataFrame(student_dict)
print(student_df)

for (key, value) in student_df.items():
    print(value)


for (index, row) in student_df.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == 'Angela':
        print(row.score)