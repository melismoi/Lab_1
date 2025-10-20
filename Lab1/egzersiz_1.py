# ==========================================
# LAB 1: PYTHON FOUNDATIONS
# Advanced Python Course - Week 1
# ==========================================
# 
# INSTRUCTIONS:
# - Complete each exercise function below
# - Do not change function names or parameters
# - Test your code by running: python test_lab1.py
# - Submit by pushing to your GitHub repository
# ==========================================

# ==========================================
# EXERCISE 1: Create Your Profile (5 points)
# ==========================================
def exercise1():
    """
    Create variables storing information about yourself and return them as a dictionary.
    
    Returns:
        dict: Dictionary with keys 'name', 'age', 'height', 'loves_programming'
    
    Example:
        {'name': 'John', 'age': 20, 'height': 1.75, 'loves_programming': True}
    """
    # TODO: Create four variables with your information
    your_name = "melis_telli"  
    your_age = 23
    your_height = 1.60
    loves_programming = True

    return {
        'name': your_name,
        'age': your_age,
        'height': your_height,
        'loves_programming': loves_programming
    }

print(exercise1())