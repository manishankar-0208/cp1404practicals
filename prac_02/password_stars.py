length = 8
password = input("Enter your password: ")
while len(password) < 8:
    print("Password must be 8 characters long or more")
    password = input("Enter your password: ")

print(len(password) * '*')