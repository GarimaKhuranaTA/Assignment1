entries = []

print("Enter data in the format 'name,age,height' (Press Enter to stop):")

while True:
    line = input()
    if not line:
        break
    parts = line.split(",")
    entries.append((parts[0], int(parts[1]), int(parts[2])))

entries.sort(key=lambda x: (x[0], x[1], x[2]))

result = [(name, str(age), str(height)) for name, age, height in entries]

print(result)
