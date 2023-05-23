def converter(feet, inches):
    feet = float(feet)
    inches = float(inches)
    meter = ((feet * 12) + inches) / 39.37
    meter = round(meter, 2)
    return meter


if __name__ == "__main__":
    feet = float(input("Feet: "))
    inches = float(input("Inches: "))
    print(converter(feet, inches))
