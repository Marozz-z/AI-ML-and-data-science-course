# Task 2: Vowel or Consonant
# Ask the user to enter a single letter.
#
# Use an if condition to check if it is a vowel (a, e, i, o, u).
#
# Print "Vowel" if it is a vowel, otherwise print "Consonant".
#
# Example:
#
# Input: e
#
# Output: Vowel

m=input("Enter single letter: ")
m.lower()

if m=="a" or m=="e" or m=="i" or m=="o" or m=="u":
    print(m," is a Vowel letter")
else:
    print(m," is a Consonant letter")

match m:
    case "a" | "e" | "i" | "o" | "u":
        print(m," is a Vowel letter")
    case _:
        print(m," is a Consonant letter")