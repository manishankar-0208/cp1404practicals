"""
CP1404/CP5632 Practical
List exercises
"""
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first Number is {numbers[0]}")
print(f"The last Number is {numbers[-1]}")
print(f"The smallest of the numbers is {min(numbers)}")
print(f"The largest of the numbers is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")


# 2. Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")