# Exercise: Hotel Room Booking System
# SDDA - 23 february 2024
# By: Quinlan Caiger
hotelrooms = [{"room_number": 5, "bed_type": "Single", 
               "smoking": True, "availability": True},
              {"room_number": 6, "bed_type": "Single", 
                 "smoking": False, "availability": False}, 
              {"room_number": 7, "bed_type": "Double", 
                 "smoking": True, "availability": False},
              {"room_number": 8, "bed_type": "Single", 
                 "smoking": False, "availability": True},
              {"room_number": 9, "bed_type": "Double", 
                 "smoking": False, "availability": True}
             ]
print("Below are the current hotel rooms:")
print(hotelrooms)
# Task 1
# default values if parameters not supplied
def add_room(rooms, room_number, bed_type="Double", smoking=False):
  # default availability to True since it's a new room 
  newroomtoadd = {"room_number": room_number, "bed_type": bed_type, 
                  "smoking": smoking, "availability": True}
  rooms.append(newroomtoadd)
  return "New room has been created"

print("") # break up prints
print(add_room(hotelrooms, 10, "Double", False))
print(hotelrooms)

# Task 2
# default values if parameters not supplied
def book_room(rooms, preferred_bed_type="Double", smoking_preference=False):
  for room in rooms:
    if room["bed_type"] == preferred_bed_type and room["smoking"] == smoking_preference and room["availability"]:
      room["availability"] = False
      return "A preferred room is available"
  return "No room with your preferences is available"

# I want a single bed with no smoking
print("") # break up prints
print(book_room(hotelrooms, "Single", False))
print(hotelrooms)

# Task 3
def list_available_rooms(rooms):
  # availablerooms = []
  # for room in rooms:
  #   if room["availability"]:
  #     availablerooms.append(room)
  # return availablerooms
  
  # List Comprehension way!
  return [room for room in rooms if room['availability']]

print("") # break up prints
print("Below is the list of currently available rooms:")
print(list_available_rooms(hotelrooms))
  