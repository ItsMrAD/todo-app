liter = input("How many liters it the liquid: ")


def convert(liter):
    cubic_meter = float(liter) / 1000
    return cubic_meter


cubic_meter = convert(liter)
print(f"It is {cubic_meter} cubic meters")