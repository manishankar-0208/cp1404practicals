"""
CP1404/CP5632 - Practical
Get a password with minimum length and display asterisks
"""

MINIMUM_LENGTH = 8

def main():
    """Get a valid password and print asterisks"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)

def get_password(length):
    """Get a password of minimum length required."""
    password = input("Enter your password: ")
    while len(password) < length:
        print("Password must be 8 characters long or more")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    """Print the asterisks of a given password."""
    print('*' * len(password))

main()