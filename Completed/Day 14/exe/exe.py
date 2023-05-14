import exe_functions

temperature = float(input("Enter water temperature: "))

state = exe_functions.water_state(temperature)
print(state)
