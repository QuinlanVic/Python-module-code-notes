# from flask import Flask
# app = Flask('app')
# @app.route('/')
# def hello_world():
#   return 'Hello, World!'
# app.run(host='0.0.0.0', port=8080)

#Declaration
# name = "Gemma"

# print(name)
# print("Hello my name is " + name)

# name = input("What is my name? ")
# print("Hello my name is " + name)

# Task -> Farenheit to Celsius
# farenheit = input("Please input a farenheit temperature: ")
# celsius = (float(farenheit) - 32) * 5/9
# print("The converted temperature in celsius is " + str(celsius))

# f = input("Please provide your Farenheit: ")
# print(f, type(f))
# c = (float(f) - 32) * 5 / 9
# print("The " + f + "°F is " + str(c) + "°C") # difficult readability

# DX = Developer's Experience
# print(f"The {f}°F is {c}°C") # more easily readable
# {} = Interpolation
# f = f string

# Find the age of the person if the birth age is given e.g. 2000 = 24
import datetime

birth_year = input("What year were you born? ")
currentyear = datetime.date.today().year
age = currentyear - int(birth_year)

print(
    f"The current year is {currentyear} - the year you were born which is {birth_year}, so your current age is {age}"
)

# print(f"Your age is {currentyear} - int(birth_year)")

# Area of the circle
# import math
# radius = input("Please enter the radius of the circle: ")
# # area = math.pi * float(radius) ** 2
# print(f"The radius you input is {radius} and the area of the circle is {math.pi * float(radius) * float(radius)}")

# Input: 70
# per = int(input("Please enter the percentage: "))
# eq = per // 10
# print(f"Output: [{('=' * eq) + ' ' * (10 - eq)}] {per}%")

quote = "I love python"
print(quote[0])
print(quote[2])
# quote[2] = "x" # error (string literals are immutable)
print(quote.upper())
print(quote)

# Slicing operator
print(quote[2:6])  # love
print(quote[7:])  # python
print(quote[-6:])  # python
#skip in slice of string
print(quote[0:6:2])  # start:end:incrementor
#skip
print(quote[::3])
# reverse
print(quote[::-1])
