from datetime import datetime

# Object Oriented Programming


# Car
# 1. Engine
# 2. wheels
# 3. doors

# Ferrari
# 1. engine - v8
# 2. wheels - 4
# 3. doors - 2

# Toyota Tazz
# 1. engine - v4
# 2. wheels - 4
# 3. doors - 4

# class Car:
#     # constructor init function so you don't have to repeat instance (object) creation all the time
#     pass

# create instance of class (object)
# ferrari = Car()
# ferrari.name = "Ferrari"
# ferrari.engine = "v8"
# ferrari.wheels = 4
# ferrari.doors = 2
# And again for Toyota Tazz
# toyotatazz = Car()
# toyotatazz.name = "Toyota Tazz"
# toyotatazz.engine = "v4"
# toyotatazz.wheels = 4
# toyotatazz.doors = 4

# print(ferrari.name, ferrari.engine, ferrari.wheels, ferrari.doors)


# Car -> Blueprint | Class blueprint object
class Car:
    # constructor method (dunder method)
    def __init__(self, name, engine, wheels, doors):
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors

    # create method for blueprint now all objects have access to this method
    def horn(self):
        return "Vroom Vroom"


# create instance/object (supply values to blueprint)
ferrari = Car("Ferrari", "V8", 4, 2)
toyotatazz = Car("Toyota Tazz", "V4", 4, 4)
bajajlol = Car("Bajaj", "V-2", 4, 2)


# print(ferrari.name, ferrari.engine, ferrari.wheels, ferrari.doors)
# print(toyotatazz.name, toyotatazz.engine, toyotatazz.wheels, toyotatazz.doors)
# print(bajajlol.name, bajajlol.engine, bajajlol.wheels, bajajlol.doors)
# print(ferrari.horn())
# print(toyotatazz.horn())

# Bank Account
# 1. accno
# 2. name
# 3. balance

# Black formatter -> Formats according to PEP = Python Enhancement Proposals


# Task 1
class Bank1:
    def __init__(
        self, accno, name, balance, numtransactions=None, transactions=None
    ):  # what def value to give to transactions? None doesn't work?
        self.accno = accno
        self.name = name
        self.balance = balance
        if numtransactions is None:
            self.numtransactions = 0
        else:
            self.numtransactions = numtransactions
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions

    # Task 2
    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"

    # Task 3
    def withdraw(self, withdrawal):
        if withdrawal > self.balance:
            return f"Insufficient funds (R{self.balance:,}) to make this withdrawal (R{withdrawal:,})"
        else:
            self.balance -= withdrawal
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "withdraw", withdrawal)
            return f"Success. {self.display_balance()}"

    # Task 4
    def deposit(self, depositamount):
        if depositamount < 0:
            return f"Invalid deposit amount of R{depositamount:,}"
        else:
            self.balance += depositamount
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "deposit", depositamount)
            return f"Success. {self.display_balance()}"

    # add deposits and withdrawals to the statement as they happen
    # Statement function assignment
    def statement(self, idnum, date, transtype, amount):
        self.transactions.append(
            {"id": idnum, "Date": date, "Type": transtype, "Amount": amount}
        )
        # f"Hi {self.name}, here is your list of transactions:\n" for nice function later
        return self.transactions


# create 3 accounts
gemma = Bank1(123, "Gemma Porrill", 15_000)
dhara = Bank1(124, "Dhara Kara", 50_001)
caleb = Bank1(125, "Caleb Potts", 100_000)

# print(gemma.balance, dhara.balance, caleb.balance)
# Task 2
print(gemma.display_balance())
# Task 3
# caleb.display_balance()
print(caleb.withdraw(2000))
print(caleb.display_balance())
print(caleb.withdraw(99000))
print(caleb.display_balance())
print(gemma.deposit(-1))
print(gemma.display_balance())
# Task 4
# dhara.deposit(10_000) -> Success. your balance is R60,001
print(dhara.deposit(10_000))
print(dhara.display_balance())


# List of Dicitonaries
# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000
print(gemma.deposit(10_000))
print(caleb.withdraw(1000))
print(dhara.deposit(15000))
print(dhara.transactions)
print(caleb.transactions)
print(gemma.transactions)


# Encapsulation = methods and variables of class all in one place (for objects to be attched to and be able to access)
class Bank2:
    # Class variable | All your instances share this variables
    interest_rate = 0.02

    def __init__(
        self, accno, name, balance, numtransactions=None, transactions=None
    ):  # what def value to give to transactions? None doesn't work?
        self.accno = accno
        self.name = name
        self.balance = balance
        if numtransactions is None:
            self.numtransactions = 0
        else:
            self.numtransactions = numtransactions
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions

    # Task 2
    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"

    # Task 3
    def withdraw(self, withdrawal):
        if withdrawal > self.balance:
            return f"Insufficient funds (R{self.balance:,}) to make this withdrawal (R{withdrawal:,})"
        else:
            self.balance -= withdrawal
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "withdraw", withdrawal)
            return f"Success. {self.display_balance()}"

    # Task 4
    def deposit(self, depositamount):
        if depositamount < 0:
            return f"Invalid deposit amount of R{depositamount:,}"
        else:
            self.balance += depositamount
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "deposit", depositamount)
            return f"Success. {self.display_balance()}"

    # add deposits and withdrawals to the statement as they happen
    # Statement function assignment
    def statement(self, idnum, date, transtype, amount):
        self.transactions.append(
            {"id": idnum, "Date": date, "Type": transtype, "Amount": amount}
        )
        # f"Hi {self.name}, here is your list of transactions:\n" for nice function later
        return self.transactions

    def apply_interest(self):
        # print(Bank2.interest_rate)
        self.balance += self.balance * Bank2.interest_rate
        # return self.balance


# create 3 accounts
gemma = Bank2(123, "Gemma Porrill", 15_000)
dhara = Bank2(124, "Dhara Kara", 50_001)
caleb = Bank2(125, "Caleb Potts", 100_000)

print(gemma.apply_interest())
print(dhara.apply_interest())
print(caleb.apply_interest())

# dhara.balance = 900_000 # can update the balance directly which is wrong!

print(gemma.display_balance())
print(dhara.display_balance())
print(caleb.display_balance())


# Encapsulation | Putting it all together in one container | Give access
class Bank3:
    # Class variable | All your instances share this variable
    interest_rate = 0.02
    totalaccounts = 0

    def __init__(
        self, accno, name, balance, numtransactions=None, transactions=None
    ):  # what def value to give to transactions? None doesn't work?
        self.accno = accno
        self.name = name
        # private variable
        self.__balance = balance
        if numtransactions is None:
            self.numtransactions = 0
        else:
            self.numtransactions = numtransactions
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions
        Bank3.totalaccounts += 1
        print(self.name, Bank3.totalaccounts)

    # class method | cls -> Class
    @classmethod
    def update_total_accounts(cls, numaccounts):
        # Bank3.totalaccounts = numaccounts # when referring to another class use this
        cls.totalccounts = numaccounts  # when referring to same class use this way

    # class method | cls -> Class
    @classmethod
    def update_interest_rate(cls, rate):
        # Bank3.interest_rate = rate  # when referring to another class use this way
        cls.interest_rate = rate  # when referring to same class use this way

    # Task 2
    # instance method | self -> instance/object
    def display_balance(self):
        return f"Your balance is: R{self.__balance:,}"

    # Task 3
    def withdraw(self, withdrawal):
        if withdrawal > self.__balance:
            return f"Insufficient funds (R{self.__balance:,}) to make this withdrawal (R{withdrawal:,})"
        else:
            self.__balance -= withdrawal
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "withdraw", withdrawal)
            return f"Success. {self.display_balance()}"

    # Task 4
    def deposit(self, depositamount):
        if depositamount < 0:
            return f"Invalid deposit amount of R{depositamount:,}"
        else:
            self.__balance += depositamount
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "deposit", depositamount)
            return f"Success. {self.display_balance()}"

    # add deposits and withdrawals to the statement as they happen
    # Statement function assignment
    def statement(self, idnum, date, transtype, amount):
        self.transactions.append(
            {"id": idnum, "Date": date, "Type": transtype, "Amount": amount}
        )
        # f"Hi {self.name}, here is your list of transactions:\n" for nice function later
        return self.transactions

    def apply_interest(self):
        # print(Bank2.interest_rate)
        self.__balance += self.__balance * Bank2.interest_rate
        # return self.balance

    # @classmethod
    # static method -> no cls, self | normal function
    # when not changing anything in the classes
    # You can have it defined outside but people want to keep things in one place/organised
    @staticmethod
    def get_total_no_accounts():
        return f"In total we have {Bank3.totalaccounts} accounts"


# create 4 accounts
gemma = Bank3(123, "Gemma Porrill", 15_000)
dhara = Bank3(124, "Dhara Kara", 50_001)
caleb = Bank3(125, "Caleb Potts", 100_000)
kenny = Bank3(126, "Ken Kenny", 100)

# print(gemma.accno)  # can print this as it's public
# print(gemma.__balance)  # error | cannot access private variables
print(gemma.display_balance())

Bank3.update_interest_rate(0.10)

# Apply interest
kenny.apply_interest()
print(kenny.display_balance())

# Task
print(Bank3.get_total_no_accounts())


# Task
class Circle:
    pi = 3.14159  # class variable

    # constructor function
    def __init__(self, radius):
        self.radius = radius

    @classmethod  # cls -> class
    # "Circle." -> therefore has to be a class method
    def from_diameter(cls, diameter):
        radius = diameter / 2  # get radius
        return cls(radius)  # make and return new circle with it

    # instance method | self -> instance/object
    def calculate_area(self):
        return f"The area of the circle is: {Circle.pi * (self.radius**2)}"

    @staticmethod  # doesn't need anything from instances or cls
    def perimeter(radius):
        return round(2 * Circle.pi * radius, 2)


# Task 1
# static method = plain function inside class
# print perimeter of circle given radius
print(
    f"The perimeter of the circle is: {Circle.perimeter(10)}"
)  # 10 -> radius | 2 * pi * r
print(f"The perimeter of the circle is: {Circle.perimeter(5)}")

# Task 2
# Create circle with radius
circle1 = Circle(2)
print(circle1.calculate_area())
# Create circle with diameter
circle_from_dia = Circle.from_diameter(20)  # 20 = diameter of circle
# have to return new instance above to call this method on circle_from_dia
print(circle_from_dia.calculate_area())


# Inheritance: Animal(Base)
class Animal:
    def __init__(self, name):
        self.name = name

    # methods/attributes
    def speak(self):
        return "Some sound"


# inherits from Animal class
class Dog(Animal):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def run(self):
        return "🐶 wags tail!!"

    # polymorphism | overriding methods
    def speak(self):  # overrides "speak" function
        return "Woof !! 🐕"

    def speed_bonus(self):
        return f"Running at {self.speed * 2}km/h"


toby = Animal("toby")
maxy = Dog("maxy", 20)

print(toby.speak())
print(maxy.speak())
print(maxy.name)
print(maxy.run())
# print(toby.run()) # error, no attribute/method called run
print(maxy.speed_bonus())


class Bank4:
    # Class variable | All your instances share this variable
    interest_rate = 0.02
    totalaccounts = 0

    def __init__(
        self, accno, name, balance, numtransactions=None, transactions=None
    ):  # what def value to give to transactions? None doesn't work?
        self.accno = accno
        self.name = name
        # protected variable - can be accessed by subclasses and printed out but not changed
        self._balance = balance
        # private variable
        # self.__balance = balance
        if numtransactions is None:
            self.numtransactions = 0
        else:
            self.numtransactions = numtransactions
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions
        Bank4.totalaccounts += 1
        print(self.name, Bank4.totalaccounts)

    # class method | cls -> Class
    @classmethod
    def update_total_accounts(cls, numaccounts):
        # Bank4.totalaccounts = numaccounts # when referring to another class use this
        cls.totalccounts = numaccounts  # when referring to same class use this way

    # class method | cls -> Class
    @classmethod
    def update_interest_rate(cls, rate):
        # Bank4.interest_rate = rate  # when referring to another class use this way
        cls.interest_rate = rate  # when referring to same class use this way

    # Task 2
    # instance method | self -> instance/object
    def display_balance(self):
        return f"Your balance is: R{self._balance:,}"

    # Task 3
    def withdraw(self, withdrawal):
        if withdrawal > self._balance:
            return f"Insufficient funds (R{self._balance:,}) to make this withdrawal (R{withdrawal:,})"
        else:
            self._balance -= withdrawal
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "withdraw", withdrawal)
            return f"Success. {self.display_balance()}"

    # Task 4
    def deposit(self, depositamount):
        if depositamount < 0:
            return f"Invalid deposit amount of R{depositamount:,}"
        else:
            self._balance += depositamount
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "deposit", depositamount)
            return f"Success. {self.display_balance()}"

    # add deposits and withdrawals to the statement as they happen
    # Statement function assignment
    def statement(self, idnum, date, transtype, amount):
        self.transactions.append(
            {"id": idnum, "Date": date, "Type": transtype, "Amount": amount}
        )
        # f"Hi {self.name}, here is your list of transactions:\n" for nice function later
        return self.transactions

    def apply_interest(self):
        # print(Bank4.interest_rate)
        # use self.interest_rate!
        self._balance += self._balance * self.interest_rate
        # return self.__balance

    # @classmethod
    # static method -> no cls, self | normal function
    # when not changing anything in the classes.
    # You can have it defined outside but people want to keep things in one place/organised
    @staticmethod
    def get_total_no_accounts():
        return f"In total we have {Bank4.totalaccounts} accounts"

    def get_balance(self):
        return self._balance

    def update_balance(self, amount):
        self._balance += amount


# create 3 accounts
gemma = Bank4(123, "Gemma Porrill", 15_000)
dhara = Bank4(124, "Dhara Kara", 50_001)
caleb = Bank4(125, "Caleb Potts", 100_000)
kenny = Bank4(126, "Ken Kenny", 100)

# Solution 1
# class SavingsAccount(Bank4):
#     interest_rate = 0.05

#     def __init__(self, accno, name, balance):
#         super().__init__(accno, name, balance)

#     def apply_interest(self):
#         self.update_balance(self.get_balance() * SavingsAccount.interest_rate)


# Solution 2
class SavingsAccount(Bank4):
    interest_rate = 0.05
    # can get rid of, don't need to override
    # def __init__(self, accno, name, balance):
    #     super().__init__(accno, name, balance)

    # changed apply_interest in Bank4
    # def apply_interest(self):
    #     self.update_balance(self.get_balance() * SavingsAccount.interest_rate)


# Magic methods __repr__ , __str__ (dunder methods)


class CheckingAccount(Bank4):
    transaction_fee = 1

    def withdraw(self, amount):
        # Can do self.transaction_fee to specify th classes transaction_fee
        return super().withdraw(amount + CheckingAccount.transaction_fee)

    # override str()
    def __str__(self):
        """For human readble output"""
        return (
            f"This account belongs to {self.name} and has balance of R{self._balance:,}"
        )

    def __repr__(self):
        """For DX: String -> Class"""
        return f"CheckngAccount({self.accno}, '{self.name}', {self._balance})"

    # override add
    def __add__(self, other):
        return self._balance + other._balance


# Task 1
# SavingsAccount -  interest_rate = 0.05
gemma = SavingsAccount(123, "Gemma Porrill", 1_000)
gemma.apply_interest()
print(gemma.display_balance())  # 1_050

# Task 2
# CheckingAccount - withdraw  R1
alex = CheckingAccount(126, "Alex Lazarus", 100)
caleb = CheckingAccount(125, "Caleb Potts", 100_000)
print(alex.withdraw(50))  # 49 value
print(alex)
# print(alex.__str__())
# print(str(alex))
# print(alex.__repr__())
print(repr(alex))  # preferred syntax
print(alex + caleb)

# Questions
# Can you please explain the "self" variable with regards to self.transaction_fee and self.interest_rate with that earlier example
# What is point of using

# difference between private and protected


# Assignment
# 1. @property,  @balance.setter = explore these and an example

# 2. Creating you own decorator
# Using function
# Using classes
# example and explanation for each way
# Create error class
