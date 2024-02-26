from math import pi

from datetime import datetime

now = datetime.now()
print(now)
print(f"The current date is: {now:%d-%m-%Y}")
print(f"The current date is: {now:%d/%m/%Y}")
print(f"The current date is: {now:%d %b %y}")

# numeric separator
salary = 420_000  # python ignores underscores for us :)
print(salary)  # DX improves (readability)

# Number formatting (only these 2 can sepera)
print(f"Dhara's salary is R{salary:,}")
print(f"Dhara's salary is R{salary:_}")

# Float formatting
print(f"The PI value is: {pi:.2f}")  # f denotes it's a floating point number
print(f"The PI value is: {pi:.3f}")  # 3 decimals
print(f"The PI value is: {round(pi)}") # just 3

# text formatting
name = "Lilitha"
person = "Quinlan"

# Padding
# add 20 spaces to the left
print(f"{name:>20}:")
# add 20 spaces to the right
print(f"{name:<20}:")
# add 20 spaces to the left
print(f"{name:^20}")
# Add symbols to padd
print(f"{person:*>20}:")
print(f"{person:#<20}:")
print(f"{person:$^20}:")

caleb = 0.925
# % symbol indicates that it is a percentage!
print(f"The test results are out and Caleb got {caleb:.2%}")

# Multi line - keeps same format
about_me = """
Hi, my name is Quinlan and i am feeling ok hehe slay :) I am not sure when it will cut off onto the next line so I will keep typing until I cry hehe. I am glad I passed lol, yoh that was scary omfg. I hope I never fail because yoh that's crazy. 70%? Hebana bruh 
"""
print(about_me)

# Can use f string with triple quote strings!
about_me2 = f"""
Hi, Caleb's percentage is {caleb}. 
"""