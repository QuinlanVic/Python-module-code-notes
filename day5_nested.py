from pprint import pprint
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

def find_avg(nums):
  return sum(nums)/len(nums)

# Find average of each class
# Task 1
# output = { # 2 decimal places
#   "Class A": 82.53,
#   "Class B": 85.5
# }

# My first solution
# finalaverages = []
# for key, value in classes.items(): # ".items()"!!!!!!!!!!!
#   averageforclasslist = []
#   for person in value:
#     averageforclasslist.append(sum(person["grades"])/len(person["grades"]))
#   finalaverages.append(sum(averageforclasslist)/len(averageforclasslist))
#   print(averageforclasslist)
# print(finalaverages)
# averagesdict = {"Class A": round(finalaverages[0], 2), "Class B": round(finalaverages[1], 2)}
# print(averagesdict)

# Better version (Rashay)
output = {}
for key, value in classes.items():
  total = 0
  for student in value:
    total+= sum(student["grades"])/len(student["grades"])
  ans = float(f"{total/len(value):.2f}")
  output = {**output, key: ans}
pprint(output)

# Class solution
classes_avg = {}
for classname, students in classes.items():
  class_student_avg = [] # resets with each classroom
  for student in students:
    class_student_avg.append(find_avg(student['grades']))
  # print(classname, sum(class_student_avg) / len(students))
  classes_avg[classname] = round(find_avg(class_student_avg), 2)
print(classes_avg) 

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

finaloutput = {}
for classname, students in classes.items():
  averagesofstudents = {}
  for student in students:
    averagesofstudents = {**averagesofstudents, student["name"]: round(find_avg(student['grades']), 2)}
  finaloutput = {**finaloutput, classname: averagesofstudents}
pprint(finaloutput)

# Class solution
print("Class solution")
students_avg_dict = {}
for cls_name, students in classes.items():
  students_dict = {}
  for student in students:
    studentname = student['name']
    studentavg = find_avg(student['grades'])
    # print("inner", studentname, studentavg)
    # put into dicitonary
    students_dict[studentname] = round(studentavg, 2)
  # print("outer", students_dict)
  students_avg_dict[cls_name] = students_dict
pprint(students_avg_dict)

# Task 3
# Task 1 + comprehension
# Class solution
print("Task 3")
print("Level 1")
classes_avg = {}
for classname, students in classes.items():
  # resets with each classroom
  class_student_avg = [find_avg(student['grades']) for student in students]
  classes_avg[classname] = round(find_avg(class_student_avg), 2)
print(classes_avg) 

print("Level 1.5")
classes_avg = {}
for classname, students in classes.items():
  # resets with each classroom
  # class_student_avg = [find_avg(student['grades']) for student in students]
  classes_avg[classname] = round(find_avg([find_avg(student['grades']) for student in students]), 2)
print(classes_avg) 

print("Level 2")
# classes_avg = {}
# for classname, students in classes.items():
  # resets with each classroom
  # class_student_avg = [find_avg(student['grades']) for student in students]
  # classes_avg[classname] = round(find_avg([find_avg(student['grades']) for student in students]), 2)
classes_avg = {classname: round(find_avg([find_avg(student['grades']) for student in students]), 2) for classname, students in classes.items()}
print(classes_avg) 

# Task 4
# Task 2 + comprehension
print("Task 4")
print("Level 1")
students_avg_dict = {}
for cls_name, students in classes.items():
  # students_dict = {}
  students_dict = {student['name']: round(find_avg(student['grades']), 2) for student in students}
  students_avg_dict[cls_name] = students_dict
pprint(students_avg_dict)

print("Level 1.5")
students_avg_dict = {}
for cls_name, students in classes.items():
  # students_dict = {}
  # students_dict = {student['name']: round(find_avg(student['grades']), 2) for student in students}
  students_avg_dict[cls_name] = {student['name']: round(find_avg(student['grades']), 2) 
                                 for student in students}
pprint(students_avg_dict)

print("Level 2")
# students_avg_dict = {}
# for cls_name, students in classes.items():
students_avg_dict = { cls_name: {student['name']: round(find_avg(student['grades']), 2) 
                                 for student in students} for cls_name, students in classes.items()
                                }
pprint(students_avg_dict)

# Debug in vs code python -> F5 and python debugger