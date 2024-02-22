# one liners, unnamed/anonymous/nameless
# anything after ":" is implicitly (automatically) returned
add = lambda a, b: a + b # assign a function to a variable (1.)
print(add(6,7))

# Functions are treated as first class citizens (value)

# 1. Assign a function to a variable
# 2. Pass a function as an argument
# 3. Return a function

player_stats = [10, 30, 60]

def square (x):
  return x * x
# map accepts normal and lambda functions to apply to each list element 
boosted_stats = map(square, player_stats) 
print(list(boosted_stats)) # have to convert map constructor into list
boosted_stats = map(lambda x: x*x, player_stats) 
print(list(boosted_stats)) # have to convert map constructor into list

# if a function is not going to be reused then use lambda 

def say_hello():
  return "Hello, "

# Higher-order function (accepts another function)
def greeting(hello_message, name):
  # call function given as parameter to greeting
  print(hello_message() + name) # print function output and add "name" to it

greeting(say_hello, 'Caleb') # pass function as value and string
# print(type(say_hello))

# map does not mutate the original list
def map_own(fn, lst):
  # newlst = []
  # for element in lst:
  #   newlst.append(fn(element))
  # return newlst 
  # List comprehension!
  return [fn(element) for element in lst]
boosted_stats = map_own(square, player_stats) 
print(boosted_stats)
print(player_stats)

# map object -> lazy | efficient

