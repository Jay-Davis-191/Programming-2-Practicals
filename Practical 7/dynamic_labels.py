from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Adam", "Bryan", "Catherine", "David", "Earl", "Fred"}

    def build(self):
        self.title = "Jay Davis: Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_phone:
            temp_button = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_button)

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


DynamicWidgetsApp().run()
