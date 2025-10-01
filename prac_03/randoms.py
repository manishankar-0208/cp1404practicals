import random

print(random.randint(5, 20))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))

# What did you see on line 1?
# I would see an integers between 5 and 20, including both 5 and 20.
# What was the smallest number you could have seen, what was the largest?
# smallest number: 5
# Larget number: 20

# What did you see on line 2?
#I would see it was printing 3, 5, 7, or 9 randomly, one at a time, within the range.

# What was the smallest number you could have seen, what was the largest?
# smallest number :3
# Larget number:9
# Could line 2 have produced a 4
# No

# What did you see on line 3?
# I would see a random floating-point number between 2.5 and 5.5
# What was the smallest number you could have seen, what was the largest?
# smallest number: 2.6943742980401937
# Larget number: 5.465359485630468
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

print(random.randint(1, 100))