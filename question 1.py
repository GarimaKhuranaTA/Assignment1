input_data =input("enter the two digits for 2D array in comma seperated form")
data = input_data.split(',')

X = int(data[0])
Y = int(data[1])
result =[]

for i in range(X):
    elements =[]
    for j in range(Y):
        elements.append(i*j)

    result.append(elements)

print(result)





