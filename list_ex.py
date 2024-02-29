scrambled_message = "world the save to time no is there"
newmessage = scrambled_message.split(" ")  # convert string into list
# print(newmessage)
# newmessage.sort(reverse=True) # not reverse sort (NOT ALPHABETICAL) (don't want asc/desc, want switch around)
# print(newmessage[::-1]) # reverse the list (BY INDEX)
# print(scrambled_message.sort())
# join all of the list items to print out final string
print((" ").join(newmessage[::-1]))
