# nonlocal keyword --> allows you to modify a variable from the enclosing (outer) function's scope
# Without 'nonlocal', assignment creates a new local variable instead of modifying the outer one

def update_order():
    chai_type = "Elaichi"  # Variable in enclosing scope (belongs to update_order function)

    def kitchen():
        # 'nonlocal' tells Python: "I want to modify the chai_type from the outer function, not create a new local one"
        nonlocal chai_type
        chai_type = "Kesar"  # This MODIFIES the enclosing function's chai_type variable
        # Without 'nonlocal', this would create a NEW local variable in kitchen() function

    kitchen()  # Call the nested function
    print("After kitchen update", chai_type)  # This will print "Kesar" because nonlocal modified it

update_order()

# Key Concepts:
# 1. 'nonlocal' is used in nested functions to modify variables from the enclosing function
# 2. Without 'nonlocal', assignment creates a new local variable (doesn't modify outer one)
# 3. 'nonlocal' only works with enclosing function scope, NOT global scope (use 'global' for that)
# 4. You can only use 'nonlocal' with variables that already exist in an enclosing scope
