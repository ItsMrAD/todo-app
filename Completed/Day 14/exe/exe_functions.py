freezing_point = 0
boiling_point = 100


def water_state(temperature):
    if temperature > boiling_point:
        state = "Gas"
    elif temperature < freezing_point:
        state = "Solid"
    else:
        state = "Liquid"
    return state
