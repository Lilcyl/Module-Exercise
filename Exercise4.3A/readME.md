# Quality Review and Refactor Practice Component

## Overview

This project is a simple Python program that processes customer orders.

The `process_order()` function:

* Calculates the order subtotal.
* Applies a 10% discount when the subtotal is greater than £100.
* Applies a 5% member discount when the customer is a member.
* Calculates the final order total.
* Displays whether the order is **Standard** or **Small**.
* Returns a summary containing the order details.

The project is designed as a **quality review and refactoring exercise** for a Level 3 Python developer.

---

## Requirements

To run this program, you need:

* Python 3 installed.
* A Python editor such as VS Code.
* Optional: Pylint, Ruff or Black for code quality checks.

The program does not require any external Python packages.

---

## How to Run

1. Save the Python code in a file, for example:

```text
process_order.py
```

2. Open a terminal in the project folder.

3. Run:

```bash
python process_order.py
```

---

## Function

The main function is:

```python
process_order(customer, price, quantity, member)
```

### Parameters

| Parameter  | Description                                           |
| ---------- | ----------------------------------------------------- |
| `customer` | Customer's name                                       |
| `price`    | Price of one item                                     |
| `quantity` | Number of items purchased                             |
| `member`   | `True` if the customer is a member, otherwise `False` |

### Calculation

The subtotal is calculated using:

```text
subtotal = price × quantity
```

A 10% discount is applied when:

```text
subtotal > 100
```

A 5% member discount is applied when:

```text
member = True
```

The final total is calculated using:

```text
total = subtotal - discount - member_discount
```

---

## Order Status

The program displays:

* **Standard** when the final total is £100 or more.
* **Small** when the final total is below £100.

---

## Test Cases

The program contains three test cases.

### Test Case 1 – Aisha

```python
process_order("Aisha", 30, 2, False)
```

Expected calculation:

```text
Subtotal = £60
Standard discount = £0
Member discount = £0
Final total = £60
Order status = Small
```

### Test Case 2 – Ben

```python
process_order("Ben", 60, 2, True)
```

Expected calculation:

```text
Subtotal = £120
Standard discount = £12
Member discount = £6
Final total = £102
Order status = Standard
```

### Test Case 3 – Chloe

```python
process_order("Chloe", 50, 3, False)
```

Expected calculation:

```text
Subtotal = £150
Standard discount = £15
Member discount = £0
Final total = £135
Order status = Standard
```

---

## Code Quality Review

The code can be reviewed using tools such as Pylint, Ruff or Black.

Areas to review include:

* Naming
* Formatting
* Readability
* Comments
* Docstrings
* Code duplication
* Unused variables or parameters
* Consistent coding style

The function includes a docstring explaining its purpose, parameters and return value.

---

## Refactoring

Refactoring means improving the structure and readability of code without changing its required behaviour.

Possible improvements include:

* Using clear variable names.
* Removing unnecessary comments.
* Improving formatting.
* Separating calculations into smaller functions if the program becomes larger.
* Keeping the code easy to test and maintain.

Any refactoring should be followed by running the original test cases again to make sure the behaviour has not changed.

---

## Expected Output

The program should produce output similar to:

```text
Order status: Small

Customer: Aisha
Price: 30
Quantity: 2
Member: False
Subtotal: 60
Discount: 0
Member discount: 0
Final total: 60

Order status: Standard

Customer: Ben
Price: 60
Quantity: 2
Member: True
Subtotal: 120
Discount: 12.0
Member discount: 6.0
Final total: 102.0

Order status: Standard

Customer: Chloe
Price: 50
Quantity: 3
Member: False
Subtotal: 150
Discount: 15.0
Member discount: 0
Final total: 135.0
```

---

## Quality Review Process

A simple review process for this project is:

1. Run the original program.
2. Record the output.
3. Review the code for quality issues.
4. Run a code-quality tool such as Pylint or Ruff.
5. Make one controlled improvement at a time.
6. Run the program again.
7. Compare the new output with the original output.
8. Confirm that the required behaviour has not changed.

## Conclusion

This project demonstrates basic Python development, functions, conditional statements, calculations, formatted strings, documentation and code-quality review.

The main goal is to practise making **small, controlled improvements** while keeping the program's required behaviour unchanged.
