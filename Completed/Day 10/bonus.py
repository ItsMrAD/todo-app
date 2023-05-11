try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))
    if width == length:
        exit("That's a square!")

    print(width * length)
except ValueError:
    print("Please Enter A Number!")
