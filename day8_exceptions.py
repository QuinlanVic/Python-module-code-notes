from datetime import datetime


def math_divide(n1, n2):
    try:
        result = n1 / n2
        print(f"The answer is {result}")
    except ZeroDivisionError:
        # When error happens
        print("You cannot divide by zero! 💀")
    else:
        # When no error
        print("Division was successful ✅")
    finally:
        # Runs no matter what
        # Usually to run cleanup code
        print("Operation done 😷✌️")


# Example 2
def math_divide2(num1, num2):
    try:
        print(f"Result is: {num1 / num2}")
    except ZeroDivisionError:
        print("You cannot divide by zero bro")
    else:
        print("Diviion was successful")
    finally:
        # Runs no matter what hehe
        print("Operation done!")


# Example 3
# Runtime Errors
def calculate_age():
    # Task 2
    try:
        # Task 1
        birth_year = int(input("Please tell me your year of birth: "))
        curryear = datetime.now().year
        if birth_year <= 0:
            # print("Year cannot be negative or zero")
            # raise -> Stops further execution and passes string to "e" in "except" block
            raise ValueError("Year cannot be negative or zero")
        if birth_year > curryear:
            # print("You cannot be from the future")
            raise ValueError("You cannot be from the future")
        # else:
        # Now you don't need elif and else now
        # Code is shielded
        print(f"Your age is {curryear - birth_year}")

    # value error - ValueError: invalid literal for int() with base 10: '"age"'
    # use alias to print exception string
    except ValueError as e:
        print("That value is not of a valid type")
        print("Invalid number: ", e)
    # catch all exceptions
    except Exception as err:
        print("This is a catch all error: ", err)
    # not mandatory to have "else" and "finally" blocks
    else:
        print("Successful age input!")
    finally:
        print("Age operation done :)")


# custom Error creation to handle logic errors
# Inherit from Exception
class NegativeNumberError(Exception):
    """Raised when the input value is negative"""

    # value is negative number input and we define a custom message
    def __init__(self, value):
        self.value = value
        self.message = "Negative numbers are not allowed"
        # here we create instance of class using base method, giving it extra message var
        super().__init__(self.message)

    # Override print() for base class of Exception
    # "__str__" = String dunder method
    def __str__(self):
        return f"{self.value} -> {self.message}"


def only_positive_num():
    try:
        x = -10
        if x < 0:
            # create instance now!
            raise NegativeNumberError(x)

    # match what type of error it is
    # assign "e" to the instance you are creating
    except NegativeNumberError as e:
        print(e)


# class Error:
#     def __init__(self, name, exctype):
#         self.name = name
#         self.exctype = exctype

#     def printerror(self):
#         return f"The error is {self.name} and its exception type is {self.exctype}"


# # create 3 errors
# null = Error("nullerror", "nullexception")
# zero = Error("zerodivisionerror", "zerodivisionexception")
# outofrange = Error("indexoutofrangeerror", "indexexception")
# print(null.printerror())
# print(zero.printerror())
# print(outofrange.printerror())

if __name__ == "__main__":
    math_divide(10, 5)
    math_divide(20, 0)
    # math_divide("abc", 1)  # breaks because it is not caught
    math_divide2(10, 8)
    math_divide2(9, 0)
    calculate_age()
    only_positive_num()
