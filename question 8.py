input_str = input("write a valid password")

passwords = input_str.split(',')

valid_passwords = []

for key in passwords:
    if 6 <= len(key) <= 12:
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False

        for char in key:
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
            elif char in "$#@":
                has_special = True

        if has_lower and has_upper and has_digit and has_special:
            valid_passwords.append(key)
print(",".join(valid_passwords))
