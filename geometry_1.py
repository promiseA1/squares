import math 
def area_of_a_regular_polygon(number_of_sides , sides):
    n = number_of_sides
    s = sides
    area = n * s**2 / (4 * math.tan(math.pi / n))
    return f"The area of the polygon is {area}"

number_of_sides = eval(input("Enter the number of sides: "))
sides = eval(input("Enter the side: "))
print(area_of_a_regular_polygon(number_of_sides , sides))