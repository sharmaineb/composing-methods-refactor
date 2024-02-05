# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math

def calculate_distance(x1, y1, x2, y2):
    """Calculate the distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

xc1, yc1 = 4, 4.25
xc2, yc2 = 53, -5.35
distance = calculate_distance(xc1, yc1, xc2, yc2)
print('distance', distance)

xa, ya = -36, 97
xb, yb = 0.34, 0.91
length = calculate_distance(xa, ya, xb, yb)
print('length', length)