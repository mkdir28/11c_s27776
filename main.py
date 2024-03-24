#Task1 List Comprehensions
squares = [x**2 for x in range(1, 11)]
print(squares)

#Task2 Functions
def e_squares(start, end):
    squares = [x**2 for x in range(start, end+1)]
    return squares
print(e_squares(1, 10))