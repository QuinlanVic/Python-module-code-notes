# a = 10
# b = 10
# c = 10

#multiple variable assignment
# a = b = c = 10 
# print (a, b, c)

# Lilitha, Dhara, Quinlan = "Chocolate", "Lime", "Vanilla"
# print(Lilitha, Dhara, Quinlan)

# movies = ["Remember the Titans", "Juno", "Lucy"]

# caleb, gemma, yolanda = movies
# print(gemma) 

# t1, t2, t3 = [100, 200, 300, 400] # error = too many values to unpack
# t1, t2, t3, _ = [100, 200, 300, 400]
# print(t1, t2, t3) # _ -> skip (ignore) [wildcard character]

# t1, t2, *t3 = [100, 200, 300, 400, 60, 40, 30] # "*" = unpacking operator -> (list) 
# print(t1, t2, t3) 

# t1, t2, *t3 = (100, 200, 300, 400, 60, 40, 30) # "*" = unpacking operator -> (list again) 
# print(t1, t2, t3)

# Task 1
coordinates = [(5, 4), (1,1), (6, 10), (9, 10)] # list of tuples (int)
# Origin (0, 0)
import math
distlist = []
for coord in coordinates:
  # print(coord[0]**2 + coord[1]**2)
  distlist.append(math.sqrt(coord[0]**2 + coord[1]**2)) 
print(distlist)

# Task 2 use unpacking
import math
distlist = []
for x, y in coordinates:
  # print(x**2 + y**2)
  distlist.append(math.sqrt(x**2 + y**2)) 
print(distlist)

# Task 3 - use unpacking and list comprehension
lengths = [math.sqrt(x**2 + y**2) for x, y in coordinates]
print(lengths)


