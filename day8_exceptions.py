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


math_divide(10, 5)
math_divide(20, 0)
print("Hiii")
