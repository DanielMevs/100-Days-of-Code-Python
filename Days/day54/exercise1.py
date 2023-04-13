def decorator_timer(some_function):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = some_function(*args, **kwargs)
        end = time()-t1
        return result, end
    return wrapper


@decorator_timer
def my_pow(a, b):
    res = a ** b
    return res
    # or just return a ** b, it doesn't really matter

result, exec_time = my_pow(99999 , 99999)
print(exec_time) 
# print(result) 