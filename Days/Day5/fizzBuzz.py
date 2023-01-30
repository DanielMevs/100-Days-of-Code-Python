length = int(input("How long is the fizz buzz? "))
arr = []
for i in range(0, length + 1):
	if i == 0:
		continue
	if i % 3 == 0 and i % 5 == 0:
		arr.append("fizzbuzz")
	elif i % 3 == 0:
		arr.append("fizz")
	elif i % 5 == 0:
		arr.append("buzz") 
	else:
		arr.append(i)

for ele in arr:
	print(ele)
