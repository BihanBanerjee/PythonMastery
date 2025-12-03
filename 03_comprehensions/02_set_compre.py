favorite_chais = [
    'Elaichi chai',
    'Ginger chai',
    'Tulsi chai',
    'Elaichi chai',
    'Ginger chai',
    'Cardamom chai',
]

unique_chai = {chai for chai in favorite_chais} # since we have given curly braces, automatically we dont have to write any if condition for filtering out the unique entries. Automatically the unique chais will come to me.
print(unique_chai)

unique_chai2 = {chai for chai in favorite_chais if len(chai) >= 12}
print(unique_chai2)



recipes = {
    'Masala Chai': ['ginger', 'cardamom', 'clove'],
    'Elaichi Chai': ['ginger', 'cardamom', 'clove'],
    'Spicy Chai': ['ginger', 'black pepper', 'clove'],
}

print(recipes.keys())
print(recipes.values())

unique_spices = { spice for ingredients in recipes.values() for spice in ingredients }
print(unique_spices)

"""
Curly Braces {} in Python:
Dictionary - key-value pairs
chai_dict = {'masala': 80, 'ginger': 60}  # Dictionary
Set - single values (no duplicates)
chai_set = {'masala', 'ginger', 'kadak'}  # Set
Empty curly braces {} = Dictionary (not set!)
empty_dict = {}           # Empty dictionary
empty_set = set()         # Empty set (must use set())
Quick visual:
# Dictionary - has colons (:)
{'key': 'value'}

# Set - no colons, just values
{'value1', 'value2'}
Key differences:
Dictionary: {'name': 'chai', 'price': 50} - has : between key and value
Set: {'chai', 'coffee', 'tea'} - just comma-separated values, no duplicates
Empty: {} is a dict, set() is a set
You nailed it! The presence or absence of the colon (:) is what tells Python whether it's a dictionary or a set.
"""




"""
Lists []
Mutable: Can be modified after creation
Ordered: Elements maintain insertion order
Allows duplicates: Can have repeated values
Syntax: my_list = [1, 2, 3, 2]
items = [1, 2, 3]
items.append(4)      # ✓ Works
items[0] = 10        # ✓ Works


Tuples ()
Immutable: Cannot be modified after creation
Ordered: Elements maintain insertion order
Allows duplicates: Can have repeated values
Syntax: my_tuple = (1, 2, 3, 2)
items = (1, 2, 3)
items.append(4)      # ✗ Error
items[0] = 10        # ✗ Error



Sets {}
Mutable: Can be modified after creation
Unordered: No guaranteed order (Python 3.7+ maintains insertion order as implementation detail)
No duplicates: Automatically removes duplicates
Syntax: my_set = {1, 2, 3}
items = {1, 2, 3, 2}  # Result: {1, 2, 3}
items.add(4)          # ✓ Works
items[0]              # ✗ Error (no indexing)


Quick Comparison
Feature	List	Tuple	Set
Mutable	✓	    ✗	    ✓
Ordered	✓	    ✓	    ✗*
Duplicates	✓	✓	    ✗
Indexed	✓	    ✓	    ✗
Use case	General collection	Immutable records	Unique items, fast lookup
When to use which:
List: Default choice for ordered collections you'll modify
Tuple: Fixed data like coordinates (x, y), dictionary keys, function return values
Set: Remove duplicates, membership testing (in), mathematical operations (union, intersection)

"""