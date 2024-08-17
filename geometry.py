from math import pi , tan
def area_of_a_pentagon(side):
    s = side
    area = 5 * s**2 / (4 * tan(pi / 5))
    return f"The area of the pentagon is {area}"

side = eval(input("Enter the side: "))
print(area_of_a_pentagon(side))