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


print(ferrari.name, ferrari.engine, ferrari.wheels, ferrari.doors)
print(toyotatazz.name, toyotatazz.engine, toyotatazz.wheels, toyotatazz.doors)
print(bajajlol.name, bajajlol.engine, bajajlol.wheels, bajajlol.doors)
print(ferrari.horn())
print(toyotatazz.horn())

# Bank Account
# 1. accno
# 2. name
# 3. balance

# Task 1
class Bank():
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name 
        self.balance = balance
    # Task 2
    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"
    # Task 3
    def withdraw(self, withdrawal):
        if (withdrawal > self.balance):
            return f"Insufficient funds (R{self.balance:,}) to make this withdrawal (R{withdrawal:,})"
        else:
            self.balance -= withdrawal
            return f"Success. Your balance is: R{self.balance:,}"
    # Task 4
    def deposit(self, depositamount):
        self.balance += depositamount
        return f"Success. Your balance is: R{self.balance:,}"
         

# create 3 accounts 
gemma = Bank(123, "Gemma Porrill", 15_000)
dhara = Bank(124, "Dhara Kara", 50_001)
caleb = Bank(125, "Caleb Potts", 100_000)

print(gemma.balance, dhara.balance, caleb.balance)
# Task 2
print(gemma.display_balance())
# Task 3
# caleb.display_balance()
print(caleb.withdraw(2000))
print(caleb.display_balance())
print(caleb.withdraw(99000))
print(caleb.display_balance())
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


