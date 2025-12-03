def serve_chai():
    chai_type = 'Masala' # local scope. --> validation of this variable is just inside this function.
    print(f"Inside function {chai_type}")

chai_type = 'Green' # global scope. --> validation of this variable is inside and outside this function.
serve_chai()
print(f"Outside function {chai_type}")

# Local scope --> inside a particular function. the variable written isnide the function is not available outside the function.

def chai_counter():
    chai_order = "lemon" # Enclosing scope

    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_order)

    print_order()
    print("Outer: ", chai_order)

chai_order = "Tulsi" # Global
chai_counter()
print("Global :", chai_order)