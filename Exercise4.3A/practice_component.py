"""
Exercise 4.3A - Quality Review and Refactor Practice Component

This is a simple working component for a quality review exercise.

Learner instructions:
- Run the program first and record the output.
- Review the code for naming, formatting, readability and duplication.
- Run Black, Ruff or Pylint as instructed by the tutor.
- Make controlled improvements without changing the required behaviour.
- Run the same test cases again after refactoring.
"""


def process_order(customer, price, quantity, member):
    """Calculate a customer's order total and return a summary.

    This function calculates the subtotal, applies any standard and member
    discounts, and returns a formatted order summary.

    Args:
        customer: The customer's name to include in the order summary.
        price: The unit price of each item in the order.
        quantity: The number of items being purchased.
        member: True if the customer is a loyalty member; otherwise False.

    Returns:
        A string containing the customer details, subtotal, discounts, and
        final total for the order.
    """
    subtotal = price * quantity

    if subtotal > 100:
        discount = subtotal * 0.10
    else:
        discount = 0

    if member is True:  # correction 2 Changed == to is using pylint
        member_discount = subtotal * 0.05
    else:
        member_discount = 0

    total = subtotal - discount - member_discount
    if total >= 100:
        print("Order status: Standard")
    else:
        print("Order status: Small")
    return f"""
    Customer: {customer}
    Price: {price}
    Quantity: {quantity}
    Member: {member}
    Subtotal: {subtotal}
    Discount: {discount}
    Member discount: {member_discount}
    Final total: {total}
    """

# Test cases
print(process_order("Aisha", 30, 2, False))
print()
print(process_order("Ben", 60, 2, True))
print()
print(process_order("Chloe", 50, 3, False))