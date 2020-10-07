from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Jay Davis: Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def greet_user(self):
        self.root.ids.name_label.text = "Hello " + self.root.ids.input_name.text

    def clear_everything(self):
        self.root.ids.input_name.text = ""
        self.root.ids.name_label.text = ""


BoxLayoutDemo().run()
