# Exercise: Event Registration System
# SDDA - 23 february 2024
# By: Quinlan Caiger
eventlist = [{"name": "John", "email": "John@gmail.com", 
  "meal_preference": "non-vegetarian", "needs_accomodation": True}
]
  
def register_par(name, email = "unknown@gmail.com", 
                 meal_preference = "non-vegetarian", needs_accomodation = False):
  newparticipant = {"name": name, "email": email, "meal_preference": meal_preference,
                   "needs_accomodation": needs_accomodation} 
  eventlist.append(newparticipant)
  return newparticipant
print("List before:")
print(eventlist)
print("New participants:")
print(register_par("Emma", "Emma@gmail.com", meal_preference="vegetarian"))
print(register_par("Lutho", "L99@gmail.com", needs_accomodation=True))
print(register_par("Steven", "Steve@gmail.com"))
print(register_par("Jemima", meal_preference="vegetarian", needs_accomodation=True))
print("List after")
print(eventlist)
  
  
  