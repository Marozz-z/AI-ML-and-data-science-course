# Given a number N
# . Print a pyramid of height N
# .
#
# Note: Solve this problem using recursion.
#
# Input
# Only one line containing a number N
#  (1≤N≤103)
# .
#
# Output
# Print the pyramid in N
#  lines.
#
# Examples
# Input
# 1
# Output
# *
# Input
# 2
# Output
#  *
# ***
# Input
# 3
# Output
#   *
#  ***
# *****
# Input
# 4
# Output
#    *
#   ***
#  *****
# *******
# Note
# Don't print any extra space after '*'.

size = int(input("Enter the size of the triangle: "))
for i in range(size):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))