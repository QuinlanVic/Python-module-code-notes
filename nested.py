classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]}
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]}
    ]
}

# Find average of each class
# Task 1
# output = { # 2 decimal places
#   "Class A": 82.53,
#   "Class B": 85.5
# }
averageforclasslist = []
finalaverages = []
for classroom in classes:
  for person in classroom:
    averageforclasslist.append(sum(person["grades"]) / len(person["grades"]))
  finalaverages.append()

# Task 2
# Student name's unique
# output each student and their average
# output = {
#   "Class A": {
#     "Alice": 90.5,
#     "Bob": 84.5,
#     "Charlie": 90
#   },
#   "Class B": {
#     "Dave": 92.5,
#     "Eve": 86.5,
#     "frank": 95
#   }
# }
averageforeachperson = {} 
for classroom in classes:
  for person in classroom:
    averageforclasslist.append(sum(person["grades"]) / len(person["grades"]))