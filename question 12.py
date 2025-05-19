s = input("Enter the alphanumeric string: ")
i = 0

while i < len(s):
    if s[i].isalpha():
        start_letter = s[i]
        i += 1
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        if num_str and i < len(s) and s[i].isalpha():
            end_letter = s[i]
            digit_sum = sum(int(ch) for ch in num_str)
            if digit_sum == 9:
                print(f"{start_letter},{end_letter}")
    else:
        i += 1
