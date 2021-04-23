print("This program will divide 2 numbers")

stop_word = "stop"
while True:
    num1 = input("Enter the first num: ")
    if num1 == stop_word:
        exit(0)
    num2 = input("Enter the second num: ")
    if num2 == stop_word:
        exit(0)
    try:
        try:
            num1 = float(num1)
        except ValueError as e:
            raise ValueError("Error: First number is not a valid number")

        try:
            num2 = float(num2)
        except ValueError as e:
            raise ValueError("Error: Second number is not a valid number")
        print("Result: " + str(num1 / num2))
    except ValueError as e:
        print(str(e))
    except ZeroDivisionError as e:
        print("Error: division by zero")

