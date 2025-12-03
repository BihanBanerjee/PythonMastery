"""
LAMBDA FUNCTIONS

Lambda = Anonymous (unnamed) function for simple, one-line operations
Syntax: lambda arguments: expression
"""

# ============================================================================
# Example 1: Using lambda with filter() - Filter items by condition
# ============================================================================

chai_types = ['light', 'kadak', 'ginger', 'kadak', 'masala']

# Filter only 'kadak' chai
strong_chai = list(filter(lambda chai: chai == 'kadak', chai_types))
print("Strong chai:", strong_chai)  # ['kadak', 'kadak']

# Filter everything except 'kadak'
mild_chai = list(filter(lambda chai: chai != 'kadak', chai_types))
print("Mild chai:", mild_chai)  # ['light', 'ginger', 'masala']


# ============================================================================
# Example 2: Using lambda with map() - Transform each item
# ============================================================================

prices = [50, 75, 100, 120]

# Add 10% tax to each price
with_tax = list(map(lambda price: price * 1.1, prices))
print("\nPrices with tax:", with_tax)


# ============================================================================
# Example 3: Using lambda with sorted() - Custom sorting
# ============================================================================

chai_menu = [
    {'name': 'Masala', 'price': 80},
    {'name': 'Ginger', 'price': 60},
    {'name': 'Kadak', 'price': 70}
]

# Sort by price
sorted_by_price = sorted(chai_menu, key=lambda item: item['price'])
print("\nSorted by price:", sorted_by_price)


# ============================================================================
# Lambda vs Regular Function
# ============================================================================

# Regular function
def add_tax(price):
    return price * 1.1

# Lambda equivalent
add_tax_lambda = lambda price: price * 1.1

print("\nRegular function:", add_tax(100))
print("Lambda function:", add_tax_lambda(100))


"""
WHEN TO USE LAMBDA:
✓ With filter(), map(), sorted() for simple operations
✓ One-time, short operations
✓ When defining a full function seems overkill

WHEN NOT TO USE:
✗ Complex logic (multiple lines) - use def instead
✗ Need to reuse multiple times - use def with a proper name
✗ Makes code hard to read - clarity over brevity
"""