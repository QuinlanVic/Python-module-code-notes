from math import pi

from datetime import datetime

now = datetime.now()
print(now)
print(f"The current date is: {now:%d-%m-%Y}")
print(f"The current date is: {now:%d/%m/%Y}")
print(f"The current date is: {now:%d %b %y}")

salary = 420_000  # pytho ignores underscores for us :)
print(salary)  # DX improves (readability)

# Number formatting
print(f"Dhara's salary is R{salary:,}")
print(f"Dhara's salary is R{salary:_}")

# Float formatting
print(f"The PI value is: {pi:.2f}")  # f denotes it's a floating point number
print(f"The PI value is: {pi:.3f}")  # 3 decimals
print(f"The PI value is: {round(pi)}")

# text formatting
name = "Lilitha"
person = "Quinlan"
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
