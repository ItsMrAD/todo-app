def get_max():
    grades = [9.6, 9.2, 9.7]
    max_local = max(grades)
    min_local = min(grades)
    output_local = f"Max: {max_local}, Min: {min_local}"
    return output_local

print(get_max())
