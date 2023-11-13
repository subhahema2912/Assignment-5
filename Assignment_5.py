# Challenge 1: Square Numbers and Return Their Sum

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

x = float(input("Enter the value for x: "))
y = float(input("Enter the value for y: "))
z = float(input("Enter the value for z: "))

point = Point(x, y, z)

result = point.sqSum()
print("Sum of squares:", result)



# Challenge 2: Implement a Calculator Class
class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 == 0:
            return "Cannot divide by zero"
        return self.num2 / self.num1

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

obj = Calculator(num1, num2)

print("Addition:", obj.add())
print("Subtraction:", obj.subtract())
print("Multiplication:", obj.multiply())
print("Division:", obj.divide())


# Challenge 3: Implement the Complete Student Class

class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

student = Student()

name = input("Enter the name: ")
rollNumber = input("Enter the roll number: ")

student.setName(name)
student.setRollNumber(rollNumber)

print("Name:", student.getName())
print("Roll Number:", student.getRollNumber())



# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

title_account = input("Enter the account title: ")
balance_account = float(input("Enter the account balance: "))
account = Account(title_account, balance_account)

title_savings = input("Enter the savings account title: ")
balance_savings = float(input("Enter the savings account balance: "))
interest_rate_savings = float(input("Enter the savings account interest rate: "))
savings_account = SavingsAccount(title_savings, balance_savings, interest_rate_savings)

print("\nAccount Information:")
print("Title:", account.title)
print("Balance:", account.balance)

print("\nSavings Account Information:")
print("Title:", savings_account.title)
print("Balance:", savings_account.balance)
print("Interest Rate:", savings_account.interestRate)



# Challenge 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100

title = input("Enter the account title: ")
balance = float(input("Enter the account balance: "))
interest_rate = float(input("Enter the interest rate (%): "))

savings_account = SavingsAccount(title, balance, interest_rate)

savings_account.deposit(500)
print("Balance after deposit:", savings_account.getBalance())

savings_account.withdrawal(300)
print("Balance after withdrawal:", savings_account.getBalance())

interest_amount = savings_account.interestAmount()
print("Interest Amount:", interest_amount)





    

