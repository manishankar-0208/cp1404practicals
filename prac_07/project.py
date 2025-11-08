"""
CP1404/CP5632 Practical - Project class.
Estimate: 10 minutes
Actual: 10 minutes
"""
from datetime import datetime
class Project:
    """Class representing a project with name, start date, priority, cost, and completion %."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Allow sorting by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is 100% complete."""
        return self.completion_percentage >= 100

    def __str__(self):
        """Return formatted string."""
        return (f"{self.name}, start: {self.start_date}, "
                f"priority {self.priority}, estimated: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")
