# Q6. Write a program that takes a month number (1–12) and prints(use if and match):
#
# "Winter"
# "Spring"
# "Summer"
# "Autumn"

x = int(input("Enter a number:(1-->12) "))

if x == 12 or x == 1 or x == 2:
    print("Winter")
elif x == 3 or x == 4 or x == 5:
    print("Spring")
elif x == 6 or x == 7 or x == 8:
    print("Summer")
elif x == 9 or x == 10 or x == 11:
    print("Autumn")
else:
    print("Invalid")

match x:
    case 12|1|2:
        print("Winter")
    case 3|4|5:
        print("Spring")
    case 6|7|8:
        print("Summer")
    case 9|10|11:
        print("Autumn")
    case _:
        print("Invalid")
