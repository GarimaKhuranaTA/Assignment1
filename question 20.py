healthy_data = {
    "Sugar level": 15,
    "Blood pressure": 32,
    "Heartbeat rate": 71,
    "weight": 65,
    "fat percentage": 10
}
print("Enter patient's readings:")
patient_data = {}

for key in healthy_data:
    print("Enter", key + ":", end=" ")
    value = int(input())
    patient_data[key] = value

print("Patient Report")
print(patient_data)

print("Differences from Healthy Values")
differences = {}

for key in healthy_data:
    diff = patient_data[key] - healthy_data[key]
    differences[key] = diff
    print(key + ":", diff)

print("Explanation")
for key in differences:
    diff = differences[key]
    if diff == 0:
        print(key + " is at the ideal value.")
    elif diff > 0:
        print(key + " is", diff, "more than the ideal value.")
    else:
        print(key + " is", abs(diff), "less than the ideal value.")
