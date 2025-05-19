email = input("Enter email address: ")
if email.count('@') != 1:
    print("Invalid: Must contain exactly one '@' symbol.")
else:
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789._@"
    valid = True

    for ch in email:
        if ch not in allowed_chars:
            valid = False
            print("Invalid: Contains characters other than lowercase letters, numbers, '.', '_' or '@'.")
            break

    if valid:
        if email.lower() != email:
            print("Invalid: Only lowercase letters are allowed.")
        else:
            print("Valid Email Address!")
