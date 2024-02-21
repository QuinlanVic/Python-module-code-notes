# books = [
#   {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
#   {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
#   {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
#   {"title": "Sapiens", "rating": 4.9, "genre": "History"},
#   {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
# ]

# Task1: Highly rated | 4.7 or more
# 2 loops
# highlyrated = []
# for book in books:
#   for key, value in book.items():
#     if key == "rating" and value >= 4.7:
#       highlyrated.append(book["title"])  
# print(highlyrated)
# # 1 loop
# highlyrated = []
# for book in books:
#     if book["rating"] >= 4.7:
#       highlyrated.append(book["title"])  
# print(highlyrated)

# Task2: List Comprehension
# goodbooks = [book["title"] for book in books if book["rating"] >= 4.7] 
# can add .sort() or sorted function
# print(goodbooks)

# Task 3: A-Z order
# Expected Output
# ['A Brief History of Time', 'Clean Code', 'Sapiens']
# print(sorted(goodbooks)) # sorts it and provides a copy (does not mutate original)
# goodbooks.sort() # mutates the list
# print(goodbooks)

inventory = [
    {"name": "Apple", "quantity": 30, "price": 0.50},
    {"name": "Banana", "quantity": 20, "price": 0.20} 
]
# print(inventory)

# Task 1
# What is the product name?
# What is the quantity?
# What is the price?

# Clue
# new_product = ("name": "Orange", "quantitiy": 10, "price": 0.60)

# newname = input("What is the product name? ")
# newquantity = int(input("What is the quantity? "))
# newprice = float(input("What is the price? "))
# new_product = {"name": newname, "quantitiy": newquantity, "price": newprice}
# inventory.append(new_product)
# print(inventory)

# Task 2: If exists then Update quantity & price & Task 3: Not Exist Add to the Inventory
# What is the product name? Apple
# What is the quantity? 40
# What is the price? 0.4
# Expected output
# inventory = [
#     {"name": "Apple", "quantity": 70, "price": 0.4},
#     {"name": "Banana", "quantity": 20, "price": 0.20} 
# ]
# Ask user for inputs
# newname = input("What is the product name? ")
# newquantity = int(input("What is the quantity? "))
# newprice = float(input("What is the price? "))
# create new product
# new_product = {"name": newname, "quantity": newquantity, "price": newprice}
# addproduct = True # boolean -> should we add product (if not exist)
# for product in inventory:
#   if (newname == product["name"]):
#     print(product["name"])
#     product["quantity"] += newquantity
#     product["price"] = newprice
#     addproduct = False
#     break
# if (addproduct):
#   inventory.append(new_product)
# print(inventory)

# More optomised version (no flag)
# for ... else
# for product in inventory:
#   if (newname == product["name"]):
#     print(product["name"])
#     product["quantity"] += newquantity
#     product["price"] = newprice
#     addproduct = False
#     break
#     # Only when break does not happen then to else
# else:
#   inventory.append(new_product)
# print(inventory)

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
  {"name": "Eve", "age": 29, "code": "VIP123"}
]

blacklist = ["Dave", "Eve"]

# Output
# People who are 21 or above and VIP123
# Blacklist people are not allowed
# ['Alice', 'Charlie']
acceptable = []
for guest in guests:
  if (guest["name"] in blacklist or guest["age"] < 21 or guest["code"] != "VIP123"):
    continue 
  else:
    acceptable.append(guest["name"])
print(acceptable)