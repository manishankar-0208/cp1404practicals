"""
CP1404/CP5632 - Practical
Program to determine score status
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Main function for the score menu program."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell! Thank you.")

def get_valid_score():
    """Get valid score."""
    score = int(input("Enter your Score: "))
    while score < 0 or score > 100:
        print("Invalid Score!")
        score = int(input("Enter your Score: "))
    return score

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

def print_asterisks(score):
    """Print the asterisks of a given score."""
    print('*' * score)

main()