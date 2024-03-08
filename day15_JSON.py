import json
from pprint import pprint

data = {
    "employees": [
        {"name": "Alice", "age": 30, "department": "Sales"},
        {"name": "Bob", "age": 25, "department": "Marketing"},
    ]
}

print(type(data))
# get age of Alice
print(data["employees"][0]["age"])

# Convert Dictionary to JSON = JavaScipt Object Notation
# pretty print with indent 4
data_json = json.dumps(data, indent=4)
# It's a string (multi-line)
print(type(data_json))
print(data_json)

# cannot access data values with dict logic as it is a string
# print(data_json["employees"]) # Error ❌

# Valid syntax as funtions are treated as first-class citizens (same as value)
sport = {"name": "Dhoni", "dbl": lambda x: x * 2}  # Valid Dictionary

print(sport["dbl"](100))

# Will give error as a function cannot be inside a string
# Not JSON serializable (converting) | Cannot convert Dictionary to JSON as it contains a function
# sport_json = json.dumps(sport)
# print(sport_json) # Invalid JSON

student_json = """
    {
        "name": "gemma",
        "gender": "female"
    }
"""

print(student_json)

# Convert from JSON multi string object
student = json.loads(student_json)
print(type(student))
print(student["name"])

bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""
# All Active users' balance should increased by 10%
# Final Output in JSON format
# convert to a list
bank_data_list = json.loads(bank_data)
print(type(bank_data_list))

# for account in bank_data_list:
#     if account["isActive"]:
#         account["balance"] += account["balance"] * 0.1
# print("Updated list version of bank data")
# pprint(bank_data_list)

# easy to put into a file
# bank_accounts_json = json.dumps(bank_data_list, indent=4)
# print("JSON string")
# print(bank_accounts_json)
# does nothing extra as it is a string unless you use indent=4 (only pretty prints )
# pprint(bank_accounts_json)

# OR

bank_data_updated = [
    (
        {**account, "balance": account["balance"] + (account["balance"] * 0.1)}
        if account["isActive"]
        else account
    )
    for account in bank_data_list
]
pprint(bank_data_updated)
# Convert list into a JSON multi-line strng
# indent 4 = prints each one with 4 spaces from left (1 tab indent)
bank_data_json = json.dumps(bank_data_updated, indent=4)
print(type(bank_data_json))
print(bank_data_json)

# create a file
# "with" closes files silently for you if there are any errors
# filename, write command
# Write a file
with open("bank_accounts.json", "w") as file:
    # "dump" not "dumps" as it is creating a file
    json.dump(bank_data_updated, file, indent=4)

# Read a file
with open("bank_accounts.json", "r") as file:
    # "load" to load a file
    data = json.load(file)
    print(data, type(data))

# Read blog_post.json
with open("blog_post.json", "r") as file:
    # load the file
    blog_post_data = json.load(file)
    print(blog_post_data, type(blog_post_data))

# change data to summary of posts
post_summary = {}
post_list = []
for post in blog_post_data["posts"]:
    post_summary["posts_summary"] = post_list.append(post_summary["posts_summary"])

# write a file
with open("posts_summary.json", "w") as file:
    # dump the file as json
    json.dump(post_summary, file, indent=4)

# Expected Output
# {
#   "posts_summary": [
#     {
#       "title": "The Future of AI",
#       "author": "Alice",
#       "number_of_comments": 2
#     },
#     {
#       "title": "Learning Python",
#       "author": "Bob",
#       "number_of_comments": 1
#     },
#     {
#       "title": "Web Development Trends",
#       "author": "Charlie",
#       "number_of_comments": 0
#     }
#   ]
# }
