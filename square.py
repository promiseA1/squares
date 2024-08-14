import math
def calculate():
    C = 50
    H = 30
    D = input("Enter a numbers seperated by comma: ").split(",")

    result = []

    for i in D:
        i = int(i)
        Q = math.sqrt((2 * C * i) / H)
        result.append(Q)
    return result


print(calculate())

