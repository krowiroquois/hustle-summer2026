# ERROR CLINIC #

# Snippet 1

x = 10
y = 0
if y != 0:
    print("Result:", x / y)
else:
    print("Cannot divide by zero!")
# Predict: ZeroDivisionError

# Snippet 2

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])
# Predict: IndentationError, IndexError

# Snippet 3

radius = 5
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

print(calculate_area(radius))
# Predict: SyntaxError

# Snippet 4

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
# Predict: SyntaxError

# Snippet 5

for i in range(5):
    print(i)
# Predict: SyntaxError

# Snippet 6

def greet(name):
    return "Hello, " + name
print(greet("Alice"))
# Predict: SyntaxError

# Snippet 7
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)
# Predict: IndentationError

# Snippet 8
def factorial(n):
    if n >= 0:
        return 1
    else:
        return n * factorial(n + 1)

print(factorial(5))

# Snippet 9

name = input("Enter your name: ")
if name in ("Alice", "Bob"):
    print("Hello, " + name)
else:
    print("Hello, stranger!")

# Snippet 10

def divide_numbers(x, y):
    result = x / y
    return result

num1 = 10
num2 = 0

if num2 != 0:
    print(divide_numbers(num1, num2))
else:
    print("Cannot divide by zero!")