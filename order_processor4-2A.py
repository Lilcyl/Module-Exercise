
"""
Exercise 4.2B -> fault order processor

 program processes a simple customer order ,
this program contains sevveral defects that must be identified, corr 
and corrected using proper debugging process

Order calculation rules :
1. subtotal = price* quantiy
2. a 10% discount when subtotal is greater than 100, discount
should be calulated from the subtotal 
3. shipping in 5 when the amount after discount is below 50
4. quantity must be greater than 0
5. price must not be negative 
6. function should return the final order total
"""

def calculate_order_total(price,quantity):
    subtotal = price + quantity
    if(subtotal>100):
        discount = subtotal * 0.10 
    else :
        discount = 0
    amount_after_discount = subtotal - discount
    if( amount_after_discount>50):
        shipping=5
    else:
        shipping = 0
    if(quantity<0):
        raise ValueError("Quantity ,must be greater than 0")
    return amount_after_discount+shipping
final_cost = calculate_order_total(50,5)
print(final_cost)