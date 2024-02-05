# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.

def get_price(quantity, item_price):
    def base_price():
        return quantity * item_price

    def discount_factor():
        if base_price() > 1000:
            return 0.95
        else:
            return 0.98

    return base_price() * discount_factor()