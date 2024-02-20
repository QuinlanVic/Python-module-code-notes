# msg = "Hi, all"
# print(msg.upper())
# print(msg.lower())
# print(msg.title())
# print(msg.capitalize())

quote = "         Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote.strip()) # strip off from beginning and end (not inbetween)

quote1 = "----Dream is not something that you see in sleep, Dream is something that does not let you sleep----"
print(quote1.strip("-"))
print(quote1.lstrip("-"))
print(quote1.rstrip("-"))

quote3 = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote3.find("something")) # returns the index of the first match 
print(quote3.find("Dream")) # returns the index of the first match
print(quote3.find("**")) # (-1 if it cannot find it)

# Replace method
print(quote3.replace("Dream", "🛌")) # returns a new string to print
print(quote3) # immutable (does not change)

# Case sensitive
print(quote3.count("Dream"))
print(quote3.count("o"))

print(quote3.startswith("Dream")) # True
print(quote3.endswith("sleep")) # True
# print(quote3.endswith("Dream is not something that you see in sleep, Dream is something that does not let you sleep")) # True (" sleep" and "p" also return true)

badge_no = "45445"
print(badge_no.isdigit())

name = "ark"
print(name.islower())

print(len(name))
