"""CP1404 Practical - Guitar class"""
name_list = []
year_list = []
cost_list = []
vintage_list = []
condition = True

class Guitar:
    def __init__(self):
        self.guitar_name = input("Name: ")
        name_list.append(self.guitar_name)

    def get_condition(self):
        if self.guitar_name == "":
            condition = False
        else:
            condition = True
        return condition

    def get_other_details(self):
        self.year = int(input("Year: "))
        year_list.append(self.year)
        self.cost = float(input("Cost: $"))
        cost_list.append(self.cost)
        self.age = 2020 - self.year
        if self.age >= 50:
            self.vintage = True
            vintage_list.append(True)
        else:
            self.vintage = False
            vintage_list.append(False)
        print("{} ({}) : ${:,.2f} added.\n".format(self.guitar_name, self.year, self.cost))

    def print_details(self):
        print("These are my guitars:")
        for x in range(len(name_list) - 1):
            if vintage_list[x] == True:
                print("Guitar {}: {} ({}), worth ${:,.2f} (vintage)".format(x + 1, name_list[x], year_list[x], cost_list[x]))
            else:
                print("Guitar {}: {} ({}), worth ${:,.2f}".format(x + 1, name_list[x], year_list[x], cost_list[x]))

