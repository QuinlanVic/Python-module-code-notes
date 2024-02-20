msg = "Hi, all"
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())

quote = "         Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote.strip()) # strip off from beginning and end (not inbetween)

quote1 = "----Dream is not something that you see in sleep, Dream is something that does not let you sleep----"
print(quote1.strip("-"))
print(quote1.lstrip("-"))
print(quote1.rstrip("-"))

quote3 = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote3.find("something")) # returns the index of the first match
print(quote3.find("Dream")) # returns the index of the first match