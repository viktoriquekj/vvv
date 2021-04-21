username = "developer1"
password = "hackme"

print("This program check if username and password correct\n")

input_username = input("please enter username:")
input_password = input("Please enter password:")

is_username_valid = username == input_username
is_password_valid = password == input_password

if not (is_password_valid and is_username_valid):
    if not is_username_valid:
        print("Invalid username")
    if not is_password_valid:
        print("Invalid password")
    exit(1)

print("Welcome " + input_username + ", you are authorized")
shut_down = input(" Do you want to shut down your computer?")
if shut_down == "Yes":
    print("Shutting down your PC")
elif shut_down == "No":
    become_admin = input("Do you want to become admin?")
    if become_admin == "Yes":
        print("You are admin now")
    else:
        print("Have a nice day")
else:
    print("Have a nice day")
