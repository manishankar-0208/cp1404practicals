"""
CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class.
Estimate: 15 minutes
Actual:   20 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    """Demo test code to show how to use the ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    # print(ruby)
    # print(visual_basic)

    languages = [python, ruby, visual_basic]
    # print(languages)
    print(f"The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()