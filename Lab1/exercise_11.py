# ==========================================
# EXERCISE 11: Logic Error (7 points)
# ==========================================
def exercise11(num):
    """
    Check if a number is positive, negative, or zero.
    
    THIS CODE HAS A LOGIC ERROR - FIX IT!
    
    Args:
        num (int): Number to check
    
    Returns:
        str: "positive", "negative", or "zero"
    
    Example:
        exercise11(5) returns "positive"
        exercise11(-3) returns "negative"
        exercise11(0) returns "zero"
    """
    # BUGGY CODE - FIX THE LOGIC:
    if num == 0:
        print("zero") # Something is wrong here!
    elif num < 0:
        print("negative")
    else:
        print("positive")  # Something is wrong here too!
    
exercise11(15)