import math

def distance_between_two_points():
    radius = 6371.01
    lat_1_rad = math.radians(lat_1)
    long_1_rad = math.radians(long_1)
    lat_2_rad = math.radians(lat_2)
    long_2_rad = math.radians(long_2)

    x1 = lat_1_rad
    x2 = lat_2_rad
    y1 = long_1_rad
    y2 = long_2_rad


    d = distance_between_two_points
    d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
    return f"The distance between the two points is {d} km"
    
lat_1 , long_1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
lat_2 , long_2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))
print(distance_between_two_points())