# Write a function called fibonacci(n) that:
# Takes an integer N (1 ≤ N ≤ 45) as a parameter.
# Returns a list containing the first N numbers of the Fibonacci sequence.
# Use the following definition:
# fib(1) = 0
# fib(2) = 1
# fib(n) = fib(n - 1) + fib(n - 2)
# After defining the function, read an integer N from the user and print the returned Fibonacci sequence numbers separated by spaces.
# 🔹 Example
# Input
# 7
# Output
# 0 1 1 2 3 5 8

def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

n = int(input("Enter the number of fibonacci numbers: "))
f = fibonacci(n)
print(f)
