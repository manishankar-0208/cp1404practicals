"""
CP1404/CP5632 Practical
Band class
"""
class Band:
    """Band class with list of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a name and list of musicians."""
        musician_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_string})"

    def add(self, musician):
        """Add a Musician object to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make each musician 'play' and return the combined lines joined with newlines."""
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)
