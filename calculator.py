def divide(a, b):
    # Check if the divisor is zero and raise a ZeroDivisionError if it is.
    if b == 0:
        raise ZeroDivisionError('Division by zero is not allowed.')
    return a / b

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_max(numbers):
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def get_user_by_id(user_id):
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users[user_id]