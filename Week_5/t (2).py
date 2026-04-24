# Given an array A of size N . Print the average(mean) of the array numbers.
# Note: Solve this problem using function.
# Input First line will contain a number N (1≤N≤104) length of the array.
# Second line will contain N numbers (1≤Ai≤103) .
# Output Print the average(mean) of the array with 6 digits after the decimal point.
# Examples Input
# 3
# 1.0 2.0 5.0
# Output
# 2.6666667
# Input
# 4
# 1.0 7.0 4.0 9.0
# Output
# 5.2500000

def avg(l):
    total = 0
    for i in l:
        total += i
    return f"{total / len(l):.7f}"

x = int(input("Enter the size of array: "))
l=list(map(float,input("Enter the list elements: ").split()))
print(avg(l))