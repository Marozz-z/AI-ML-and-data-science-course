# Given a number N. Print a pyramid that has N rows.
#
# For more clarification see the example below.
#
# Input
#
# Only one line containing a number N (1≤N≤99).
#
# Output
#
# Print the answer according to the required above.
#
# Note Don't print any extra spaces after symbol "*".
#
# Input
#
# 4
#
# Output
#
#    *
#   ***
#  *****
# *******

size = int(input("Enter the size of the triangle: "))
for i in range(size):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))
