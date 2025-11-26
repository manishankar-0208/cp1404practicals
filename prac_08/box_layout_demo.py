from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy app using BoxLayout with buttons, text input, and a label."""
    def build(self):
        """Load and return the KV layout."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display a greeting message with the entered name."""
        print("greet")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear the text input and output label."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


BoxLayoutDemo().run()
