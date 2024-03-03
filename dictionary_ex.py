books = [
    {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
    {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
    {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
    {"title": "Sapiens", "rating": 4.9, "genre": "History"},
    {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]

# Task1: Highly rated | 4.7 or more
# 2 loops
print("Task 1")
highlyrated = []
for book in books:
    for key, value in book.items():
        if key == "rating" and value >= 4.7:
            highlyrated.append(book["title"])
print(highlyrated)
# # 1 loop
print("Task 1.5")
highlyrated = []
for book in books:
    if book["rating"] >= 4.7:
        highlyrated.append(book["title"])
print(highlyrated)

# Task2: List Comprehension
print("Task 2")
goodbooks = [book["title"] for book in books if book["rating"] >= 4.7]
# can add .sort() or sorted function
print(goodbooks)

# Task 3: A-Z order
# Expected Output
# ['A Brief History of Time', 'Clean Code', 'Sapiens']
# print(sorted(goodbooks)) # sorts it and provides a copy (does not mutate original)
# goodbooks.sort() # mutates the list
# print(goodbooks)

inventory = [
    {"name": "Apple", "quantity": 30, "price": 0.50},
    {"name": "Banana", "quantity": 20, "price": 0.20},
]
print(inventory)

# Task 1 - Add new product
# What is the product name?
# What is the quantity?
# What is the price?

# Clue
# new_product = ("name": "Orange", "quantity": 10, "price": 0.60)
print("Task 1")
newname = input("What is the product name? ")
newquantity = int(input("What is the quantity? "))
newprice = float(input("What is the price? "))
new_product = {"name": newname, "quantity": newquantity, "price": newprice}
inventory.append(new_product)
print(inventory)

# Task 2: If exists then Update quantity & price & Task 3: Not Exist Add to Inventory
# What is the product name? Apple
# What is the quantity? 40
# What is the price? 0.4
# Expected output
# inventory = [
#     {"name": "Apple", "quantity": 70, "price": 0.4},
#     {"name": "Banana", "quantity": 20, "price": 0.20}
# ]

# Ask user for inputs
print("Task 2")
newname = input("What is the product name? ")
newquantity = int(input("What is the quantity? "))
newprice = float(input("What is the price? "))
# create new product
new_product = {"name": newname, "quantity": newquantity, "price": newprice}
addnewproduct = True  # boolean -> should we add product (if not exist)
for product in inventory:
    if newname == product["name"]:
        print(product["name"])
        product["quantity"] += newquantity
        product["price"] = newprice
        addnewproduct = False
        break
if addnewproduct:
    inventory.append(new_product)
print(inventory)

# More optomised version (no flag)
# for ... else
for product in inventory:
    if newname == product["name"]:
        print(product["name"])
        product["quantity"] += newquantity
        product["price"] = newprice
        addproduct = False
        break
        # Only when break does not happen then to else
else:
    inventory.append(new_product)
print(inventory)

# 5 pillars -> Good Quality
# 1. Readability - 70%
# 2. Maintainability
# 3. Extendability
# 4. Testability
# 5. Performance

# New Task

# list of dictionaries
guests = [
    {"name": "Alice", "age": 25, "code": "VIP123"},
    {"name": "Bob", "age": 17, "code": "VIP123"},
    {"name": "Charlie", "age": 30, "code": "VIP123"},
    {"name": "Dave", "age": 22, "code": "GUEST"},
    {"name": "Eve", "age": 29, "code": "VIP123"},
]

blacklist = ["Dave", "Eve"]

# Output
# People who are 21 or above and VIP123
# Blacklist people are not allowed
# ['Alice', 'Charlie']

# PEP - Python Enhancement Proposals

acceptable = []
# # CONSTANT_CASE
PASS_CODE = "VIP123"
# # check if bad
for guest in guests:
    if guest["name"] in blacklist or guest["age"] < 21 or guest["code"] != PASS_CODE:
        continue
    else:
        acceptable.append(guest["name"])
print(acceptable)

# # check if good
acceptable2 = []
for guest in guests:
    if (
        guest["name"] not in blacklist
        and guest["age"] >= 21
        and guest["code"] == PASS_CODE
    ):
        acceptable2.append(guest["name"])
print(acceptable2)

# # List comprehension check if good
acceptable3 = [
    guest["name"]
    for guest in guests
    if (
        guest["name"] not in blacklist
        and guest["age"] >= 21
        and guest["code"] == PASS_CODE
    )
]
print(acceptable3)

nums = [90, 50, 80]
# enumerate gives you both the index and value (a list of tuples)
# (0, 90) (1, 50) (2, 80)
# for num in enumerate(nums):
#     print(num)
print(list(enumerate(nums)))
# can unpack tuple values
# 0 90 1 50 2 80
# for idx, num in enumerate(nums):
#     print(idx, num)

# 2023
employees = [
    {"name": "Alex", "experience": 2},
    {"name": "Gemma"},
    {"name": "Rashay", "experience": 4},
    {"name": "Thato"},
]

# 2024
# Expected Output
# employees = [
#   {"name": "Alex", "experience": 3},
#   {"name": "Gemma", "experience": 1},
#   {"name": "Rashay", "experience": 5},
#   {"name": "Thato", "experience": 1}
# ]
print(employees)

# Task 1
# for employee in employees:
#   if employee.get('experience') is None:
#     employee['experience'] = 1
#   else:
#     employee['experience'] += 1
# print(employees)

# Task 2
for employee in employees:
    # need to give default value for safety
    employee["experience"] = employee.get("experience", 0) + 1
print(employees)

# Task 3
# employees = [employee['experience'] = 1 if employee.get('experience') is None
# else employee['experience'] += 1 for employee in employees]
# Senior 5 or more, mid-level 3 to 5, Junior < 3
# Expected Output
# employees = [
#   {"name": "Alex", "experience": 3, status: "Mid-Level"},
#   {"name": "Gemma", "experience": 1, status: "Junior"},
#   {"name": "Rashay", "experience": 5, status: "Senior"},
#   {"name": "Thato", "experience": 1, status: "Junior"}
# ]

# for employee in employees:
#   if employee.get('experience', 0) < 3:
#     employee['status'] = "Junior"
#   elif employee.get('experience', 0) < 5:
#     employee['status'] = "Mid-Level"
#   else:
#     employee['status'] = "Senior"
# print(employees)

for employee in employees:
    experience = employee["experience"]
    if experience < 3:
        employee["status"] = "Junior"
    elif experience < 5:
        employee["status"] = "Mid-Level"
    else:
        employee["status"] = "Senior"
print(employees)

# Copy
movie = {"name": "Mr Bones", "year": 2001}

# Make copy of dicitonary
movie_copy1 = movie.copy()

# Unpacking Operator * -> List | ** -> Dictionaries
movie_copy2 = {**movie, "rating": 10}
print(movie_copy2)

movie_copy3 = {
    **movie,
    "rating": 10,
    "year": 2002,
}  # last "year" overrides previous one, therefore 2002
print(movie_copy3)

movie_copy4 = {
    "rating": 10,
    "year": 2002,
    **movie,
}  # last "year" overrides previous one, therefore 2001
# the unpacking is like this
# {"rating": 10, "year":2002, "name": "Mr Bones", "year":2001} (2001 overrides!)
print(movie_copy4)

detail = {"actor": "Leon Schuster", "director": "Dzithendo"}
# Concatenate dictionaries into one using copies!!!!
movie_details = {**movie, **detail}  # ** = unpacking copy of dicts
print(movie_details)

price = [1000, 1200, 400]
price_copy = [*price]  # copy with one star as it is a list!
# print(price_copy)
# UNPACKING OPERATOR!
price_copy1 = [50, 40, *price, 60]
print(price_copy, price_copy1)

t1 = [80, 90]
t2 = [50, 60]
t3 = t1 + t2
print(t3)
t3 = [*t1, *t2]
print(t3)
