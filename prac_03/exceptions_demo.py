"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError happens because the program expects an integer.
If we enter something other than an integer such as a float, a string, or empty input.

2. When will a ZeroDivisionError occur?
# A ZeroDivisionError occurs when we attempt to divide a number by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we can restrict this by using an if condition.
Whenever the user enters 0 as the denominator, we can skip the division.
"""

is_valid_input  = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Denominator cannot be zero. Try again.")
            continue
        fraction = numerator / denominator
        print(f"{fraction:.2f}")
        is_valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")
