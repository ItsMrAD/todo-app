try:
    tv = int(input('Enter total value: '))
    v = int(input('Enter value: '))
    print(f"That is {v / tv * 100}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero")
