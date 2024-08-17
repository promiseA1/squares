import math

def distance_between_two_cities(lat_1 , lon_1 ,lat_2 , lon_2):
    radius = 6371.01
    lat_1_rad = math.radians(lat_1)
    lon_1_rad = math.radians(lon_1)
    lat_2_rad = math.radians(lat_2)
    lon_2_rad = math.radians(lon_2)

    x1 = lat_1_rad
    x2 = lat_2_rad
    y1 = lon_1_rad
    y2 = lon_2_rad

    return radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
    #return f"The distance between Atlanta,  Georgia and Charlotte , North_Carolina is {distance_between_two_cities:.2f} km"

def area_of_a_triangle(side1 , side2 , side3):
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))







lat_1 , lon_1 = eval(input("Enter lat_1 and lon_1 for Atlanta , Georgia: "))
lat_2 , lon_2 = eval(input("Enter lat_2 and lon_2 for Charlotte , North_Carolina: "))
lat_3 , lon_3 = eval(input("Enter lat_3 and lon_3 for Savannah , Georgia: "))

#calculate distances between the points
side1 = distance_between_two_cities(lat_1 , lon_1 , lat_2 , lon_2)
side2 = distance_between_two_cities(lat_2 , lon_2 , lat_3 , lon_3)
side3 = distance_between_two_cities(lat_3 , lon_3 , lat_1 , lon_1)

#calculate the area of the triangle
area = area_of_a_triangle(side1 , side2 , side3)



print(distance_between_two_cities(lat_1  , lon_1 , lat_2 , lon_2))
print(area_of_a_triangle(side1 , side2 , side3))