from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConversionApp(App):
    def build(self):
        self.title = "Jay Davis: Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles(self):
        value = self.validate_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_km.text = str(result)

    def handle_increment(self, change):
        value = self.validate_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.convert_miles()

    def validate_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConversionApp().run()
