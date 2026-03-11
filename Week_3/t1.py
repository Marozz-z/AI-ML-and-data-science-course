# Task 1: Compare Two Numbers:
# Take two numbers as input from the user.
#
# Use an if condition to print the larger number.
#
# If the numbers are equal, print "Both are equal".
#
# Example:
#
# Input: 10, 20
#
# Output: 20 is greater


m=int(input("Enter a number: "))
d=int(input("Enter a number: "))

if m>d:
    print(m," is greater than ",d)
elif m<d:
    print(d," is greater than ",m)
else:
    print(f"Both are equal")

match m,d:
    case b if m > d:
        print(m," is greater than ",d)
    case d if m < d:
        print(d," is greater than ",m)
    case _:
        print("Both are equal")