"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes_list over a given number of months."""
    incomes_list = []
    number_of_months = int(input("How many months? "))
    return number_of_months

def income_each_month():
    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes_list.append(income)
    return incomes_list

def print_report():
    print(number_of_months, incomes_list)
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes_list[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

number_of_months = 0
incomes_list = []
income = 0
total = 0

number_of_months = main()
incomes_list = income_each_month()
print_report()
