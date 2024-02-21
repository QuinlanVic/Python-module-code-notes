# i = 0
# while i < 3:
#   print(i)
#   i += 1
# ctrl + d -> multicursor (grab each occurence of the ting)
# j = 0
# rows = int(input("How many rows would you like? "))
# while j < rows:
#   print("😍" * (j+1))
#   j += 1 # j = j + 1

# for curr in range(3):
#   print(curr)
# print("")
# for curr in range(1, 3):
#   print(curr)
# print("")
# for curr in range (0, 25, 2):
#   print(curr)

# rows2 = int(input("How many rows would you like? "))
# for k in range(rows2):
#   print("😍" * (k + 1))
#   k += 1

# # Task
player_stats = [10, 30, 60]
# player_stats_dbl = player_stats.copy()
# for i in range(len(player_stats_dbl)):
#   # player_stats_dbl[i] = player_stats_dbl[i] * 2
#   player_stats_dbl[i] *= 2
# print("Power Up:", player_stats_dbl, player_stats)

# for x in player_stats:
#   print(x)  # prints each value in the list

# List comprehension!!!!!!!!!!!!!!!!!!!
# creates a copy (does not mutate original list)
powered_up_stats = [stat for stat in player_stats]  
print(powered_up_stats)

powered_up_stats = [stat * 2 for stat in player_stats]  # creates a copy
print(powered_up_stats, player_stats)

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]

leneachword = [len(super) for super in avengers]
print(leneachword)

# give me superheros with more than 10 chars
# ["Black widow", "Captain america"]
leneachword = [len(super) for super in avengers]
print(leneachword)

avengerslong = []
for i in avengers:
  if len(i) > 10:
    avengerslong.append(i)
print(avengerslong)

# make in one line? -> LIST COMPREHENSION
filtered_names = [avenger for avenger in avengers if len(avenger) > 10]
filtered_names_upper = [avenger.upper() for avenger in avengers if len(avenger) > 10]
print(filtered_names, filtered_names_upper)

