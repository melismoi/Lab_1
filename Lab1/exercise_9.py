# ==========================================
# EXERCISE 9: Discount Calculator (10 points)
# ==========================================
def exercise9(purchase_amount):
    """
    Calculate discount and final price.
    $100+: 20% off, $50-99: 10% off, <$50: no discount
    
    Args:
        purchase_amount (float): Original purchase amount
    
    Returns:
        dict: Dictionary with 'discount_rate', 'discount_amount', 'final_price'
    
    Example:
        exercise9(75) returns 
        {'discount_rate': 0.10, 'discount_amount': 7.5, 'final_price': 67.5}
    """
    # TODO: Determine discount rate based on purchase amount
    discount_rate = 0
    discount_amount = 0
    final_price = 0
    
    return {
        'discount_rate': discount_rate,
        'discount_amount': discount_amount,
        'final_price': final_price
    }

exercise9()