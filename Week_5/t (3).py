# A prime number is a number that is greater than 1 and has only two factors which are 1 and itself.
# The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.
# Given a number N. Determine whether N is prime or not.
# Note: Solve this problem using function.
# Input First line will contain a number T (1≤T≤103) number of test cases.
# Next T lines will contain a number N (1≤N≤109).
# Output Print "YES" if the Nth number is prime otherwise, print "NO".
# Example
# Input
# 3
# 2
# 4
# 8
# Output
# YES
# NO
# NO

def prim_check(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                return "--> NO"
        else:
            return "--> YES"
    else:
        return "--> YES"

num = map(int,input("Enter some number: ").split())

for n in num:
    print(n, prim_check(n))