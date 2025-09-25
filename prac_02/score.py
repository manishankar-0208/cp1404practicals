import random
"""
CP1404/CP5632 - Practical
Program to determine score status
"""

def  main():
    """Program to determine score status"""
    score = float(input("Enter score: "))
    print(determine_status(score))

    random_score =  random.randint(1,100)
    print(determine_status(random_score))

def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()