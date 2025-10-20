# ==========================================
# EXERCISE 5: Rectangle Area (7 points)
# ==========================================
def exercise5(length, width):
    """
    Calculate the area and perimeter of a rectangle.
    
    Args:
        length (float): Length of rectangle
        width (float): Width of rectangle
    
    Returns:
        dict: Dictionary with keys 'area' and 'perimeter'
    
    Example:
        exercise5(12.5, 8.3) returns {'area': 103.75, 'perimeter': 41.6}
    """
    # TODO: Calculate area and perimeter
    area = (length * width)
    perimeter = (2 * (length + width))
    print(area,perimeter)
    return {'area': area, 'perimeter': perimeter}

exercise5(15.5,8.5)