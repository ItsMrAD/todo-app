password = input("Enter a password: ")

result = {}


def check(result):
    if len(password) >= 8:
        result['length'] = True
    else:
        result['length'] = False

    result['uppercase'] = False
    for i in password:
        if i.isupper():
            result['uppercase'] = True

    result['digit'] = False
    for i in password:
        if i.isdigit():
            result['digit'] = True

    return result


result = check(result)
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")