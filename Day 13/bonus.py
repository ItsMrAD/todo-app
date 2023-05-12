feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


parsed = parse(feet_inches)


def convert(feet, inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert(parsed['feet'], parsed['inches'])
if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
