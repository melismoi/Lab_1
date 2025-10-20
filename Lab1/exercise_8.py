# ==========================================
# EXERCISE 8: Grade Calculator (10 points)
# ==========================================
def exercise8(score):
    """
    Convert numerical score to letter grade.
    90+: A, 80-89: B, 70-79: C, 60-69: D, <60: F
    
    Args:
        score (int): Numerical score
    
    Returns:
        str: Letter grade (A, B, C, D, or F)
    
    Example:
        exercise8(85) returns "B"
    """
    # TODO: Use if-elif-else to determine letter grade
    letter = ""
    if score > 90 :
        print("A")
    elif 80 > score >= 89:
        print("B")
    elif 70 > score >= 79:
        print("C")
    elif 60 > score >= 69:
        print("D")
    else:
        print("F")
    

        
    
    return letter
exercise8(15)