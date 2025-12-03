"""
PURE vs IMPURE FUNCTIONS

PURE: Same input → Same output, No side effects
IMPURE: Different outputs with same inputs OR has side effects
"""

# ============================================================================
# PURE FUNCTIONS
# ============================================================================

def add(a, b):
    """PURE: Always returns same result, no side effects"""
    return a + b

print("add(2, 3):", add(2, 3))  # Always 5
print("add(2, 3):", add(2, 3))  # Always 5


# ============================================================================
# IMPURE FUNCTIONS
# ============================================================================

# Type 1: Modifying global variables
counter = 0

def increment():
    """IMPURE: Modifies global variable"""
    global counter
    counter += 1
    return counter

print("\nincrement():", increment())  # 1
print("increment():", increment())    # 2 - Different result!


# Type 2: Depends on external state
chai_stock = 10

def get_total(price):
    """IMPURE: Depends on global variable"""
    return chai_stock * price

print("\nget_total(50):", get_total(50))  # 500
chai_stock = 20
print("get_total(50):", get_total(50))    # 1000 - Different!


# Type 3: I/O operations
def greet(name):
    """IMPURE: Prints (side effect)"""
    print(f"Hello, {name}!")
    return "Greeted"


# ============================================================================
# CONVERTING IMPURE TO PURE
# ============================================================================

# IMPURE
total = 0
def add_impure(value):
    global total
    total += value
    return total

# PURE - pass state as parameter
def add_pure(current_total, value):
    return current_total + value

my_total = 0
my_total = add_pure(my_total, 10)
print("\nAfter adding 10:", my_total)


"""
KEY POINTS:
- Pure functions: Predictable, easier to test
- Impure functions: Have side effects (modify globals, print, etc.)
- Best practice: Prefer pure functions, pass state as parameters
"""
