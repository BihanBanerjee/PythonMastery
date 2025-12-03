def pour_chai(n: int):
    """
    Recursive function: A function that calls itself
    This function counts down from n to 0
    """
    print(n)
    if (n == 0):
        return  # Base case: stops the recursion
    pour_chai(n-1)  # Recursive call: function calls itself with n-1

# Test the function
pour_chai(5)