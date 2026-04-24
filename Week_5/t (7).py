# Write a function that takes an integer number as input and returns a list containing each digit of the number separately.

def return_list(num):
    return [int(list1) for list1 in str(abs(num))]

num = int(input("Enter the first number: "))
print(return_list(num))
