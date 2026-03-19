#Q7. Take a character from the user(use if and match). Check if it is a vowel (a, e, i, o, u) or not.

x = input("Enter a letter: ")
v = ["a","e","i","o","u"]
x.lower()

if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
    print("Vowel")
else:
    print("Not a vowel")


match x:
    case "a"|"e"|"i"|"o"|"u":
        print("Vowel")
    case _:
        print("Not a vowel")
