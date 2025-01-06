# MyMathLibrary.py
from app import add, sub, multiply

class MyMathLibrary:
    def Add(self, a, b):
        return add(float(a), float(b))  # Convert inputs to floats

    def Subtract(self, a, b):
        return sub(float(a), float(b))  # Convert inputs to floats

    def Multiply(self, a, b):
        return multiply(float(a), float(b))  # Convert inputs to floats