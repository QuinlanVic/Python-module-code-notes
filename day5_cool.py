# utility functions
# doc string
def to_uppercase(text):
  return text.upper()

def to_lowercase(text):
  return text.lower()

help(to_uppercase) # tells you about this method (press "q" to get out of this)

# Anything you want to execute only in this file you put it into this if statement
# dunder variables "__variable__"
if (__name__ == "__main__"): # true in this file
  print(__name__, type(__name__)) # prints ("__main__")
  print(to_uppercase("Quinlan"))