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
    """Calculate the final price of a customer's order."""  # correction 1 added Docstring
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

# print("Customer:", customer)  #Repeatitive code
# print("Price:", price)
# print("Quantity:", quantity)
# print("Subtotal:", subtotal)
# print("Discount:", discount)
# print("Member discount:", member_discount)
# print("Final total:", total)


# print("Customer:", customer) # commented this out as this is a repeat code
# print("Final total:", total)



