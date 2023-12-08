"""

@Author: Omkar Bhise

@Date: 2023-12-07 10:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-07 1:00:00

@Title :  Using OOPs concept create an ATM

"""
import math


class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        temp_num = self.den * other.num + self.den * other.num
        temp_den = self.den * other.den

        gcd = math.gcd(temp_den,temp_num)
        temp_num //= gcd
        temp_den //= gcd

        return f"{temp_num}/{temp_den}"

    def __sub__(self, other):
        temp_num = self.num * self.den - self.den * other.num
        temp_den = self.den * other.den

        gcd = math.gcd(temp_den, temp_num)
        temp_num //= gcd
        temp_den //= gcd

        return f"{temp_num}/{temp_den}"

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den

        gcd = math.gcd(temp_den, temp_num)
        temp_num //= gcd
        temp_den //= gcd

        return f"{temp_num}/{temp_den}"

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num

        gcd = math.gcd(temp_den, temp_num)
        temp_num //= gcd
        temp_den //= gcd

        return f"{temp_num}/{temp_den}"


if __name__=="__main__":

    a = Fraction(2,3)
    b = Fraction(3,5)
    print(f"a : {a.num}/{a.den} And b : {b.num}/{b.den}")
    print(f"Addition  {a+b}")
    print(f"subtraction {a-b}")
    print(f"Multiplication {a*b}")
    print(f"Division {a/b}")

