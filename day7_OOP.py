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


# Encapsulation = methods and variables of class all in one place
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

print(gemma.display_balance())
print(dhara.display_balance())
print(caleb.display_balance())
