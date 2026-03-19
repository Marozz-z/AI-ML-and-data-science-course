#Q4. Create a list of numbers and write a program to sort it in ascending order.

x = [2,4,1,6,9,7,0]

for i in range(len(x)):
    for j in range(len(x)):
        if x[i] < x[j]:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp

print(x)