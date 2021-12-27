"""
ASSUMPTIONS OF THE PROGRAM:

Counting and displaying the Fibonacci sequence

"""


def fibonacci(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    elif value > 1:
        sequence_fib = [0, 1]
        for i in range(2, value+1):
            result = sequence_fib[i-2] + sequence_fib[i-1]
            sequence_fib.append(result)
        return sequence_fib


print("Fibonacci sequence")
user_number = int(input("Enter any integer: "))
print(f"Fibonacci for number {user_number} this {fibonacci(user_number)[-1]}")
print(f"The whole fibonacci sequence for a number {user_number} "
      f"looks like this: {fibonacci(user_number)}")