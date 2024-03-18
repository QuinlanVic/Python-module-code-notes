import asyncio


# have to mark function as async
async def hello_world():
    print("Started 🌏")
    # another async function in an async function
    # therefore you have to "await" it and you pause execution until you continue with the "hello_world" function
    await asyncio.sleep(3)
    print("Hello, Sanlam🌏")


# how to run an async function
# asyncio.run(hello_world())


# Task 1 + 2 countdown
# Eg) 3, 2, 1, Happy New Year
async def countdown(count):
    for i in range(count, 0, -1):
        # or
        # for i in reversed(range(1, count + 1)):
        print(i)
        await asyncio.sleep(1)
    print("Happy New Year 🎊")


# asyncio.run(countdown(3))


# Task 3 countdown without any loop
# Eg) 3, 2, 1, Happy New Year
async def print_countdown(msg):
    # can only use await in an async function
    await asyncio.sleep(1)  # "sleep" -> inbuilt async function
    print(msg)


async def countdown():
    # these are async that have to be awaited since they are inside another async function
    await print_countdown(3)
    await print_countdown(2)
    await print_countdown(1)
    await print_countdown("Happy New Year 🎊")


# all async functions return a coroutine
# print(type(countdown()))
asyncio.run(countdown())

# Event Loop: Behind Async function
# our code will (line by line) be placed in a call stack
# once completed it will be removed from the stack
# through either a return or when the function completes
# first in last out or last in first out (FILO or LIFO)

# execution on call stack example
# call stack
# c = 4 + 6 (pulled from stack 5)
# 5 + 1 (pulled from stack 3)
# add (5) (pulled from stack 4)
# 3 + 1 (pulled from stack 1)
# add (3) (pulled from stack 2)
# add(a) + add(b) (pulled from stack 0)
# sum (3, 5)
# UP!
# print(sum(3, 5))


def add(x):
    return x + 1


def sum(a, b):
    c = add(a) + add(b)
    return c


print(sum(3, 5))


# def dbl(x):
#     y = x * 2
#     dbl(y)


# dbl(10) # infinite loop
