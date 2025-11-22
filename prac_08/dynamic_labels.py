"""
CP1404/CP5632 Practical
Kivy GUI program to dynamically create Labels
ManiShankar
Started 13/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label #used to create text widgets dynamically.


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic Label creation."""
    def __init__(self, **kwargs):
        """Construct the app and store data."""
        super().__init__(**kwargs)
        self.names = ["Smith", "Williams", "Warner", "David", "James"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels Example"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically create Label widgets from the names list."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
DynamicLabelsApp().run()