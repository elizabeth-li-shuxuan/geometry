from geometry.circle import calculate_area
from math import pi


def test_area():
    r = 1 
    area = calculate_area(r)
    area = 1
    assert area == pi, "The calculation is wrong"

    r = -1 
    area = calculate_area(r)
    assert area = np.nan

    