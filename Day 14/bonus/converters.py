def convert(feet, inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
    return meters