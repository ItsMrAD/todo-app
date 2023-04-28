country = input("Which country you are from? ")
country = country.lower()
match country:
    case "india" | "bharat":
        print("Namaste")
    case "usa" | "america" | "us":
        print("Hello")
    case "germany":
        print("Hallo")