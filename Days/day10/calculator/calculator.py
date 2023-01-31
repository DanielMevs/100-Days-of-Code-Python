from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

print(logo)

def calculator():
    is_interested = 'y'
    num1 = int(input("What's your first number?: "))

    while(is_interested=='y' or is_interested=='Y'):

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What's your second number?: "))


        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}" )

        # operation_symbol = input("Pick an operation: ")
        # num3 = int(input("What's the next number?: "))

        # calculation_function = operations[operation_symbol]

        # second_answer = calculation_function(answer, num3)

        # print(f"{answer} {operation_symbol} {num3} = {second_answer}")

        is_interested = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to exit.: ")

        # - Uncomment below for recursively rerun this function ad absurdem.
        # if is_interested != 'y' or is_interested != 'Y':
        #     calculator()
        num1 = answer




