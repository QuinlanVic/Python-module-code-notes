# marks = [98, 75, 40, 45, 80, 60]
# print(type(marks))
# # marks.pop() # remove the last value from the array
# print(marks)
# print(marks[:-3]) # does not mutate the list
# print(len(marks))
# # print(marks.pop(-3)) # mutates the list
# print(marks)

# marks = [98, 75, 40, 45, 80, 60]
# marks.remove(40) # mutates the list (remove specific value) (not index)
# print(marks)

# eng = 88
# marks.append(eng) # mutates the list (adds to the end)
# print(marks)

# sci = 85
# marks.insert(2, sci) # add at specific position/index in list
# print(marks)

# [5, 6] * 2 -> [5, 6, 5, 6] (Duplicate list)
# price_list1 = [1000, 1500, 400]
# price_list2 = [2000, 500]

# price_list3 = price_list1 + price_list2
# print(price_list3)
# print(price_list1 + price_list2) # does not mutate list
# print(price_list1, price_list2)

# price_list1_copy = price_list1
# price_list1_copy.append(600)
# price_list1.append(700)
# print(price_list1, price_list1_copy)

# price_list1 = stores the memory address of the first item in the list (e.g. 456)
# 456 + 0 = first list item mem addr.
# 456 + 1 = second list item mem addr.
# 456 + 2 = third list item mem addr.

# Slice -> copy
price_list = [1000, 1500, 400]
price_list2 = price_list[:]
# price_list2 = price_list.copy()

price_list2.append(600)
price_list.append(700)
print(price_list, price_list2)
print(id(price_list), id(price_list2))

subjects = ["maths", "science", "eng"]
print(", ".join(subjects))  # returns a string

subjects.sort()  # mutates list (sorts in place)
print(subjects)
subjects.sort(reverse=True)
print(subjects)
