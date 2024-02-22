library = [
    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Advance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]


# Task 1
# add_book function (library, newbook) -> adds new book to library
# def add_book (library2, newbook):
#   library2.append(newbook) #does not return, changes og
#   print(library2)
# newbookentry = {"title": "Programming Elm", "author": "Jeremy Fairbanks", "year": 2019, "available": True}
# not passing a copy 
# add_book(library, newbookentry) 
# updates original list (pass parameter by reference)
# add_book(*library, newbookentry) # pass a copy (pass by value) (will not change original)


# Task 2
# books_by_author (library, authorname) -> give all books they have written
# E.g., Mark Lutz -> [ ]
def search_by_author (library3, authorname):
  # pass # can declare function and call it without error before defining
  # booksbyauthor = []
  # for book in library:
  #   if book["author"] == authorname:
  #     booksbyauthor.append(book)
  # booksbyauthor = [book for book in library3 if book["author"] == authorname]
  # return booksbyauthor
  return [book for book in library3 if book["author"] == authorname]
# print("Task 2")
# print(search_by_author(library, "Mark Lutz"))
# print(search_by_author(library, "Eric Matthes"))
# print(search_by_author(library, "Mark Lut"))

# Task 3
# Check out book function: marks books as not available if it exists and is available
print("Task 3")

# def check_out_book(library4, title):
#   # exists = False
#   for book in library4:
#     if book["title"] == title:
#       print("books exists")
#       # exists = True
#       if book["available"] is True:
#         print("Book is available and has been checked out")
#         book["available"] = False #change availability to False
#       else:
#         print("Book is not available")
#       break
#   # if (not exists):
#   else:
#     print("Book does not exist")

# check_out_book(library, "Hello")
# check_out_book(library, "Advance Python")
# check_out_book(library, "Fluent Python")

def check_out_book1(library4, title):
  # exists = False
  for book in library4:
    if book["title"] == title:
      print(f"{title} exists")
      # exists = True
      if book["available"]:
        book["available"] = False #change availability to False
        return f"{title} is available and has been checked out"
      else:
        return f"{title} is not available"
  return f"{title} does not exist"

print("Library before")
print(library)
print(check_out_book1(library, "Hello"))
print(check_out_book1(library, "Advance Python"))
print(check_out_book1(library, "Fluent Python"))
print("Library after")
print(library)
print("Fluent Python should not be available now")
print(check_out_book1(library, "Fluent Python"))
print(library)

# def check_out_book(library4, title):
#   for book in library4:
#     if book["title"] == title and book["available"]: # is True is not necessary 
#       # book['available'] returns bool
#         book["available"] = False #change availability to False
#         return f"Yes, {title} is available and has been checked out :)"
#   # Return breaks from the for loop, if it does not then book is unavailable
#   return f"{title} is unavailable"

# print(check_out_book(library, "Hello"))
# print(check_out_book(library, "Advance Python"))
# print(check_out_book(library, "Fluent Python"))
# print(library)
# print(check_out_book(library, "Fluent Python"))
# print(library)

# Dictionary - Not a Sequence | It is Iterable

