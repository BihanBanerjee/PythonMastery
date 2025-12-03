# Difference between 'nonlocal' and 'global' keywords in Python

# =====================================================
# EXAMPLE 1: Using 'nonlocal' keyword
# =====================================================
# 'nonlocal' modifies variables from the ENCLOSING (outer) function scope

def outer_function():
    message = "Original message"  # Variable in enclosing scope

    def inner_function():
        nonlocal message  # Refers to the 'message' variable in outer_function
        message = "Modified by nonlocal"  # Modifies the enclosing function's variable

    print(f"Before inner call: {message}")
    inner_function()
    print(f"After inner call: {message}")  # Will show the modified value

print("=== NONLOCAL Example ===")
outer_function()

# =====================================================
# EXAMPLE 2: Using 'global' keyword
# =====================================================
# 'global' modifies variables from the GLOBAL (module-level) scope

counter = 0  # Global variable

def increment_counter():
    global counter  # Refers to the global 'counter' variable
    counter += 1  # Modifies the global variable
    print(f"Counter inside function: {counter}")

print("\n=== GLOBAL Example ===")
print(f"Counter before function call: {counter}")
increment_counter()
increment_counter()
print(f"Counter after function calls: {counter}")

# =====================================================
# EXAMPLE 3: Comparing both in one scenario
# =====================================================

chai_stock = 100  # Global variable

def tea_shop():
    chai_orders = 0  # Enclosing variable (local to tea_shop)

    def take_order():
        nonlocal chai_orders  # Modifies enclosing variable
        global chai_stock     # Modifies global variable

        chai_orders += 1
        chai_stock -= 1

    print(f"\n=== TEA SHOP Example ===")
    print(f"Initial - Orders: {chai_orders}, Stock: {chai_stock}")

    take_order()
    take_order()
    take_order()

    print(f"After 3 orders - Orders: {chai_orders}, Stock: {chai_stock}")

tea_shop()
print(f"Global stock after tea_shop closed: {chai_stock}")

# =====================================================
# KEY DIFFERENCES SUMMARY
# =====================================================
#
# 1. SCOPE LEVEL:
#    - nonlocal: Works with variables in the ENCLOSING function scope
#    - global: Works with variables in the GLOBAL (module-level) scope
#
# 2. WHERE TO USE:
#    - nonlocal: Use in nested functions to modify outer function's variables
#    - global: Use in any function to modify module-level variables
#
# 3. VARIABLE MUST EXIST:
#    - nonlocal: Variable MUST already exist in an enclosing function
#    - global: Variable doesn't need to exist (can be created)
#
# 4. CANNOT BE USED TOGETHER:
#    - A variable cannot be both nonlocal and global
#    - You must choose one based on which scope you want to modify
#
# 5. READING vs WRITING:
#    - Both keywords are needed only for MODIFICATION (assignment)
#    - You can READ variables from outer/global scope without these keywords
