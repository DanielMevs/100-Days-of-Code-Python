#calculate the sum of all the even numbers from 1 to 100, including 1 and 100
runningSum = 0
for i in range(1, 101):
	if i % 2 == 0:
		runningSum += i
print(f"The sum of all even numbers from 1 to 100 are {runningSum}")

#alternatively
runningSum = 0
for i in range(2,101, 2):
	runningSum += i

print(f"The sum of all even numbers from 1 to 100 are {runningSum}")