# Write a Python function is_divisible(num1, num2) that takes two numbers as input and returns True
# if the first number is divisible by the second number, and False otherwise.

def is_divisible(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
x = is_divisible(num1, num2)
print(x)
