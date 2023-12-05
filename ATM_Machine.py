"""

@Author: Omkar Bhise

@Date: 2023-12-05 10:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-05 1:00:00

@Title :  Using OOPs concept create an ATM

"""


class Atm:

    # Constructor
    def __init__(self):

        self.pin = ""
        self.balance = 0

        # self.menu()

    def menu(self):
        """
           Description:
               it implements the menu bar of Atm

           Parameter: self

           Return: None

        """
        while True:
            user_input = int(input("""
                                Hello, How would you like to Proceed?
                                1. Enter 1 to create pin
                                2. Enter 2 to deposit
                                3. Enter 3 to withdraw
                                4. Enter 4 to check balance
                                5. Enter 5 to exist

                    """))
            if user_input == 1:
                self.create_pin()
            elif user_input == 2:
                self.deposit()
            elif user_input == 3:
                self.withdraw()
            elif user_input == 4:
                self.check_balance()
            else:
                print("Thanks for using ATM ")
                break

    def create_pin(self):
        """
           Description:
               in this function we set the pin of object or User

           Parameter: self

           Return: None

        """
        self.pin = input("Enter the pin ")
        print("Pin set Successfully")

    def deposit(self):
        """
           Description:
               in this function we deposit the user amount if user is valid

           Parameter: self

           Return: None

        """
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount "))
            self.balance += amount
            print("Amount deposited Successfully")
        else:
            print("Invalid Pin")

    def withdraw(self):
        """
           Description:
               in this function we perform the withdrawal of user amount

           Parameter: self

           Return: None

        """
        temp = input("Enter the pin ")
        if temp == self.pin:
            amount = int(input("Enter the amount "))
            if amount > self.balance:
                print("Insufficient Balance ")
            else:
                self.balance -= amount

    def check_balance(self):
        """
               Description:
                   in the function we perform the check user balance

               Parameter: None

               Return: None

        """
        temp = input("Enter your pin")
        if temp == self.balance:
            print(f"Your account Balance is : {self.balance}")
        else:
            print("Invalid Pin")


if __name__ == '__main__':
    sbi = Atm()
    sbi.menu()