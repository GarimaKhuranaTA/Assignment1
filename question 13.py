s = input("Enter the binary string: ")
count_ones = s.count('1')
pairs = count_ones * (count_ones - 1) // 2
print(pairs)
