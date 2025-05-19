n = int(input("Enter total number of stops (n): "))
m = int(input("Enter number of stops to choose (m): "))

def nCr(n, r):
    return fact(n) // (fact(r) * fact(n - r))


def fact(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

if m > n - m + 1:
    print("Output: 0")
else:
    result = nCr(n - m + 1, m)
    print("Output:", result)
