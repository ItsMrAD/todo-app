year_of_birth = int(input("What is your year of birth? \n"))


def age(year_of_birth, current_year=2023):
    age_local = current_year - year_of_birth
    return age_local


age = age(year_of_birth)
if age <= 122:
    print(f"Your age is {age}")
else:
    print("Bruh! Go get a job")
