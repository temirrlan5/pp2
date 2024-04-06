#1
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def printString(self):
        print(self.input_string.upper())


#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)

#ex usage
point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()  # Output: (1, 2)
point2.show()  # Output: (4, 6)

point1.move(2, 3)
point1.show()  # Output: (3, 5)

distance = point1.dist(point2)
print(distance)  # Output: 5.0

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


#6
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter function with a lambda expression to filter prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)

