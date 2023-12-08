"""

@Author: Omkar Bhise

@Date: 2023-12-07 03:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-07 03:30:00

@Title :  Using OOPs concept create an ATM

"""


class Parent:

    def __init__(self,fname,age):
        self.fname = fname
        self.age = age

    def display(self):
        print(f"Name is {self.fname} and age is {self.age} ")


class Child(Parent):

    def __init__(self,fname,age,lname):
        super().__init__(fname, age)
        self.lname = lname

    def display(self):
        print(f"Name is {self.fname} {self.lname} and age is {self.age}")


if __name__ == '__main__':
    ob = Child("omkar",22,"Bhise")
    ob.display()