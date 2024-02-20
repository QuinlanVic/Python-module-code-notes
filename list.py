# marks = [98, 75, 40, 45, 80, 60]
# print(type(marks))
# # marks.pop() # take the last value from the array
# print(marks)
# print(marks[:-3]) # does not mutate the list
# print(len(marks))
# # print(marks.pop(-3)) # mutates the list
# print(marks)

marks = [98, 75, 40, 45, 80, 60]
marks.remove(40) # mutates the list
print(marks)

eng = 88
marks.append(eng) # mutates the list (adds to the end)
print(marks)

sci = 85
marks.insert(2, sci)
print(marks)

# [5, 6] * 2 -> [5, 6, 5, 6]
price_list1 = [1000, 1500, 400]
price_list2 = [2000, 500]

# price_list3 = price_list1 + price_list2 
# print(price_list3)
print(price_list1 + price_list2) # does not mutate list
print(price_list1, price_list2)