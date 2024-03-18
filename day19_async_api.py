import requests
import aiohttp
import asyncio
from time import time
from pprint import pprint

TOKEN = "f06fdf2d66c24a91a6c93111241503"

# url_ex = "http://api.weatherapi.com/v1/current.json?key=f06fdf2d66c24a91a6c93111241503&q=cape%20town&aqi=no"


# def get_temp(city):
#     city_changed = city.replace(" ", "%20")
#     created_url = (
#         f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_changed}&aqi=no"
#     )
#     response = requests.get(created_url, verify=False)
#     weather_city = response.json()
#     # print(type(weather_city))
#     # print(weather_city)
#     return f'The temperature in {weather_city["location"]["name"]} is {int(weather_city["current"]["temp_c"])}°C'


# print(get_temp("cape town"))


# async -> co_routine
async def get_city_temp(city_name):
    # show one by one printing and make it slow
    print(f"Getting temp of {city_name}")
    await asyncio.sleep(2)

    city_name2 = city_name.replace(" ", "%20")
    url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name2}&aqi=no"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            print(
                f'The temperature in {weather["location"]["name"]} is {int(weather["current"]["temp_c"])}°C'
            )


# async -> co_routine
async def get_city_temp2(city_name):
    # show one by one printing and make it slow
    print(f"Getting temp of {city_name}")
    await asyncio.sleep(2)

    city_name2 = city_name.replace(" ", "%20")
    url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name2}&aqi=no"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            # print(
            #     f'The temperature in {weather["location"]["name"]} is {int(weather["current"]["temp_c"])}°C'
            # )
            return weather["location"]["name"], int(weather["current"]["temp_c"])


# async -> co-routine
# Task 1 - gather
# async def main():
#     print("Task 1")
#     # await get_city_temp("Chennai")
#     # await get_city_temp("Johannesburg")
#     # await get_city_temp("Durban")

#     all_get_temp_city_co_routines = [
#         get_city_temp("Cape Town"),
#         get_city_temp("Chennai"),
#         get_city_temp("Johannesburg"),
#     ]
#     await asyncio.gather(*all_get_temp_city_co_routines)


# Task 2 - gather & create task
# async def main():
#     print("Task 2")
#     all_get_temp_city_co_routines = [
#         asyncio.create_task(get_city_temp("Cape Town")),
#         asyncio.create_task(get_city_temp("Chennai")),
#         asyncio.create_task(get_city_temp("Johannesburg")),
#     ]
#     await asyncio.gather(*all_get_temp_city_co_routines)

# Task 4
# async -> coroutine
# async def get_list_city_temp(city_list):
#     # dict to store all cities and temperatures
#     list_city_temp = {}
#     # go through each city
#     for city in city_list:
#         # set up url to fetch from
#         city_name = city.replace(" ", "%20")
#         url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
#         # use "aiohttp" to get required data from api through a session
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 weather = await response.json()
#                 list_city_temp.update(
#                     {weather["location"]["name"]: int(weather["current"]["temp_c"])}
#                 )
#                 # return await asyncio.gather(get_city_temp2(city))
#     return list_city_temp
# pprint(list_city_temp, indent=4)

# RAGAV ALL CODE TASK 4


# async def get_city_name_temp(city_name):
#     print(f"Getting temp of {city_name}")
#     url = f"https://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             weather = await response.json()
#             return (weather["location"]["name"], weather["current"]["temp_c"])


# async def main(cities):
#     # print(await get_city_name_temp("New York"))
#     # print(await get_city_name_temp("Hong Kong"))
#     cities_data = [await get_city_name_temp(city) for city in cities]
#     pprint(dict(cities_data))


# asyncio.run(main(cities))


# Performance
# async def main(cities):
#     cities_data_co_current = [get_city_name_temp(city) for city in cities]
#     cities_data = await asyncio.gather(*cities_data_co_current)
#     pprint(dict(cities_data))


# asyncio.run(main(cities))


# Task 4 RAGAV
# async -> co_routine
async def get_city_name_temp(city_name):
    print(f"Getting temp of {city_name}")
    city_name2 = city_name.replace(" ", "%20")
    url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name2}&aqi=no"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            return weather["location"]["name"], int(weather["current"]["temp_c"])


# Task 3
# async def main():
#     # print("Task 3")
#     cities = [
#         "New York",
#         "Tokyo",
#         "London",
#         "Paris",
#         "Dubai",
#         "Singapore",
#         "Sydney",
#         "Istanbul",
#         "Hong Kong",
#         "Cape Town",
#     ]
#     # don't have to use "create_task"
#     # get_temp_all = [asyncio.create_task(get_city_temp(city)) for city in cities]
#     # await asyncio.gather(*get_temp_all)

#     print("Task 4")
#     # NO - does one by one and slow
#     # print(await get_city_name_temp("New York"))
#     # print(await get_city_name_temp("Hong Kong"))
#     cities_data = [await get_city_name_temp(city) for city in cities]
#     pprint(dict(cities_data))

#     # Performance
#     cities_data_concurrent = [get_city_name_temp(city) for city in cities]
#     cities_data = await asyncio.gather(*cities_data_concurrent)
#     pprint(dict(cities_data))


# async speedup!
# start_time = time()
# asyncio.run(main())
# end_time = time()

# print(f"Time taken: {end_time - start_time}")

# convert array of tuples to dict
# arr = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
# {k: v for k, v in arr}
# or
# dict(arr)


# Task 5
# print all users names
# async -> co-routine
async def get_names(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            users = await response.json()
            # print(users)
    return "\n".join([user["name"] for user in users])


async def main():
    names_url = "https://65f8286cb4f842e8088713ab.mockapi.io/users"
    print("Task 5")
    # do not need gather as we are firing one api
    print(await get_names(names_url))


# asyncio.run(main())

# params
# have to put data in the body (POST and PUT requests) (safer)
# mockapi autogenerates created at and id values
# postman used to test if api is working


# Delete user with id = 15
async def delete_user_by_id(id):
    url = f"https://65f8286cb4f842e8088713ab.mockapi.io/users/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.delete(url) as response:
            user = await response.json()
            # print(users)
    return user


async def main(id):
    user = await delete_user_by_id(id)
    pprint(user)


# asyncio.run(main(10))

# Task - 1
# Delete the first 5 users
# Performant < 0.5s

#     # Performance
#     cities_data_concurrent = [get_city_name_temp(city) for city in cities]
#     cities_data = await asyncio.gather(*cities_data_concurrent)
#     pprint(dict(cities_data))


async def get_first_five_users(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            users = await response.json()
            # print(users)
    return [user["id"] for user in users[0:5]]


async def main2():
    names_url = "https://65f8286cb4f842e8088713ab.mockapi.io/users"
    # first_five_ids = [1, 2, 4, 5, 6]
    first_five_ids = await get_first_five_users(names_url)
    print(first_five_ids)
    users_data_concurrent = [delete_user_by_id(id) for id in first_five_ids]
    users_data = await asyncio.gather(*users_data_concurrent)
    pprint(users_data)


# async speedup!
# start_time = time()
# asyncio.run(main2())
# end_time = time()

# print(f"Time taken: {end_time - start_time}")


# Task 2
# Change all the users' avatars to human rights flag


async def get_all_users_id(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            users = await response.json()
            # print(users)
    return [user["id"] for user in users]


import json


async def update_avatar(id):
    url = f"https://65f8286cb4f842e8088713ab.mockapi.io/users/{id}"
    # have to make avatar json
    avatar = {
        "avatar": "https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg"
    }
    async with aiohttp.ClientSession() as session:
        async with session.put(url, data=json.dumps(avatar)) as response:
            updated_user = await response.json()
    return updated_user


async def main3():
    print("Main 3 Final")
    names_url = "https://65f8286cb4f842e8088713ab.mockapi.io/users"
    # get all the user ids
    all_users_id = await get_all_users_id(names_url)
    # get all co-routines (load shotgun)
    users_data_co_routine = [update_avatar(id) for id in all_users_id]
    # use "gather" to run all co-routines concurrently (shoot all co-routines)
    users_data = await asyncio.gather(*users_data_co_routine)
    # get data that was updated and pretty print it out
    pprint(users_data)


start_time = time()
asyncio.run(main3())
end_time = time()

print(f"Time taken: {end_time - start_time}")
