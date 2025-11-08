"""
CP1404/CP5632 Practical - Project Management Program client code
Estimate: 45 minutes
Actual:   45 minutes
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

def add_new_project(projects):
    """Ask user for input and add a new project."""
    print("Let's add a new project")
    name = get_valid_input("Name: ", str)
    start_date = get_valid_input("Start date (dd/mm/yyyy): ", date_format="%d/%m/%Y")
    priority = get_valid_input("Priority: ", int, min_value=1)
    cost = get_valid_input("Cost estimate: $", float, min_value=0)
    percent = get_valid_input("Percent complete: ", int, min_value=0, max_value=100)
    project = Project(name, start_date, priority, cost, percent)
    projects.append(project)
    print(f"{project.name} added successfully!\n")

def get_valid_input(prompt, input_type=str, min_value=None, max_value=None, date_format=None):
    """Function to get valid input from user."""
    is_valid_input = False
    while not is_valid_input:
        user_input = input(prompt).strip()
        try:
            if date_format:
                value = datetime.strptime(user_input, date_format).strftime(date_format)
                is_valid_input = True
                return value
            value = input_type(user_input)
            if min_value is not None and value < min_value:
                print(f"Value must be >= {min_value}")
            elif max_value is not None and value > max_value:
                print(f"Value must be <= {max_value}")
            else:
                is_valid_input = True
                return value
        except ValueError:
            type_name = "date" if date_format else input_type.__name__
            print(f"Invalid {type_name}, please try again.")

def update_project(projects):
    """Update completion percentage and/or priority for an existing project."""
    for i, project in enumerate(projects):
        print(i, project)

    choice = get_valid_input("Project choice: ", int, min_value=0, max_value=len(projects) - 1)
    project = projects[choice]
    print(project)

    new_percentage = get_valid_input("New percentage: ", int, min_value=0, max_value=100)
    project.completion_percentage = new_percentage

    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)

if __name__ == "__main__":
    main()
