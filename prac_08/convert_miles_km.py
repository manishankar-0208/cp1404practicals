"""
CP1404/CP5632 Practical
Kivy GUI program to Convert Miles to Kilometres
ManiShankar
Started 13/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

FACTOR_MILES_TO_KM = 1.60934

class MilesToKmConverterApp(App):
    """Miles to Kilometres Converter"""

    def build(self):
        Window.size = (400, 300)
        self.title = "Convert Miles to Kilometres"
        self.output_km = "Result appears here"
        return Builder.load_file('convert_miles_km.kv')

    def convert_miles_to_km(self, text):
        """Convert miles to kilometres and update label"""
        try:
            miles = float(text)
            km = miles * FACTOR_MILES_TO_KM
            self.output_km = f"{km:.2f}"
            self.root.ids.output_label.text = self.output_km
        except ValueError:
            self.output_km = "Invalid input!"
            self.root.ids.output_label.text = self.output_km

    def handle_increment(self, change):
        """Increment or decrement input"""
        try:
            value = float(self.root.ids.input_number.text) + change
            self.root.ids.input_number.text = str(value)
            self.update_result(str(value))
        except ValueError:
            self.root.ids.input_number.text = '0'

    def update_result(self, text):
        """Update km result automatically"""
        print("update")
        self.convert_miles_to_km(text)

MilesToKmConverterApp().run()