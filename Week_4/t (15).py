# Given a number N. Print a diamond that has 2N rows.
#
# For more clarification see the example below.
#
# Input Only one line containing number N (1 ≤ N ≤ 99).
#
# Output Print the answer according to the required above.
#
# Example Input
#
# 4
#
# Output
#
#    *
#   ***
#  *****
# *******
# *******
#  *****
#   ***
#    *

size = int(input("Enter the size of triangle: "))
for i in range(size):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))

for i in range(size-2,-1,-1):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))