# ==========================================
# EXERCISE 7: Age Checker (8 points)
# ==========================================
def exercise7(age):
    """
    Check if someone can vote (18 or older).
    
    Args:
        age (int): Person's age
    
    Returns:
        str: "You can vote!" or "You cannot vote yet."
    
    Example:
        exercise7(16) returns "You cannot vote yet."
        exercise7(20) returns "You can vote!"
    """
    # TODO: Use if-else to check voting eligibility
    result = ""
    if age > 18 :
        print( "You can vote!")
    else :
        print("You cannot vote yet.")    

    return result
exercise7(17)
