# Task 5: Grade Evaluation
# Write a program that:
#
# Asks the user to enter their score.
#
# Prints:
#
# "Excellent" if the score is 90 or above.
#
# "Very Good" if the score is between 75 and 89.
#
# "Good" if the score is between 60 and 74.
#
# "Fail" if the score is less than 60.

m = int(input("Enter your score: "))

if m >= 90:
    print("Excellent")
elif m >= 75 and m <= 89:
    print("Very Good")
elif m >= 60 and m <= 74:
    print("Good")
elif m <= 60:
    print("Fail")

match m:
    case d if m >= 90:
        print("Excellent")
    case v if m >= 75 and m <= 89:
        print("Very Good")
    case b if m >= 60 and m <= 74:
        print("Good")
    case e if m >= 60:
        print("Fail")
