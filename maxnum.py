number1 = input("Please input first nr: ")
number2 = input("Please input second nr: ")


number1 = float(number1)
number2 = float(number2)

if number1 > number2:
    max_number = number1
    info = "first nr is greater"
elif number2 > number1:
    max_number = number2
    info = "second nr is greater"
elif number1 == number2:
    max_number = None
    info = "Numbers are even"
else:
    max_number = None
    info = "Unexpected behaviour"

print(info)
if max_number:
    print("Greater nr value: " + str(max_number))
