password = input("Enter a password: ")
password_length = len(password)
if password_length > 7:
    print("Great password there!")
elif password_length == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak.")
