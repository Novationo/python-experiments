password = str(input())
goodpass = ""

for i in password:
    if i == "i":
        goodpass += "1"
    elif i == "a":
        goodpass += "@"
    elif i == "m":
        goodpass += "M"
    elif i == "B":
        goodpass += "8"
    elif i == "s":
        goodpass += "$"
    else:
        goodpass += i


print(f"{goodpass}!")