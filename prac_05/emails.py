"""
CP1404/CP5632 Practical
Email to name dictionary
Estimate: 15 minutes
Actual:   20 minutes
"""
def main():
    """Create dictionary of emails-to-names."""
    email_to_name = {}
    email = input("Email: ").lower()
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ").lower()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()