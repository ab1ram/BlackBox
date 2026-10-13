import string


def check_strength(password:str):
    report = []
    pass_len =len(password) 
    upper_count = 0
    lower_count = 0
    digit_count = 0
    symbol_count = 0

    for char in password:
        if char.isupper():
            upper_count += 1
        if char.islower():
            lower_count += 1
        if char.isdigit():
            digit_count += 1
        if char in string.punctuation :
            symbol_count += 1

    if pass_len < 12:
        print("Password length is too short, at least 12 characters recommended")
        report.append(False)
    if upper_count < 2:
        print("Not enough uppercase letters, at least 2 recommended")
        report.append(False)
    if lower_count < 2:
        print("Not enough lowercase letters, at least 2 recommended")
        report.append(False)
    if digit_count < 2:
        print("Not enough digits, at least 2 recommended")
        report.append(False)
    if symbol_count < 2:
        print("Not enough special characters, at least 2 recommended")
        report.append(False)

    if False in report :
        print(f"Your password failed {report.count(False)}/5 tests")
    else :
        print("Your password passed 5/5 tests")