# String, List, Tuple, Dictionary, Sets
# Sets - Mutable but only has unique values
# No order [No guarantee]

# {}
tech_gadgets = {'Smartphone', 'Laptop', 'Smartwatch', 'Tablet'}
# doesn't add duplicate
# tech_gadgets2 = {'Smartphone', 'Laptop', 'Smartwatch', 'Tablet', 'Tablet'} 
tech_gadgets_list = ['Smartphone', 'Laptop', 'Smartwatch', 'Tablet']
print(tech_gadgets, type(tech_gadgets))
# print(tech_gadgets2)
print(tech_gadgets_list)

# don't know position it will be added
tech_gadgets.add('E-reader')
print(tech_gadgets)

more_gadgets = ['Drone', 'Selfiestick']
tech_gadgets.update(more_gadgets)
print(tech_gadgets)
tech_gadgets.discard('Drone') #does not give error if not found (safer, does nothing)
# tech_gadgets.remove('g') # KeyError if not in set 
print(tech_gadgets)

# x = {} # empty dictionary
# Use set constructor!
# empty_set = set()
# print(empty_set)
# empty_set.add('Quinlan')
# print(empty_set)
# print(type(empty_set))

outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}

print("Intersection")
print(indoor_activities.intersection(outdoor_activities))
print("Union")
print(indoor_activities.union(outdoor_activities))
# Different perspectives
print("Difference")
print(indoor_activities.difference(outdoor_activities)) # {'Gaming', 'Reading'}
print(outdoor_activities.difference(indoor_activities)) # {'Swimming', 'Hiking'}

# opposite of intersection
print("Symmetric difference")
print(indoor_activities.symmetric_difference(outdoor_activities))

colors = ["red", "blue", "red", "green", "pink", "blue"]
# Task 1 = Hard way
unique = set()
for color in colors:
  unique.add(color)
print(unique)

# Task 2 = Easy way
uniquecolors = set(colors)
print(uniquecolors)

# Covert set to list
# Use list constructor!
print(list(uniquecolors))
# ONE LINE!!!!!!!!!!!!!!!!!
print(list(set(colors)))
# ["red", "blue", "green", "pink"]


outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}

# Task 1
# Which are outdoor_gadgets?
# {'Smartwatch', 'Drone'}
# outdoor_gadgets = set()
# for (key, value) in activity_gadgets.items():
#   if value in outdoor_activities:
#     outdoor_gadgets.add(key)
# print(outdoor_gadgets)
# List comprehension!
# print("List comprehension way")
outdoor_gadgets2 = {key for key, value in activity_gadgets.items() if value in outdoor_activities}
print("Outdoor gadgets:", outdoor_gadgets2)

    

# Task 2
# Which are indoor_gadgets?
# {'VR Headset', 'Smartphone'}
# indoor_gadgets = set()
# for (key, value) in activity_gadgets.items():
#   if value in indoor_activities:
#     indoor_gadgets.add(key)
# print(indoor_gadgets)
# List comprehension!
# print("List comprehension way")
indoor_gadgets2 = {key for key, value in activity_gadgets.items() if value in indoor_activities}
print("Indoor gadgets:", indoor_gadgets2)

# Task 3 - DRY | Concept of today (function?)
def gadgettype (act_gadgets, type_activities):
  # type_gadgets = set()
  # for (key, value) in act_gadgets.items():
  #   if value in type_activities:
  #     type_gadgets.add(key)
  # return type_gadgets
  # List comprehension way
  # print("List comprehension way")
  return {key for key, value in act_gadgets.items() if value in type_activities} 
print("Function approach")
print("Indoor gadgets:", gadgettype(activity_gadgets, outdoor_activities))
print("Outdoor gadgets:", gadgettype(activity_gadgets, indoor_activities))

  