# Shortcuts
# ctrl + shift + p -> command
# ctrl + p -> find file

# VS Code and Discord is chrome????

price = 100

# Scope = lifetime of a variable
# Lexical scope
# Closure = own scope + lexical scope
def market():

    def get_price():
        print("the price is: ", price)

# get_price() # unknown
market()

def cool():
    x = 10
    print("Super")

cool()
# print("The value of x is: ", x)

code_word = "Hulk"

def space_ship():
    question = "Please provide code word"

    def code_word_check():
        password = "Hulk"
        print(question) # checks if question is defined locally and then checks lexical scope

        if(password == code_word):
            print(f"Welcome, {password} the strongest avenger 💪")
        else:
            print("❌ Access denied to 🚀")
    code_word_check()

space_ship() 

# Currying
def add(x):
    def add1(y):
        return x + y 
    return add1
print(add(10)(5)) 
# x -> y -> x + y

# Closure/Lexical Scope
add = lambda x: lambda y: x + y 


# Default value copy by reference 

def fun(nums=[]):
    nums.append(10)
    print(nums)

# Interesting - mutable value overshadowed by local reference after adding to it
fun() # [10]
fun() # [10, 10]
fun() # [10, 10, 10]
fun() # [10, 10, 10]
# Why? = the nums variable default value will share the same reference 

print("fun2")
def fun2(nums2=()):
    if nums2 == ():
        nums2 = []
    nums2.append(10)
    print(nums2)

fun2() # [10]
fun2() # [10]
fun2() # [10]
fun2() # [10]
fun2([70]) # [70, 10]

print("fun3")
# Class solution
# Singleton -> None (one of a kind) (immutable value) 
def fun3(nums=None):
    if nums is None:
        nums = []
    nums.append(10)
    print(nums)

fun3() # [10]
fun3() # [10]
fun3() # [10]
fun3() # [10]
fun3([70]) # [70, 10]

# is vs ==
x1 = [2,3]
x2 = [2,3]
x3 = x1
print(x1 == x2) # True -> checks if values are the same
print(x1 is x2) # False -> checks if memory addresses are the same
print(x1 is x3) # True