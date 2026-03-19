#Q3. Create a list of five elements and remove the third element.

x = ["M","D","R","C"]

for i in x:
    if i == x[2]:
        x.remove(x[2])
print(x)