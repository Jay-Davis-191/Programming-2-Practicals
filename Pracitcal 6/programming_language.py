"""CP1404 Practical - ProgrammingLanguage Class"""

language_list = []

class ProgrammingLanguage():
    def __init__(self, field, typing, reflection, year):
        self.field = field
        language_list.append(field)
        self.typing = typing
        language_list.append(typing)
        self.reflection = reflection
        language_list.append(reflection)
        self.year = year
        language_list.append(year)
        print("{}, {} Typing, Reflection={}, First appeared in {}".format(self.field, self.typing, self.reflection, self.year))

    def determine_dynamic(self):
        if self.typing == "Dynamic":
            print(self.field)
