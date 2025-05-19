
input_str = input("enter the input")

letter_count = 0
digit_count = 0

for char in input_str:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print("LETTERS", letter_count)
print("DIGITS", digit_count)
