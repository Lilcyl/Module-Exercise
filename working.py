
"""
Exercise 4.2B -> fault order processor

 program processes a simple customer order ,
this program contains sevveral defects that must be identified, corr 
and corrected using proper debugging process

Order calculation rules :
1. subtotal = price* quantiy
2. a 10% discount when subtotal is greater than 100, discount
should be calulated from the subtotal 
3. shipping is 5 when the amount after discount is below 50
4. quantity must be greater than 0
5. price must not be negative 
6. function should return the final order total
"""

def calculate_order_total(price,quantity):
    try:
        subtotal = price * quantity #Correction no 1 previously +
        if(subtotal>100):
            discount = subtotal * 0.10 
        else :
            discount = 0
        amount_after_discount = subtotal - discount
        if(amount_after_discount<50): #correction no 2 previously >
            shipping=5
        else:
            shipping = 0
        if(quantity<=0): #Correction no 3 corrected to <=
            raise ValueError("Quantity ,must be greater than 0")
        if price <=0:
            raise ValueError("Price, must be a positive no ")
        return amount_after_discount+shipping
    except Exception as e:
        print(e)
final_cost = calculate_order_total(50,5)
print(final_cost)

final_cost = calculate_order_total(10,5)
print(final_cost)

final_cost = calculate_order_total(10,4)
print(final_cost)

