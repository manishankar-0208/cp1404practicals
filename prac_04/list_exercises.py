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