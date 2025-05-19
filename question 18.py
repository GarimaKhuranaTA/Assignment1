def pattern1():
    rows = int(input("Enter number of rows"))
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end="")
            if j != i:
                print(" * ", end="")
            num += 1
        print()

def pattern2():
    n = int(input("Enter number of rows"))
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)

def pattern3():
    rows = int(input("Enter number of rows"))
    num = 1
    store = []
    for i in range(1, rows + 1):
        line = []
        for j in range(i):
            line.append(str(num))
            num += 1
            if j != i - 1:
                line.append("*")
        store.append(" ".join(line))
        print(store[-1])
    for i in range(rows - 2, -1, -1):
        print(store[i])

def pattern4():
    n = int(input("Enter number of rows"))
    for i in range(n):
        if i == 0:
            print("  ***  ")
        elif i == 1 or i == 2:
            print(" *     ")
        elif i == 3:
            print(" * *** ")
        elif i == 4 or i == 5:
            print(" *    *")
        elif i == 6:
            print("  ***  ")

def pattern5():
    n = int(input("Enter an odd number of rows: "))
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == n // 2:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

while True:
    print("Pattern Menu ")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6. Exit")

    choice = input("Enter your choice (1-6) ")

    if choice == '1':
        pattern1()
    elif choice == '2':
        pattern2()
    elif choice == '3':
        pattern3()
    elif choice == '4':
        pattern4()
    elif choice == '5':
        pattern5()
    elif choice == '6':
        print("Exiting")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
