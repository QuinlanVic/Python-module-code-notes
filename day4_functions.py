# a = 8
# b = 10

# print("The sum is: ", a + b)

# a1 = 60
# b1 = 70

# print("the sum is: ", a1 + b1)

# a2 = 600
# b2 = 70

# print("The sum is: ", a2 + b2)


# Functions are a way to pack your logic
# Declaration / Definition
# sum = function name
# a and b are the 2 parameters
def sum(a, b):
    # a + b # None
    return a + b  # body


# Abstracted the logic | Hiding implementation

print("the sum is: ", sum(30, 50))


# Default values!!!!
# default value if argument not given
# All default values have to be at the end/last. Cannot have default values for
# arguments before and not have after
def driving_test(name, age=15, car="Toyota tazz"):
    # print(age)
    if age >= 18:
        return f"{name} you're eligible for driving. You will do the test with a {car}"
    else:
        return "Try again after a few years :)"


# print(driving_test("Caleb", 20, "GR Corolla"))
# print(driving_test(10))
# print(driving_test("Gemma", 20))

# Types of argument
# Position argument (normal, based on order/position of argument)
# Keyword arguments (give keyword="parameter")!!!!
print(driving_test(age=21, name="Tina"))  # order does not matter (keyword argument)
print(driving_test("Gemma"))  # order matters (position argument)
listb4rev = [9, 3, 8]
listb4rev.sort(reverse=True)  # mutates it
print(listb4rev)
print(sorted(listb4rev))  # reverse order copy
