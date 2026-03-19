# Given a number N. Print a face down right angled triangle that has N rows.
#
# For more clarification see the example below.
#
# Input =4
#
# Output:
#
# ****
# ***
# **
# *
star = int(input("Enter a number: "))
for i in range(6,0,-1):
  for j in range(i):
       print("*", end="")
  print()