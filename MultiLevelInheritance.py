"""

@Author: Omkar Bhise

@Date: 2023-12-07 04:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-07 04:30:00

@Title :  Using OOPs concept create an ATM

"""


class Phone:
    def __init__(self, phone_name, price, color):
        self.phone_name = phone_name
        self.price = price
        self.color = color

    def display(self):
        """
           Description:
               This function print the all data of Phone class

           Parameter: self

           Return: None

        """
        print(f"My phone name is {self.phone_name} , color is {self.color} and its price is {self.price}")


class SmartPhone(Phone):

    def __init__(self, model, phone_name, color, price):
        super().__init__(phone_name, color, price)
        self.model = model

    def display(self):
        """
           Description:
               This function print the all data of Phone and SmartPhone class

           Parameter: self

           Return: None

        """
        super().display()
        print(f"and Model numebr is {self.model}")


class Redmi(SmartPhone):

    def __init__(self, memory, ram, model, phone_name, color, price):
        super().__init__(model, phone_name, color, price)
        self.ram = ram
        self.memory = memory

    def display(self):
        """
           Description:
               This function print the all data of Phone, SmartPhone Redmi  class

           Parameter: self

           Return: None

        """
        super().display()
        print(f"Internal Memory is {self.memory} and Ram is : {self.ram}")


if __name__ == '__main__':
    p = Phone("Redmi", 15000, "red")
    # p.display()

    c = SmartPhone(12, "redmi", "sky Blue", 15500)
    # c.display()

    r = Redmi(64, 4, 12.2, "Redmi", "white", 11500)
    r.display()
