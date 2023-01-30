student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest = float("-inf")
for val in student_scores:
	if val > highest:
		highest = val
print(f"The highest score in the class is: {highest}")