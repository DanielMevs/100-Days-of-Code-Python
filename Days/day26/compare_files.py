file1, file2 = [], []

with open("file1.txt") as f1:
    for line in f1.readlines():
        file1.append(int(line.strip()))

with open("file2.txt") as f2:
    for line in f2.readlines():
        file2.append(int(line.strip()))


like_numbers = [x for x in file1 if x in file2]


# - Alternatively

with open("file1.txt") as f1:
    file1 = f1.readlines()

with open("file2.txt") as f2:
    file2 = f2.readlines()


like_numbers = [int(x) for x in file1 if x in file2]


# print(file1)
# print(file2)

# like_numbers1 = [x for x in file1 if x in file2]
# like_numbers2 = [x for x in file2 if x in file1]


# print(like_numbers1)
# print(like_numbers2)

# check = all(item in like_numbers1 for item in like_numbers2)
# print(check)
