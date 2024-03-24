import math
# Import square_generator.py module
from square_generator import SquareGenerator, checker
#Task1 List Comprehensions
squares = [x**2 for x in range(1, 11)]
print(squares)

#Task2 Functions
def e_squares(start, end):
    squares = [x**2 for x in range(start, end+1)]
    return squares
print(e_squares(1, 10))

#Task3 Classes
class SquareGenerator:
    def e_squares(start, end):
        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

    print(e_squares(1, 10))

#Task4 Libraries
class SquareGenerator:
    def e_squares(start, end):
        squares = [math.sqrt(x) for x in range(start, end + 1)]
        return squares

    print(e_squares(1, 10))

#Task5 Exceptions
class SquareGenerator:
    def e_squares(start, end):
        try:
            if end > start:
                squares = [x ** 2 for x in range(start, end + 1)]
                return squares
            else:
                raise ValueError("Error - there couldn't be  the end of the range is less than the start.")
        except ValueError as ve:
            print(ve)
    print(e_squares(6, 1))

#Task6 Modules
print(checker)
print(SquareGenerator.e_squares(1, 10))