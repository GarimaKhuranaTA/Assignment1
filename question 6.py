input_str = input("Enter the sentence to calculate the upper and lower case character")

upper_count = 0
lower_count = 0

for char in input_str:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("UPPER CASE", upper_count)
print("LOWER CASE", lower_count)
