x = input("Please input first nr: ")
y = input("Please input second nr: ")

x = float(x)
y = float(y)

if x > y:
    max_number = x
    info = "first nr is greater"
elif y > x:
    max_number = y
    info = "second nr is greater"
elif x == y:
    max_number = None
    info = "Numbers are even"
else:
    max_number = None
    info = "Unexpected behaviour"

print(info)
if max_number:
    print("Greater nr value: " + str(max_number))
