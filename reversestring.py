phrase = input("Enter your phrase: ")

phrase_reversed = ""

for i in range(1, len(phrase) + 1):
    phrase_reversed += phrase[-i]

print(f"Reversed phrase is: '{phrase_reversed}' ")
print(f"Integrated python solution: {phrase[::-1]}")
