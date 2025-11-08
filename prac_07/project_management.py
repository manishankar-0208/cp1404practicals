"""
CP1404/CP5632 Practical - Project Management Program client code
Estimate: 20 minutes
Actual: 25 minutes
"""

from datetime import datetime
from prac_07.project import Project

DEFAULT_FILENAME = "projects.txt"

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""
def main():
    """Project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    choice = input(f"{MENU}\n>>> ").strip().upper()
    while choice != "X":
        if choice == "L":
            filename = input("Filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        choice = input(f"{MENU}\n>>> ").strip().upper()

    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? (Y/N)").strip()
    if save_choice == 'Y':
        save_projects(DEFAULT_FILENAME, projects)

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = parts[2]
            cost = parts[3]
            completion_percentage = parts[4]
            project = Project(name, start_date, int(priority), float(cost), int(completion_percentage))
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t"
                  f"{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    completed_projects = sorted([project for project in projects if project.is_complete()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

if __name__ == "__main__":
    main()
