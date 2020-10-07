from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        Window.size = (400, 200)
        self.title = "Jay Davis: Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def square_number(self, value):
        """Calculates the inputted number squared"""
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
