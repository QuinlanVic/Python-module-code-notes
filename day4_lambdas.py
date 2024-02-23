# one liners, unnamed/anonymous/nameless
# anything after ":" is implicitly (automatically) returned
add = lambda a, b: a + b # assign a function to a variable (1.)
print(add(6,7))

# Functions are treated as first class citizens (value)

# 1. Assign a function to a variable
# 2. Pass a function as an argument to a function
# 3. A function can return another function

player_stats = [10, 30, 60]

def square (x):
  return x * x
# map accepts normal and lambda functions to apply to each list element 
boosted_stats = map(square, player_stats) 
# returns a map object (always same length as og list input)
print(list(boosted_stats)) # have to convert map constructor into list
boosted_stats = map(lambda x: x*x, player_stats) 
print(list(boosted_stats)) # have to convert map object into list using list constructor
# The function that filter accepts must return a boolean. 
# Returns an iterable of elements that obey the condition (max = length of list)
result = filter(lambda x: x > 10, [10, 50, 60, 100, 6, 8, 30])

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

def sayHello1():
  def msg():
    return "Hello, 🎊"
  return msg 

# Task 1
msg_function = sayHello1()
print(msg_function())

# Task 2
print(sayHello1()())

# Task 3
# Anything on the right of the ":" is returned by the lambda function
# In this case another function is returned | Implicit return | Factory function
# Programming paradigm = Functional programming (currying)
mul = lambda x: lambda y: x * y

# print(type(mul(5))) # type function
# mul 5 = lambda y: 5 * y
# 3 6 -> 18
# first application accepts 3, second application of returned function accepts 6
print(mul (3)(6))
# lambda x is returning lambda y as a function
# x -> y -> x * y
mul_1 = mul (3)
print(mul_1(6))

# Higher Order Function (HOF) - Argument = function
result1 = map(lambda x: x * 2, [10, 30, 60])
result2 = filter(lambda x: x > 10, [0, 50, 60, 100, 6, 8, 30])
print(list(result1))
print(list(result2))

# Sequence - List

print(sum([10, 30, 60]))
print(max([10, 80, 30, 60]))
print(min([10, -1, 30, 60]))

print(all([True, False, True]))
print(any([True, False, True]))

print(all([10, 0, 30, -1]))

# Falsy values | When converted to Boolean = False
# 1. 0
# 2. []
# 3. None
# 4. {}
# 5. ""
# 6. set()
# 7. ()
# 8. False

x = []
if (x):
  print('cool')
else:
  print('super')