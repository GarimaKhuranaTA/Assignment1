
input_str = input("enter the words in comma seperated form")

words = input_str.split(',')

n = len(words)
for i in range(n):
    for j in range(0, n - i - 1):
        if words[j] > words[j + 1]:
            words[j], words[j + 1] = words[j + 1], words[j]

output_str = ",".join(words)

print(output_str)
