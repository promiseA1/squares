import math
def calculate():
    C =  50
    H = 30
    D = input("Enter a number seperated by commas: ").split(",")

    result = []

    for i in D:
        i = int(i)
        Q = math.sqrt((2 * C * i) / H)
        result.append(round(Q))
    return result



print(calculate())