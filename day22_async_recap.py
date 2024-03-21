import asyncio


async def background_task1():
    print("Start background task 1")
    await asyncio.sleep(3)  # Simulating a background task


async def background_task2():
    print("Start background task 2")
    await asyncio.sleep(2)  # Simulating a background task


async def background_task3():
    print("Start background task 3")
    await asyncio.sleep(2)  # Simulating a background task


async def main():
    # Sequence - Take total 7s (sync)
    # await background_task1()  # 3s  (When things take time - await)
    # await background_task2()  # 2s
    # await background_task3()  # 2s

    # Concurrent (Parallel) - 3s (async)
    await asyncio.gather(background_task1(), background_task2(), background_task3())
    print("Main function says - Hi " * 4)


from time import time

start = time()
asyncio.run(main())  # 7s vs 3s
end = time()
print(f"Total time = {end - start}")


# await getUser('123') # GET

data = {"id": "123", "name": "Rashay", "age": 20, "friends": ["234", "346", "567"]}

#  await getUser('234')

data = {"id": "234", "name": "Quinlan", "age": 20, "friends": ["123", "569", "567"]}

# "Rashay"  "123" -> "friends" ["234", "346", "567"]
# gather(getUser('234'),  getUser('346'),  getUser('567'))


# Cooking
# async Toasting
# 1. await Toasting (1s)
# 2. await Buttering (2s)

# async Coffee
# 1. await Mix water coffee powder  (2s)
# 2. await Mix the sugar  (1s)

# gather(Toasting, Coffee) # directly
# gather(*[Toasting, Coffee]) # unpacking list


async def make_coffee():
    print("Coffee brewing ☕")
    await asyncio.sleep(2)
    print("Coffee done ✅")
    return f"Data - Coffee ☕"


async def cooking_eggs():
    print("Egg cooking 🥚")
    await asyncio.sleep(3)
    print("Eggs cooked ✅")
    return f"Data - Eggs cooked"


# result1 = cooking_eggs()  # co-routine  Box(f"Data - Eggs cooked")  | Box -> co-routine
# result2 = await cooking_eggs()          f"Data - Eggs cooked"
# result3 = make_coffee()  # co-routine  Box(f"Data - Coffee ☕")
# result4 = await make_coffee()          f"Data - Eggs cooked"

# type(result1)  # co-routine
# type(result2)  # string

# gather(result1, result3)  # 2            Box([output1, output2]) | Box -> co-routine
# await gather(result1, result3) # 2    [output1, output2]
# gather(*[result1, result3]) # 2
# gather(result2, result4)
