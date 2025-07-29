from geometry.circle import calculate_area
from math import pi


def test_area():
    r = 1 
    area = calculate_area(r)
    assert area == pi, "The calculation is wrong"
    