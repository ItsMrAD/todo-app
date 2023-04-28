while True:
    with open("sides.txt", "r") as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ") + "\n"
    sides.append(side)

    with open("sides.txt", "w") as file:
        file.writelines(sides)

    head_count = sides.count("head\n")
    side_count = len(sides)
    percentage = head_count / side_count * 100
    print(f"Heads = {percentage}%")
