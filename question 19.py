choice = int(input("Enter 1 for left rotation or 2 for right rotation"))
s = input("Enter string")
n = int(input("Enter number of rotations"))

print("\nRotated Outputs:")

for i in range(n):
    if choice == 1:
        s = s[1:] + s[0]
    elif choice == 2:
        s = s[-1] + s[:-1]
    else:
        print("Invalid choice. Please enter 1 or 2.")
        break
    print(s)
