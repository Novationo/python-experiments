password3 = ""
password1 = ""
password2 =""

password1 = str(input("Enter Password: "))
password2 = str(input("Re-enter Password: "))

if password1 == password2:
    print("Success")
elif password1 != password2:
    password3 = str(input("Passwords do not match, Retry: "))
    if password1 == password3:
        print("Success")
    else:
        print("Passwords still don't match")