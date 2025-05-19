n = int(input("Enter a number: "))
num_str = str(n)
num_digits = len(num_str)
sum_of_powers = 0

for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

if sum_of_powers == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
