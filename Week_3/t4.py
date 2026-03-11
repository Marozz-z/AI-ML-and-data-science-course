# Task 4: Password Check : Even or Odd
# Write a program that:
#
# Asks the user to enter a number.
#
# If the number is even, print "Even Number".
#
# Otherwise, print "Odd Number".

m = int(input("Enter a number: "))

if m%2==0:
    print(m," is an even number")
else:
    print(m," is an odd number")

match m:
    case d if m%2== 0:
        print(m," is an even number")
    case _:
        print(m," is an odd number")