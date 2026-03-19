# Q9* Given a list of numbers:
#
# if number is even → add it to even_list
#
# otherwise → add it to odd_list Print both lists at the end.

while 0 == 0:
    x = int(input("Enter a number: "))
    even_list = []
    odd_list = []

    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)

    even_list.sort()
    odd_list.sort()

    print(even_list)
    print(odd_list)