# Given 3 lines of input described as follow:
# First line contains a symbol S . Second line contains a number N . Third line contains N numbers. For each number Xi in the N numbers
# print a new line that contains the symbol S repeated Xi time.
# Input The first line contains a symbol S can be (+,−,∗,/) .
# The second line an number N (1≤N≤50) .
# The third line contains N numbers (1≤Xi≤100)
# Input
# +
# 5
# 5 2 4 3 7
# Output:
# +++++
# ++
# ++++
# +++
# +++++++

s = input("Enter the symbl you want to print(+,−,∗,/): ")
n = int(input("Enter the number of lines: "))
l = list(map(int, input("Enter the list numbers: ").split()))
index = l[0]

# for i in range(n):
#     for j in l:
#         if j == index:
#             print(s*index , end="\n")
#
#         else:
#             break
#         index += 1

for i in l:
    print(i*s,end="\n")