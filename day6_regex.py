import re

# Regex -> Regular Expression

# Pattern match in a string

numbers = """
387954, 4985048584, 098305843, 987077540545, 9348584854545
387954, 4985048584, 098305843, 487077540545, 488584854545
"""

# Theey have 16 digits
# Start with 4

# [487077540545, 488584854545]

quote = "To be or not to be"

# r - raw
is_be = re.search(r"be$", quote)
# returns a re.Match object (None if no matches (falsy values))
output = "Present and end with be" if is_be else "Not present"

print(is_be, type(is_be))
print(output)

print(re.search(r"^Hello", "Hello World!").group(0))  # Hello

# findall matches all cases and returns them in a list
# [] = character set (or), {} = exactly 2 (gives repetition range)
quote1 = "funny funy funnnny fuzzy"
find_be = re.findall(r"fu[nz]{2}y", quote1)  # returns a list
print(find_be)

# 1. search
# 2. findAll
# 3. sub

text = "This \\ that \\ those"
# have to escape \ with another \
matches = re.findall("\\\\", text)
# or use "r" string without having to escape
matches_r = re.findall(r"\\", text)
print(matches)
print(matches_r)

tweet = "Spoiler: This movie is great, but the spoiler was unexpected. Avoid sharing spoilers!"

# *****
# Alternatives (|) - gets either "spoiler" or "but" (whole group)
censor_tweet = re.sub(r"(spoiler|but)", "*" * 7, tweet, flags=re.IGNORECASE)
print(censor_tweet)

list_websites = "facebook.com, google.com, twitter.in, amazon.com"
# result = re.sub(r'(\w+)\.com$', 'blacklist.com', list_websites)
# any alphaneumeric char
result = re.sub(r"(\w+)(\.com)", r"\1.subdomain\2", list_websites)
print(result)

# Using search with groups to group things
# result2 = re.search(r'(\w+)(\.com)', list_websites)
# print(result2.groups())

names = ["John    Doe  ", "Jane     Smith", "Alice      Johnson", "Chris   Evans  "]

output = ["Doe, John", "Smith, Jane", "Johnson, Alice", "Evans, Chris"]

# get rid of spaces on ends and replace first group with second
# split string into different parts and then group what you want and replace!
# "\s" accounts for spaces and newlines
# re.sub returns a string which is built up in the sortednames list using comprehension
sortednames = [re.sub(r"\s*(\w+)\s+(\w+)\s*", r"\2, \1", name) for name in names]
print(sortednames)

# Rashay's output
# output = [re.sub(r'\s*(\w+)\s+(\w+)\s*',r'\2, \1', name) for name in names]

# print(switched_names)


# Assignment
post = "Loving the #sunny weather in #California. #travel #fun"
# "#" + alphaneumonic characters
hashtags = re.findall("#\w+", post)
print(hashtags)

# Output
["#sunny", "#California", "#travel", "#fun"]

# Classes

# Open terminal -> ctrl + ~
# Virtual Environment (fix code breaks with time and updates in new versions)
# python --version -> 3.10.8
# code then = print(f"abc [abc]")
# python --version -> 3.14.1 (In 3 years time)
# code now = print(f"abc [abc]") # breaking change

# WINDOWS (powershell)
# command = python -m venv myenv
# myenv -> copy of python
# .\myenv\Scripts\Activate.ps1 -> activate my environment -> python -> point to local copy of python
# (myenv/Scripts/python.exe) = local python version
# Now you can run any of your python files :)
# deactivate -> python -> point to global python installed

# Docker creates virtual OS/hypervisor for client machines to be able to successfully use your application
# Ship containers like shipyards

# ctrl + ~ -> Open/Close Terminal
