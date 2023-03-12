numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)


name = "Daniel"
new_list = [letter for letter in name]
print(new_list)

range_list = [num * 2 for num in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]

short_names = [name for name in names if len(name) < 5]

print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)


def square_list(arr):
    return [num**2 for num in arr]



from functools import reduce

MAX_RANGE = 11
other_numbers = [num for num in range(1, MAX_RANGE)]
squared_nums = square_list(other_numbers)
print(squared_nums)

'''Lambda is a short-hand way to denote a function
Reduce is a function whose first argument is a function, the second argument is 
the range which denotes who many times to iterate over and perform the given function.
The third argument is the initial list for which the items being iterated over can be
fed to the given function.'''
fib_func = lambda n: reduce(lambda x, _: x+[x[-1] + x[-2]], range(n - 2), [0, 1])
fibbed_numbers = fib_func(MAX_RANGE)
new_squared_nums = square_list(fibbed_numbers)
print(new_squared_nums)

def only_evens(arr):
    return [num for num in arr if num % 2 == 0 and num != 0]

even_nums = only_evens(fibbed_numbers)

print(even_nums)


# - Fun with lambda

squared = lambda n: list((x**2) for x in n)
# print(list(squared(fibbed_numbers)))
print(squared(fibbed_numbers))

even = lambda n: list(x for x in n if x % 2 == 0)
print(even(fibbed_numbers))