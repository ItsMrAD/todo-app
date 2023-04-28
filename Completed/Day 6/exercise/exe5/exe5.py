files = ["a.txt", "b.txt", "c.txt"]
for file in files:
    text = open(file, "r")
    print(text.read())