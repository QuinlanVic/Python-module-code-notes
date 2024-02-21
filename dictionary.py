
  # Dictionary -> HashMap -> Key: Value
  # Keys should be unique
  # [] = List (mutable)
  # () = Tuple (immutable)
  # {} = Dictionary (mutable)
  # Create Dictionary
person = {
  "name": "Siya Kolisi",
  "age": 32,
  "country": "South Africa",
  "sport": "Rugby"
}

print(person, type(person))
# Access Value
print(person["name"]) # use key to access value
# Update Value
person["age"] += 1 # update age by one year
print(person) 
# Methods
# Iterable -> List, Tuple, dict_keys
# access keys
print(person.keys(), type(person.keys()))
# access values
print(person.values()) 
print(person.items()) # key value pairs (tuples)

# Loop

for detail in person.items():
  print(detail) # all items
  print(detail[0]) # only keys
  print(detail[1]) # only values

for key, value in person.items():
  print(key, value)


