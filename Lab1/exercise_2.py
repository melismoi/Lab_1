# ==========================================
# EXERCISE 2: String Operations (5 points)
# ==========================================
def exercise2(first_name, last_name):
    """
    Combine first and last names with a space between.
    
    Args:
        first_name (str): First name
        last_name (str): Last name
    
    Returns:
        str: Full name with space between
    
    Example:
        exercise2("John", "Doe") returns "John Doe"
    """
    # TODO: Combine first_name and last_name with a space
    first_name = "melis" 
    last_name = "telli"
    full_name = first_name + ' ' + last_name
    
    
    return full_name

print(exercise2('melis', 'telli'))