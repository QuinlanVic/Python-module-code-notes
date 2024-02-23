# import day5_cool

# # the entire file will be run using "import"
# # just want to grab function
# # __name__ is "day5_cool" in this file
# print(day5_cool.to_uppercase("Alex"))

# Alias
from day5_cool import to_uppercase as to_upper

print(to_upper("Alex"))

# Inbuilt packages
from math import pi

print(pi)

x = [3, 5, 8]

# dir(x)
# x.__ge__ -> dunder methods | Don't use | Internal methods