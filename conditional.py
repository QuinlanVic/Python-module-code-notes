# lexical order

person1 = input("Please give your name? ")
height1 = int(input("Provide your height in cm: "))
person2 = input("Please give your name? ")
height2 = int(input("Provide your height in cm: "))

# 166 > 166
# if (height1 > height2):
#   print(f"{person1} is taller")
# else:
#   print(f"{person2} is taller")

if (height1 > height2):
  print(f"{person1} is taller")
elif (height1 == height2):
  print(f"{person1} is the same height as {person2}")
else:
  print(f"{person2} is taller")