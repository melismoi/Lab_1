# ==========================================
# EXERCISE 6: Shopping Cart (8 points)
# ==========================================
def exercise6(item_price, quantity, tax_rate):
    """
    Calculate shopping cart totals with tax.
    
    Args:
        item_price (float): Price per item
        quantity (int): Number of items
        tax_rate (float): Tax rate (e.g., 0.07 for 7%)
    
    Returns:
        dict: Dictionary with keys 'subtotal', 'tax', 'total'
    
    Example:
        exercise6(29.99, 4, 0.07) returns 
        {'subtotal': 119.96, 'tax': 8.3972, 'total': 128.3572}
    """
    # TODO: Calculate subtotal, tax, and total
    subtotal = item_price * quantity 
    tax = subtotal * tax_rate           
    total = subtotal + tax           
    
    print(subtotal , tax , total )
    return {'subtotal': subtotal, 'tax': tax, 'total': total}
exercise6(31.11 , 5 , 0.07)