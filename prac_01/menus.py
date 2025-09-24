"""
CP1404/CP5632 - Practical
Menu Program using the standard while loop pattern
Pseudocode:
get user_name
display menu
get user_choice
while user_choice != Q
   if user_choice == H
       display "hello" name
   else if user_choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get user_choice
display finished message
"""

user_name = input("Enter name: ")
MENU ="""(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
user_choice = input(">>> ").upper()
while user_choice != 'Q':
    if user_choice == 'H':
        print("Hello",user_name)
    elif user_choice == 'G':
        print("Goodbye",user_name)
    else:
        print("Invalid choice")
    print(MENU)
    user_choice = input(">>> ").upper()
print("Finished.")