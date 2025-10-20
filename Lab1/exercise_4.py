# ========================================
# EXERCISE 4: Temperature Converter (7 points)
# ==========================================
def exercise4(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    
    Example:
        exercise4(25) returns 77.0
    """
    # TODO: Calculate and return fahrenheit
    fahrenheit = (celsius * 9/5) + 32 
    print(fahrenheit)
    return fahrenheit
    
exercise4(40)  
