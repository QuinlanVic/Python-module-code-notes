movies = [
  {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
  {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
  {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
  {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
  {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]

# Task 1 - Find average for all - map, filter, all, ...
# Dont use for loop or List comp
print("Task 1")
titles = map(lambda x: x["title"], movies)
print(list(titles))

print("Task 1.1")
averageratings = map(lambda x: sum(x["ratings"])/len(x["ratings"]), movies)
print(list(averageratings))

print("Task 1.2")
averageratingsaddition = list(map(lambda x: {**x, "average_rating": sum(x["ratings"])/len(x["ratings"])}, movies))
print(averageratingsaddition)
# or create def
def find_avg(movie):
  return sum(movie["ratings"])/len(movie["ratings"])
print("Task 1.2 again")
averageratingsaddition = list(map(lambda x: {**x, "average_rating": find_avg(x)}, movies))
print(averageratingsaddition)
# print(type(averageratingsaddition))

print("Task 2")
# toprated = max(movies, key=(lambda movie: movie["ratings"]))
toprated = max(averageratingsaddition, key=(lambda movie: movie["average_rating"]))
print(f"The top rated movie is '{toprated['title']}'")

print("Task 3")
# Movies with ratings more than or equal to 4.6
# output = ['Inception', 'Interstellar', 'The Dark Knight']
highlyratedmovies = list(filter(lambda movie: movie["average_rating"] >= 4.6, averageratingsaddition))
# filter does not change the data type
print(list(map(lambda movie: movie["title"], highlyratedmovies)))

# Task 4
# movie names in order of rating
# ['The Dark Knight', 'Inception', 'Interstellar', 'Memento', 'Dunkirk']
ratingordered = sorted(averageratingsaddition, key=lambda movie: movie["average_rating"], reverse=True)
# print(type(ratingordered))
print(list(map(lambda movie: movie["title"], ratingordered)))