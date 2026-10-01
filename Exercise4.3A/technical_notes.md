# Technical Note – Exercise 4.3A Quality Review and Refactor

## 1. Overview

This technical note documents the debugging and quality review of the `process_order()` Python component.

The original program was reviewed for:

* Functional defects
* Code duplication
* Naming and readability
* Documentation
* Pylint feedback
* Boolean comparisons
* Output handling
* Maintainability

The corrected version was then tested using the same three customer test cases.

---

# 2. Original Code

The original code calculated an order subtotal, applied discounts, calculated the final total and displayed the order information.

However, several quality issues were identified.

### Original member check

```python
if member == True:
    member_discount = subtotal * 0.05
else:
    member_discount = 0
```

### Duplicate output

The following information was printed:

```python
print("Customer:", customer)
print("Final total:", total)
```

and then printed again later in the function.

This resulted in unnecessary duplicate output.

---

# 3. Defects and Improvements

| ID   | Issue                                        | Original Code                                   | Correction                             | Reason                                                                                       |
| ---- | -------------------------------------------- | ----------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------- |
| D001 | Missing function docstring                   | No docstring was provided                       | Added a function docstring             | Improves documentation and satisfies Pylint documentation checks                             |
| D002 | Boolean comparison                           | `member == True`                                | `member is True`                       | Provides a more appropriate explicit Boolean check                                           |
| D003 | Duplicate output                             | Customer and final total were printed twice     | Removed duplicate output               | Makes the program output clearer and avoids repetition                                       |
| D004 | Function only printed results                | Values were printed directly                    | Function returns a formatted summary   | Makes the function more reusable because the returned value can be printed, stored or tested |
| D005 | Output readability                           | Several separate `print()` statements were used | Formatted multi-line f-string was used | Keeps the order summary together and improves readability                                    |
| D006 | Documentation of parameters and return value | No explanation of parameters or return value    | Added `Args` and `Returns` sections    | Makes the function easier for another developer to understand                                |

---

# 4. Debugging and Corrections

## D001 – Missing Function Docstring

### Problem

The original function started with:

```python
def process_order(customer, price, quantity, member):
```

There was no documentation explaining what the function does.

A code-quality tool such as Pylint can report a missing function docstring.

### Correction

A docstring was added:

```python
def process_order(customer, price, quantity, member):
    """Calculate a customer's order total and return a summary.
```

The documentation was then expanded to describe the parameters and returned value.

### Benefit

The function is easier for another developer to understand and maintain.

---

# 5. Boolean Comparison

## Original

```python
if member == True:
```

The code compares the value of `member` with `True`.

## Corrected

```python
if member is True:
```

This makes it explicit that the value must be the Boolean value `True`.

For this exercise, the corrected version follows the feedback received from the code-quality review.

A simpler Python style could also be:

```python
if member:
```

because `member` is expected to contain a Boolean value.

---

# 6. Duplicate Code

## Problem

The original program printed the customer and final total, then printed them again:

```python
print("Customer:", customer)
print("Final total:", total)

# ...

print("Customer:", customer)
print("Final total:", total)
```

This is unnecessary duplication.

## Correction

The duplicate output was removed.

The corrected function creates one formatted summary:

```python
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
```

This provides all the order information in one place.

---

# 7. Returning a Value

## Original Behaviour

The original function used `print()` statements to display the results.

This meant the function mainly performed output rather than returning a result that another part of the program could use.

## Corrected Behaviour

The corrected version uses:

```python
return f"""
Customer: {customer}
...
Final total: {total}
"""
```

The returned value is then displayed using:

```python
print(process_order("Aisha", 30, 2, False))
```

### Benefit

The function is now more flexible.

The returned value could be:

* Printed
* Stored in a variable
* Passed to another function
* Used in a test

For example:

```python
order_summary = process_order("Aisha", 30, 2, False)
print(order_summary)
```

---

# 8. Order Calculation

The calculation logic was checked during debugging.

The subtotal is calculated using:

```python
subtotal = price * quantity
```

A 10% discount is applied when:

```python
if subtotal > 100:
    discount = subtotal * 0.10
```

A 5% member discount is applied when the customer is a member:

```python
if member is True:
    member_discount = subtotal * 0.05
```

The final total is:

```python
total = subtotal - discount - member_discount
```

The order status is then determined using:

```python
if total >= 100:
    print("Order status: Standard")
else:
    print("Order status: Small")
```

---

# 9. Test Cases

The same three test cases were used after the corrections.

## Test Case 1 – Aisha

```python
process_order("Aisha", 30, 2, False)
```

### Calculation

```text
Subtotal = 30 × 2
Subtotal = 60

Discount = 0
Member discount = 0

Final total = 60
```

Expected status:

```text
Order status: Small
```

---

## Test Case 2 – Ben

```python
process_order("Ben", 60, 2, True)
```

### Calculation

```text
Subtotal = 60 × 2
Subtotal = 120

Standard discount = 120 × 0.10
Standard discount = 12

Member discount = 120 × 0.05
Member discount = 6

Final total = 120 - 12 - 6
Final total = 102
```

Expected status:

```text
Order status: Standard
```

---

## Test Case 3 – Chloe

```python
process_order("Chloe", 50, 3, False)
```

### Calculation

```text
Subtotal = 50 × 3
Subtotal = 150

Standard discount = 150 × 0.10
Standard discount = 15

Member discount = 0

Final total = 150 - 15
Final total = 135
```

Expected status:

```text
Order status: Standard
```

---

# 10. Testing Results

| Test Case | Customer | Subtotal | Discount | Member Discount | Final Total | Status   |
| --------- | -------- | -------: | -------: | --------------: | ----------: | -------- |
| 1         | Aisha    |       60 |        0 |               0 |          60 | Small    |
| 2         | Ben      |      120 |       12 |               6 |         102 | Standard |
| 3         | Chloe    |      150 |       15 |               0 |         135 | Standard |

The calculations produced the expected results after the code was corrected.

---

# 11. Quality Improvements

The corrected version includes several improvements:

### Documentation

A detailed docstring was added to explain:

* The purpose of the function
* Its parameters
* The returned value

### Readability

The returned order summary is formatted so that each piece of information appears on a separate line.

### Duplication

The repeated customer and final-total output was removed.

### Maintainability

Returning a summary rather than only printing individual values makes the function easier to reuse and test.

### Code Quality

The Boolean comparison was changed from:

```python
member == True
```

to:

```python
member is True
```

following the quality-review feedback.

---

# 12. Before and After

## Original

```python
if member == True:
    member_discount = subtotal * 0.05
else:
    member_discount = 0
```

## Corrected

```python
if member is True:
    member_discount = subtotal * 0.05
else:
    member_discount = 0
```

---

## Original

```python
print("Customer:", customer)
print("Final total:", total)

# ...

print("Customer:", customer)
print("Final total:", total)
```

## Corrected

```python
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
```

---

# 13. Debugging Process Used

The following process was used to review the component:

1. Run the original program.
2. Observe the program output.
3. Identify unexpected or duplicated output.
4. Review the code for repeated code and readability issues.
5. Run a code-quality tool such as Pylint.
6. Investigate the warnings rather than changing code without understanding them.
7. Add the missing function documentation.
8. Correct the Boolean comparison.
9. Remove unnecessary duplicated output.
10. Change the function to return an order summary.
11. Run the original test cases again.
12. Compare the results with the expected calculations.

---

# 14. Conclusion

The original program was functional but contained several quality and maintainability issues.

The main improvements were:

* Added a function docstring.
* Documented parameters and the return value.
* Improved the Boolean comparison.
* Removed duplicated output.
* Changed the function to return a formatted order summary.
* Re-ran the original test cases after making the changes.
* Confirmed that the order calculations produced the expected results.

