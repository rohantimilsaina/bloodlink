
from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of Earth in kilometers
    print(distance)

    return distance

# Test code with default values (New York City to Los Angeles)
# lat1, lon1 = 28.613108, 81.152134  # Latitude and longitude of New York City
# lat2, lon2 = 28.642915, 81.281671  # Latitude and longitude of Los Angeles
lat1, lon1 =28.6268345,81.15468041666666
lat2, lon2 =28.642915,81.281671
distance = calculate_distance(lat1, lon1, lat2, lon2)
print("Distance between New York City and Los Angeles is {:.2f} kilometers.".format(distance))