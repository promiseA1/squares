import math
def area_of_a_pentagon(length):
    r = length
    s = 2 * r * (math.sin(math.pi/5))
    area = (3 * (math.sqrt(3)) / 2) * s**2
    return f"The area of a pentagon is {area:.2f}"


length = eval(input("Enter the length from the center to a vertex: "))
print(area_of_a_pentagon(length))

