import asyncio


# have to mark function as async
async def hello_world():
    print("Started 🌏")

    # another async function in an async function
    # therefore you have to "await" it and you pause execution until you continue with the "hello_world" function
    # have to wait for sleep to be completed for "hello_world" to complete
    # (if you do not then the function is pushed into the wait loop and is cancelled when "hello_world" completes)
    # awaits are all generators in disguise (pausing execution like "yield")
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
        # async function inside of async function
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
    await print_countdown(3)  # sync
    await print_countdown(2)  # sync
    await print_countdown(1)  # sync
    await print_countdown("Happy New Year 🎊")


# all async functions return a coroutine
# print(type(countdown()))
# asyncio.run(countdown())

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
# sum (3, 5) (pulled from stack 6)
# UP!
# print(sum(3, 5)) (pulled from stack 7)


def add(x):
    return x + 1


def sum(a, b):
    c = add(a) + add(b)
    return c


# print(sum(3, 5))


# def dbl(x):
#     y = x * 2
#     dbl(y)
# dbl(10) # infinite loop

# Event loop will only push to the stack when the call stack is empty
# during that time it sits in the callback queue
# The async function will be scheduled until the call stack is empty


async def cooking_eggs():
    print("Egg cooking")
    await asyncio.sleep(3)
    print("Eggs cooked ✅")


async def make_coffee():
    print("Coffee brewing ☕")
    await asyncio.sleep(2)
    print("Coffee done ✅")


# async function with the event loop
async def main():
    # await cooking_eggs()  # sync
    # await make_coffee()  # sync
    # waiting for the background task
    # print("Bread Toast 1")
    # print("Bread Toast 2")
    # print("Bread Toast 3")
    # print("Bread Toast 4")

    # Request to event loop to schedule immediately after creating the task
    # Event loop manages scheduling between callback queue and call stack
    task1 = asyncio.create_task(cooking_eggs())  # concurrently
    task2 = asyncio.create_task(make_coffee())  # concurrently

    # running while background tasks are happening as call stack is empty
    print("Bread Toast 1")
    print("Bread Toast 2")
    print("Bread Toast 3")
    print("Bread Toast 4")

    # have to place the await here as otherwise the task will execute in the background but
    # if the "main" function finishes executing before the background task it will not complete
    # do not know which task will take longer to execute and therefore cannot predict which one to await
    # if you choose the wrong one then some code of one of the tasks may not execute
    await task1
    await task2
    # wait until the longest one completes
    # await asyncio.wait({task1, task2}) # set of tasks to wait for


# asyncio.run(main())


async def cooking_eggs():
    print("Egg cooking 🥚")
    await asyncio.sleep(3)
    print("Eggs cooked ✅")
    return f"Data - Eggs 🥚"


async def make_coffee():
    print("Coffee brewing ☕")
    await asyncio.sleep(2)
    print("Coffee done ✅")
    return f"Data - Coffee ☕"


async def make_cereal():
    print("Making Cereal bowl 🧃")
    await asyncio.sleep(5)
    print("Cereal done ✅")
    return f"Data - Cereal 🧃"


async def main():
    # Request to event loop to schedule
    # task1 = asyncio.create_task(cooking_eggs())  # concurrently
    # task2 = asyncio.create_task(make_coffee())  # concurrently
    # task3 = asyncio.create_task(make_cereal())  # concurrently
    # all_tasks = [task1, task2, task3]

    # does not schedule immediately - therefore sleep happens to you
    # all_tasks = [
    #     cooking_eggs(),  # concurrently
    #     make_coffee(),  # concurrently
    #     make_cereal(),  # concurrently
    # ]

    # vs

    # schedules immediately and sleep does not happen directly as it overlaps with task execution!!!!!!!!!!!!!!
    all_tasks = [
        asyncio.create_task(cooking_eggs()),  # concurrently
        asyncio.create_task(make_coffee()),  # concurrently
        asyncio.create_task(make_cereal()),  # concurrently
    ]

    print("Bread Toast 1")
    print("Bread Toast 2")
    print("Bread Toast 3")
    print("Bread Toast 4")

    # initial wait
    await asyncio.sleep(6)

    # wait until the longest one completes
    # await asyncio.gather(all_tasks[0], all_tasks[1], all_tasks[2])

    # takes in a list and we can unpack it (simpler)
    # want to fire all async functions together concurrently!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    data = await asyncio.gather(*all_tasks)
    # print(type(data)) # list
    # order of data RETURNED depends on order of tasks put into all_tasks
    print(data)


# asyncio.run(main())


async def cooking_eggs():
    print("Egg cooking 🥚")
    await asyncio.sleep(3)
    print("Eggs cooked ✅")
    return f"Data - Eggs 🥚"


async def make_coffee():
    print("Coffee brewing ☕")
    await asyncio.sleep(2)
    print("Coffee done ✅")
    return f"Data - Coffee ☕"


async def make_cereal():
    print("Making Cereal bowl 🧃")
    await asyncio.sleep(5)
    print("Cereal done ✅")
    return f"Data - Cereal 🧃"


async def main():
    # Request to event loop to schedule
    # task1 = asyncio.create_task(cooking_eggs())  # concurrently
    # task2 = asyncio.create_task(make_coffee())  # concurrently
    # task3 = asyncio.create_task(make_cereal())  # concurrently

    # scheduling is done immediately when tasks are created
    # starts before sleep starts and finishes before sleep has ended
    all_co_routines = [
        asyncio.create_task(cooking_eggs()),  # concurrently
        asyncio.create_task(make_coffee()),  # concurrently
        asyncio.create_task(make_cereal()),  # concurrently
    ]

    # vs

    # put into a list but no scheduling is done immediately
    # starts only after sleep
    # all_co_routines = [
    #     # do not need to mention/create tasks
    #     # it is ok if they are all async functions
    #     cooking_eggs(),  # concurrently
    #     make_coffee(),  # concurrently
    #     make_cereal(),  # concurrently
    # ]

    print("Bread Toast 1")
    print("Bread Toast 2")
    print("Bread Toast 3")
    print("Bread Toast 4")

    # same as example above in terms of task execution
    print("Sleep started (6 sec hehe)")
    await asyncio.sleep(6)
    print("Sleep ended")

    # takes in a list and we can unpack it (simpler)
    # the scheduling only happens here if the elements in the list are not tasks!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # each element must be a task/co-routine and is passed to "gather" without having to list it explicitly
    data = await asyncio.gather(*all_co_routines)
    # print(type(data)) # list
    # order of data depends on order of tasks put into all_tasks
    print(data)


asyncio.run(main())

# When things are dependent on one another you cannot do it asynchronously
# If they are not then you can do asynchronously


async def make_coffee():
    print("Coffee brewing")
    await asyncio.sleep(2)
    print("Coffee done")
    return f"Data - Coffee"


async def cooking_eggs():
    print("Egg cooking")
    await asyncio.sleep(3)
    print("Eggs cooked")
    return f"Data - Eggs cooked"


# co-routine (async function returns a co-routine) = Box(f"Data - Eggs Cooked") | Box -> co-routine
result1 = cooking_eggs()
# string = f"Data - Eggs Cooked" | opens box -> await co-routine
# result2 = await cooking_eggs()
result3 = make_coffee()
# result4 = await make_coffee()

type(result1)  # co-routine
# type(result2) # string

# asyncio.gather(result1, result3)  # Box([output, output2])
# This is why we use no await inside gather and then an await outside with gather
# (and because it is called inside an async function and is an async function itself)
# await gather(result1, result3) # [output1, output2]

# therefore for gather you have to use the co-routines, not awaits as they return strings and you need to

# Mock API = all CRUD operations and it is free (e.g. can't delete from chrome)

# event loop is only called when working with asynch functions
# async.run() is where it starts
# ends when call stack is empty
# functions not waited for are thrown out of event loop if parent async function ends before they complete

# call stack = FILO / LIFO
# function calls inside of other functions builds the stack
# block things when call stack is busy and nothing cna enter
