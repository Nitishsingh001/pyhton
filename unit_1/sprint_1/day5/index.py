# 📌 Day 5: File Handling & Exception Handling
# Topics:

# Reading/writing files (open(), read(), write())

# with statement (context manager)

# Exception handling (try, except, finally)

# Raising exceptions (raise)


try:
    name = input("Enter your name: ")
    if name == "":
        raise ValueError("❌ Name cannot be empty.")
    print("Hello,", name)
except ValueError as e:
    print("Error:", e)


class MyError(Exception):
    pass

raise MyError("🚫 This is a custom error.")


def check_number(num):
    if num < 1 or num > 10:
        raise ValueError("Number must be between 1 and 10.")
    return f"{num} is valid."

try:
    n = int(input("Enter a number between 1 and 10: "))
    print(check_number(n))
except ValueError as e:
    print("Error:", e)


# Sample structure
try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Enter valid numbers only!")
finally:
    print("End of operation.")
