books = [
  {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
  {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
  {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
  {"title": "Sapiens", "rating": 4.9, "genre": "History"},
  {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]

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
goodbooks = [book["title"] for book in books if book["rating"] >= 4.7] 
# can add .sort() or sorted function
print(goodbooks)

# Task 3: A-Z order
# Expected Output
# ['A Brief History of Time', 'Clean Code', 'Sapiens']
print(sorted(goodbooks)) # sorts it and provides a copy (does not mutate original)
# goodbooks.sort() # mutates the list
# print(goodbooks)

inventory = [
    {"name": "Apple", "quantity": 30, "price": 0.50},
    {"name": "Banana", "quantity": 20, "price": 0.20} 
]
print(inventory)

# Task 1
# What is the product name?
# What is the quantity?
# What is the price?

# Clue
# new_product = ("name": "Orange", "quantitiy": 10, "price": 0.60)

newname = input("What is the product name? ")
newquantity = int(input("What is the quantity? "))
newprice = float(input("What is the price? "))
new_product = {"name": newname, "quantitiy": newquantity, "price": newprice}
inventory.append(new_product)
print(inventory)

# Task 2: If exists then Update quantity & price
# What is the product name? Apple
# What is the quantity? 40
# What is the price? 0.4
# Expected output
# inventory = [
#     {"name": "Apple", "quantity": 70, "price": 0.4},
#     {"name": "Banana", "quantity": 20, "price": 0.20} 
# ]

