def apply_discount(price, discount_percent):
    """Apply a percentage discount to a price."""
    discount = price * discount_percent / 100
    return price - discount