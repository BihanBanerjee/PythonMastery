# global keyword --> allows you to modify a global variable from inside a function
# Without 'global', assignment inside a function creates a new local variable

chai_type = "Plain"  # Global variable (defined at module level, outside any function)

def front_desk():
    # front_desk() doesn't have its own chai_type variable
    # It contains a nested function that will modify the global variable

    def kitchen():
        # 'global' tells Python: "I want to modify the global chai_type, not create a local one"
        global chai_type
        chai_type = "Irnai"  # This MODIFIES the global variable
        # Without 'global', this would create a NEW local variable inside kitchen() function

    kitchen()  # Call the nested function which modifies the global variable

front_desk()  # Call the outer function
print("Final global chai: ", chai_type)  # This prints "Irnai" because global variable was modified

# Key Concepts:
# 1. 'global' is used to modify variables defined at the module level (global scope)
# 2. Without 'global', assignment creates a new local variable (doesn't modify global one)
# 3. 'global' can be used from any level of nested functions to modify global variables
# 4. Use 'nonlocal' for enclosing function scope, 'global' for module-level scope
# 5. You can READ global variables without 'global' keyword, but need it to MODIFY them