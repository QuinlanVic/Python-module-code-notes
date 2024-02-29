# Dictionary -> HashMap -> Key: Value
# Keys should be unique
# [] = List (mutable)
# () = Tuple (immutable)
# {} = Dictionary (mutable)
# Create Dictionary
person = {"name": "Siya Kolisi", "age": 32, "country": "South Africa", "sport": "Rugby"}

# print(person, type(person))
# Access Value
# print(person["name"]) # use key to access value
# Update Value
# person["age"] += 1 # update age by one year
# print(person)
# Methods
# Iterable -> List, Tuple, dict_keys
# access keys
print(person.keys(), type(person.keys()))
# access values
print(person.values())
print(person.items())  # key value pairs (tuples)

# Loop

# for detail in person.items():
#   print(detail) # all items
#   print(detail[0]) # only keys
#   print(detail[1]) # only values

# for key, value in person.items():
#   print(key, value)

person = {"name": "Siya Kolisi", "age": 32, "country": "South Africa", "sport": "Rugby"}

print(person, type(person))

# safety for value
# print(person['height']) # KeyError: 'height'
print(person.get("height"))  # None

# get('key', default_value)
print(person.get("height", 175))  # 175

person = {
    "name": "Siya Kolisi",
    "age": 32,
    "address": {
        "city": "Port Elizabeth",
        "country": "South Africa",
    },
    "school": "Grey high school",
    "height": 186,
    "sport": "Rugby",
}

print(person.get("height"))  # 186

# get('key', default_value)
print(person.get("height", 175))  # 186 (has height so default value not printed)
# print(person['address']['city']) # not safe, need to give default value if no address
# print(person['address', {}].get('city')) # safe now, if no address -> None


print(person.get("stats"))
# None.get('points')
# print(person.get('stats').get('points'))
# AttributeError: 'NoneType' object has no attribute 'get'!!!!
# Fix -> give empty dicitonary value which has get available
print(person.get("stats", {}).get("points"))  # None
# print(person.get('stats', {}).get('points', 'No points data')) # No points data

# Dictionary Comprehension!!!!
# Different to list comprehension with "{}" instead of "[]" and
# uses ":" notation to return a dictionary
nums = {x: x**2 for x in range(10) if x % 2 == 0}
print(nums)
