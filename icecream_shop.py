
flavourasked = input("Please input an icecream flavour: ")

stock1 = "vanilla"
stock2 = "lime"
stock3 = "chocolate"

#Task 1
# if (flavourasked == stock1 or flavourasked == stock2 or flavourasked == stock3):
# if (flavourasked in (stock1, stock2, stock3)): 
#   print("yes, we do have it")
# else:
#   print("No, we ran out of stock")

# Task 2
shop_stock = "vanilla, lime, chocolate"
# in operator | membership operator | boolean
if (flavourasked in shop_stock): 
  print("yes, we do have it")
else:
  print("No, we ran out of stock")
# refactor -> Code Quality (up)
result = "yes, we do have it" if flavourasked in shop_stock else "No, we ran out of stock"
print(result)

# Ternary operator (3 operands)
# ___ if condition else ___

# Binary operator (2 operands)
# >, <, ==, >=, <=, !=
# and, or
# arithmatic and comparison and logical operators (except not)
#  = assignment operator

# Unary operator (1 operand)
# not, ~

# Binary numbers
# 1 -> 1
# 2 -> 10
# 3 -> 11
# 4 -> 100
# 32-bit representation
# 4 -> 0...100
# ~4 = flips bits (all 0 -> 1 and vice versa)
# ~4 = 1...011 -> -5



# shopstocklist = shop_stock.split(", ") 
# for (int i = 0; i < len(shopstocklist); i++):
#   if (flavourasked == shopstocklist[i]):
#     have = True
#   else:
#     continue
# if have:
#     print("yes, we do have it")
# else:
#   print("No, we ran out of stock")
  
  



  