"""
CP1404/CP5632 Practical - Project Management Program client code
Estimate: 30 minutes
Actual:   35 minutes
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
            filter_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
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

def filter_by_date(projects):
    """Ask the user for a date and display projects starting on or after that date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if datetime.strptime(project.start_date, "%d/%m/%Y").date() >= filter_date]
    # Temporarily override __lt__ to sort by start_date
    original_lt = Project.__lt__
    Project.__lt__ = Project.compare_by_start_date
    filtered_projects.sort()
    Project.__lt__ = original_lt  # restore priority sorting
    for project in filtered_projects:
        print(project)

if __name__ == "__main__":
    main()
