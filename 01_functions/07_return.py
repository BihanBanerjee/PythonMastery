# Once the function hit the return keyword it will exit the function
# and return the value to the calling function. No other code (inside the function) will be executed.
def chai_status(cups_left):
    if cups_left == 0:
        return 'Sorry, chai is out of stock'
    return 'Chai is ready'

print(chai_status(0))
print(chai_status(4))

# ============================================================================
# RETURNING MULTIPLE VALUES FROM A FUNCTION
# ============================================================================

"""
Python allows functions to return multiple values at once!
The values are returned as a tuple, which can be unpacked into separate variables.
"""

def chai_report():
    """
    This function returns THREE values at once:
    1. Number of cups sold
    2. Number of cups remaining
    3. Number of cups in production

    When you return multiple values separated by commas,
    Python automatically packs them into a tuple.
    """
    return 100, 20, 10  # sold, remaining, in_production

# ============================================================================
# METHOD 1: Unpacking the return values into separate variables
# ============================================================================

# The returned tuple is automatically unpacked into three variables
# This is called "tuple unpacking" or "multiple assignment"
sold, remaining, in_production = chai_report()

print("Sold:", sold)
print("Remaining:", remaining)
print("In production:", in_production)

# ============================================================================
# METHOD 2: Receiving all values as a single tuple
# ============================================================================

# If you want, you can also receive all values as a single tuple
report = chai_report()
print("\nComplete report:", report)
print("Type of report:", type(report))  # It's a tuple!

# Then access individual values using indexing
print("Sold (via index):", report[0])
print("Remaining (via index):", report[1])

# ============================================================================
# METHOD 3: Using underscore (_) to ignore unwanted values
# ============================================================================

"""
Sometimes you only need SOME of the returned values, not all of them.
In Python, the underscore (_) is used as a throwaway variable name
to indicate "I don't care about this value"
"""

# Example: We only care about 'sold' and 'remaining', not 'in_production'
sold, remaining, _ = chai_report()
print("\n--- Using underscore to ignore values ---")
print("Sold:", sold)
print("Remaining:", remaining)
# We deliberately ignored the third value (in_production) using _

# Example: We only care about 'remaining', ignore the rest
_, remaining, _ = chai_report()
print("\n--- Only caring about the middle value ---")
print("Only remaining matters:", remaining)

# Example: We only care about the first value
sold, _, _ = chai_report()
print("\n--- Only caring about the first value ---")
print("Only sold matters:", sold)

# Note: The underscore is just a convention. Technically, _ is a valid variable name
# but using it signals to other programmers "I'm not going to use this value"

# ============================================================================
# PRACTICAL EXAMPLE: Function with multiple return values
# ============================================================================

def calculate_chai_stats(total_made, cups_sold):
    """
    Calculate various statistics about chai sales

    Returns:
        remaining: Cups left to sell
        revenue: Total money earned (assuming 50 rupees per cup)
        percentage_sold: What percentage was sold
    """
    remaining = total_made - cups_sold
    revenue = cups_sold * 50
    percentage_sold = (cups_sold / total_made) * 100

    return remaining, revenue, percentage_sold

# Unpack the three return values
cups_left, money_earned, sold_percent = calculate_chai_stats(100, 75)

print(f"\nChai Stats:")
print(f"Cups remaining: {cups_left}")
print(f"Revenue earned: ₹{money_earned}")
print(f"Percentage sold: {sold_percent}%")

# ============================================================================
# KEY POINTS TO REMEMBER
# ============================================================================

"""
IMPORTANT CONCEPTS:

1. Multiple Return Values:
   - Use commas to return multiple values: return val1, val2, val3
   - Python automatically packs them into a tuple

2. Tuple Unpacking:
   - You can unpack returned values directly: a, b, c = function()
   - Number of variables must match number of returned values
   - Or receive as a single tuple: result = function()

3. Order Matters:
   - Values are returned and unpacked in the same order
   - Make sure you assign them to the correct variables

4. Common Use Cases:
   - Returning multiple related pieces of information
   - Returning both result and status/error code
   - Returning min and max values together
   - Returning statistics or calculations

5. You can also return other data types:
   - Lists: return [val1, val2, val3]
   - Dictionaries: return {"key1": val1, "key2": val2}
   - But tuples are the standard convention for multiple returns

6. Using Underscore (_) to Ignore Values:
   - Use _ for values you don't need: result, _, error = function()
   - You can use multiple underscores: _, middle, _ = function()
   - This is a convention that makes code more readable
   - It tells other developers "I'm intentionally not using this value"
"""