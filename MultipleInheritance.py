"""

@Author: Omkar Bhise

@Date: 2023-12-07 04:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-07 04:30:00

@Title :  Using OOPs concept create an ATM

"""


class Milk:
    def __init__(self):
        self.milk = "Milk "

    def display_milk(self):
        print("Milk is white")


class Suger:
    def __init__(self):
        self.suger = "Suger "

    def display_suger(self):
        print("Suger is sweet")


class Tea(Suger, Milk):
    def __init__(self):
        Milk.__init__(self)
        Suger.__init__(self)
        self.tea_powder = "Tea Powder"

    def make_a_tea(self):
        print(f"By using {self.milk} , {self.suger} and Tea_powder we make a Tea")


class Coffee(Suger, Milk):
    def __init__(self):
        self.coffee_powder = "Coffee Powder"

    # def make_a_coffee(self):
    #     print(f"Using {self.milk}, {self.suger} and {self.coffee_powder} we make a Coffee ")


class BlackTea(Tea):

    def make_a_black_tea(self):
        print(f"Using {self.suger} and {self.tea_powder} we make a black tea")


if __name__ == '__main__':
    tea = Tea()
    tea.make_a_tea()
    tea.display_milk()
    tea.display_suger()

    # coffee = Coffee()
    # coffee.make_a_coffee()
    # coffee.display_suger()
    # coffee.display_milk()