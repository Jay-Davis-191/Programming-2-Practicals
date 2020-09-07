colour_list = {"black": "#000000", "coral": "#ff7150", "cornflowerblue": "#6495ed", "darkgreen": "#006400", "darkorchid": "#9932cc", "firebrick": "#b22222", "ghostwhite": "#f8f8ff", "lightblue": "#add8e6", "limegreen": "#32cd32", "magenta": "#ff00ff"}
print(colour_list)
choice = input("Pick a colour from the list: ")
while choice != "":
    if choice in colour_list:
        print("{} is {}.\n".format(choice, colour_list[choice]))
    else:
        print("Invalid input. Please try again\n")
    choice = input("Pick a colour from the list: ")
