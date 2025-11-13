"""
CP1404/CP5632 Practical
Kivy GUI program to Convert Miles to Kilometres
ManiShankar
Started 13/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934

class MilesToKmConverterApp(App):
    """Miles to Kilometres Converter"""
    output_km = StringProperty('Result appears here')

    def build(self):
        Window.size = (400, 300)
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file('convert_miles_km.kv')

    def convert_miles_to_km(self, text):
        """Convert miles to kilometres and update label"""
        try:
            miles = float(text)
        except ValueError:
            miles = 0
        km = miles * FACTOR_MILES_TO_KM
        self.output_km = f"{km:.2f}"

    def handle_increment(self, change):
        """Increment or decrement input"""
        try:
            result = float(self.root.ids.input_number.text)
        except ValueError:
            result = 0
        result += change
        self.root.ids.input_number.text = str(result)
        self.convert_miles_to_km(str(result))

MilesToKmConverterApp().run()