"""
CP1404/CP5632 Practical
Prompt the user for a Wikipedia page title and print details.
Repeats until the user enters a blank title.
"""
import wikipedia

def main():
    title = input("Enter page title: ").strip()
    while title != "":
        page = wikipedia.page(title, auto_suggest=False)
        print(f"\n{title.capitalize()} Wikipedia Page Details")
        print(f"Title: {page.title}")
        print(f"URL: {page.url}")
        print(f"Summary:\n{page.summary}")
        print()
        title = input("Enter page title: ").strip()
main()
