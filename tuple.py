# tuple vs list
# tuples are Immutable!!!! | lists are mutable!!!!
person = ("Alex", "SA", 20) 
print(person, type(person))
# person[0] = "Thato" # Error

print(person.count(20)) # counts occurrences of value
print(person.index("Alex")) # gets index of value
# issue with index
# print(person.index(80)) # gives error if not found | find gives -1 if not found