# Task 6: Number Comparison
# Write a program that:
#
# Asks the user to enter a number.
#
# Prints:
#
# "Zero" if the number is 0.
#
# "Positive" if the number is greater than 0.
#
# "Negative" if the number is less than 0.

m = int(input("Enter a number: "))

if m > 0:
    print("Positive")
elif m < 0:
    print("Nigative")
else:
    print("It's a Zero")


match m:
    case d if m > 0:
        print("Positive")
    case v if m < 0:
        print("Nigative")
    case _:
        print("It's a Zero")