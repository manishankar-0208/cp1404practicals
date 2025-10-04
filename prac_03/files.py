"""
CP1404/CP5632 Practical
- read() -Reads the entire file content as one big string.
- readline() -Reads just one line from the file each time when it’s called.
- readlines() -Reads all lines at once and returns a list of strings, one for each line.
- for line in file -Reads one line at a time in a loop in a sequence
"""

# 1.
out_file = open("name.txt", "w")
name = input("Enter your name: ")
# print(name, file=out_file)
out_file.write(name)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)