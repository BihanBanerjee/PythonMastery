"""
Understanding *args and **kwargs in Python

This file explains two powerful concepts in Python:
1. *args (arbitrary positional arguments)
2. **kwargs (arbitrary keyword arguments)

These allow functions to accept variable numbers of arguments.
"""

# ============================================================================
# PART 1: Understanding *args (Arbitrary Positional Arguments)
# ============================================================================

# *args allows a function to accept any number of positional arguments
# The arguments are collected into a tuple

def simple_function(*args):
    """
    *args collects all positional arguments into a tuple
    You can name it anything (*ingredients, *numbers, etc.)
    The * is what makes it special, 'args' is just convention
    """
    print("Type of args:", type(args))
    print("Contents of args:", args)
    print()

# Example calls:
print("=== Example 1: Using *args ===")
simple_function(1, 2, 3)
simple_function("apple", "banana", "cherry", "dates")
simple_function()  # Can even call with no arguments


# ============================================================================
# PART 2: Understanding **kwargs (Arbitrary Keyword Arguments)
# ============================================================================

# **kwargs allows a function to accept any number of keyword arguments
# The arguments are collected into a dictionary

def simple_kwargs_function(**kwargs):
    """
    **kwargs collects all keyword arguments into a dictionary
    Keys are the parameter names, values are the values passed
    Again, you can name it anything (**extras, **options, etc.)
    The ** is what makes it special, 'kwargs' is just convention
    """
    print("Type of kwargs:", type(kwargs))
    print("Contents of kwargs:", kwargs)
    print()

# Example calls:
print("\n=== Example 2: Using **kwargs ===")
simple_kwargs_function(name="Alice", age=25, city="New York")
simple_kwargs_function(color="red", size="large")
simple_kwargs_function()  # Can call with no keyword arguments


# ============================================================================
# PART 3: Combining *args and **kwargs
# ============================================================================

def special_chai(*ingredients, **extras):
    """
    This function demonstrates using both *args and **kwargs together

    *ingredients will capture all positional arguments (like "Cinnamon", "Cardmom")
    **extras will capture all keyword arguments (like sweetener="Honey", foam="yes")
    """
    print("Ingredients:", ingredients)
    print("Extras:", extras)
    print()

# Example call from your screenshot:
print("=== Example 3: The Chai Function ===")
special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")


# ============================================================================
# PART 4: Practical Examples
# ============================================================================

def make_pizza(*toppings, **options):
    """
    A practical example: Making a pizza

    *toppings: Any number of toppings (positional arguments)
    **options: Pizza customization options (keyword arguments)
    """
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"  - {topping}")

    print("\nPizza options:")
    for option, value in options.items():
        print(f"  {option}: {value}")
    print()

print("\n=== Example 4: Pizza Maker ===")
make_pizza("pepperoni", "mushrooms", "olives",
           size="large", crust="thin", extra_cheese=True)


def calculate_sum(*numbers):
    """
    Example: Calculate sum of any number of values
    This shows how to actually USE the arguments collected by *args
    """
    total = 0
    for num in numbers:
        total += num
    return total

print("\n=== Example 5: Calculating Sums ===")
print("Sum of 1, 2, 3:", calculate_sum(1, 2, 3))
print("Sum of 10, 20, 30, 40, 50:", calculate_sum(10, 20, 30, 40, 50))


def user_profile(username, *interests, **details):
    """
    Example with regular argument, *args, and **kwargs combined

    Order matters when mixing parameter types:
    1. Regular positional parameters (username)
    2. *args (interests)
    3. **kwargs (details)
    """
    print(f"Username: {username}")

    print("Interests:", end=" ")
    for interest in interests:
        print(interest, end=" ")
    print()

    print("Additional details:")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()

print("\n=== Example 6: User Profile ===")
user_profile("john_doe", "coding", "gaming", "reading",
             age=28, location="California", profession="Developer")


# ============================================================================
# PART 5: Key Points to Remember
# ============================================================================

"""
KEY TAKEAWAYS:

1. *args:
   - Collects extra POSITIONAL arguments into a TUPLE
   - Use when you don't know how many positional arguments will be passed
   - The name 'args' is convention, but you can use any name with *

2. **kwargs:
   - Collects extra KEYWORD arguments into a DICTIONARY
   - Use when you don't know what keyword arguments will be passed
   - The name 'kwargs' is convention, but you can use any name with **

3. Order matters when combining parameters:
   def function(regular_param, *args, **kwargs):

   This order must be followed:
   a) Regular positional parameters
   b) *args
   c) **kwargs

4. Real-world uses:
   - Creating flexible APIs
   - Wrapper functions
   - Decorator functions
   - When you want to accept any number of arguments

5. Unpacking:
   You can also use * and ** to UNPACK arguments when CALLING functions:

   numbers = [1, 2, 3]
   calculate_sum(*numbers)  # Unpacks list into separate arguments

   options = {"size": "large", "crust": "thin"}
   make_pizza("cheese", **options)  # Unpacks dict into keyword arguments
"""

# ============================================================================
# PART 6: Advanced Example - Unpacking Arguments
# ============================================================================

print("\n=== Example 7: Unpacking Arguments ===")

# Using * to unpack a list/tuple into positional arguments
ingredients_list = ["Ginger", "Lemon", "Mint"]
special_chai(*ingredients_list, temperature="hot", sugar="2-spoons")

# Using ** to unpack a dictionary into keyword arguments
chai_options = {"sweetener": "Stevia", "milk": "oat", "foam": "yes"}
special_chai("Tea-leaves", "Water", **chai_options)
