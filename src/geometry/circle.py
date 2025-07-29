from math import pi

def calculate_area(r):
    """ 
    Calculate area of a circle.

    Parameters 
    ----------
    r : float 
       The radius of a circle. 

    Returns
    -------
    area : float
       The area calculated. 
    """ 
    area = pi * r ** 2 
    return area

def calculate_circ(r):
    """
    Calculate circumference of a circle.

    Parameters 
    ----------
    r : float 
       The radius of a circle. 

    Returns
    -------
    area : float
       The circumference calculated. 
    """
    circ = 2 * pi * r
    return circ