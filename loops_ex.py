numbers = [8, 5, 7, 4, 6, 2]

# Task 1: With List Comprehension
# ["Even", "Odd", "Odd", "Even", "Even", "Even"]
# change format to account for if and else
evenorodd = ["Even" if (number % 2 == 0) else "Odd" for number in numbers]
print(evenorodd)

# numbers_copy = [] # 1.
# for num in numbers: # 3.
#   numbers_copy.append("Even" if num % 2 == 0 else "Odd") # 2. & 3.
# print(numbers_copy)
