"""
CP1404/CP5632 Practical
Prompt the user for a Wikipedia page title and print details.
Repeats until the user enters a blank title.
"""
import wikipedia

def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(f"Title: {page.title}")
            print(f"URL: {page.url}")
            print(f"Summary:\n{page.summary}")
            print()
        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        except wikipedia.DisambiguationError as sub:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(sub.options)
        title = input("Enter page title: ").strip()
    print("Thank you")
main()