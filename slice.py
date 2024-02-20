# String literal | Immutable (Cannot change)
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