student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
runningSum = 0
numOfHeights = 0
for num in student_heights:
	runningSum += num
	numOfHeights += 1
averageHeight = runningSum / numOfHeights