# Task 3: Password Check
# Set a fixed password in the program, e.g., "Open123".
#
# Ask the user to enter a password.
#
# Use an if condition to check if it matches the fixed password.
#
# Print "Access Granted" if correct, otherwise "Access Denied".
#
# Example:
#
# Input: Open123
#
# Output: Access Granted

Fpasskey="Open123"

m = input("Enter your Password: ")

if Fpasskey == m:
    print("Access Granted")
else:
    print("Access Denied")


match Fpasskey:
    case d if Fpasskey == m:
        print("Access Granted")
    case _:
        print("Access Denied")