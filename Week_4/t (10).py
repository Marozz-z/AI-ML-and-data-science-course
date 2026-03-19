#Q10. Take a list of words. Count how many words have length > 5.

# x = list(input("Enter a list of words: "))
x = ["Marwan","D","M","Dl"]
counter = 0

for i in x:
    if len(i) > 5:
        counter += 1

print(counter)