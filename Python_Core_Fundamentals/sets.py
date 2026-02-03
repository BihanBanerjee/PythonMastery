# =============================================================================
# PYTHON SETS - Creating Sets Techniques
# =============================================================================
# Sets are MUTABLE, UNORDERED, and contain only UNIQUE elements
# Elements must be IMMUTABLE (hashable): strings, numbers, tuples

# -----------------------------------------------------------------------------
# 1. CREATING SETS - All Techniques
# -----------------------------------------------------------------------------

# Method 1: Using curly braces {} (most common)
set1 = {"a", "b", "c"}                   # Direct creation
set2 = {"a", "d", "e"}

# Method 2: Using set() constructor
empty_set = set()                        # ONLY way to create empty set ({} is dict!)
from_list = set([1, 2, 3, 2, 1])         # {1, 2, 3} - duplicates removed
from_tuple = set((1, 2, 3))              # {1, 2, 3}
from_string = set("hello")               # {'h', 'e', 'l', 'o'} - unique chars
from_range = set(range(5))               # {0, 1, 2, 3, 4}

# Method 3: Set comprehension
squares = {x**2 for x in range(1, 6)}    # {1, 4, 9, 16, 25}
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

# Method 4: From dictionary keys/values
my_dict = {"a": 1, "b": 2, "c": 3}
keys_set = set(my_dict.keys())           # {"a", "b", "c"}
values_set = set(my_dict.values())       # {1, 2, 3}

# Method 5: Using unpacking (Python 3.5+)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
combined = {*set_a, *set_b}              # {1, 2, 3, 4, 5}

# Method 6: From generator expression
gen_set = set(x * 2 for x in range(5))   # {0, 2, 4, 6, 8}

# Method 7: Frozen set (immutable set - can be used as dict key or set element)
frozen = frozenset([1, 2, 3])            # Immutable, hashable
nested_set = {frozenset([1, 2]), frozenset([3, 4])}  # Set of sets

# -----------------------------------------------------------------------------
# 2. SET OPERATIONS (using operators)
# -----------------------------------------------------------------------------
all_values = set1 | set2                 # Union: {'a', 'b', 'c', 'd', 'e'}
print(all_values)

common_values = set1 & set2              # Intersection: {'a'}
print(common_values)

only_in_set1 = set1 - set2               # Difference: {'b', 'c'}
print(only_in_set1)

symmetric_diff = set1 ^ set2             # Symmetric difference: {'b', 'c', 'd', 'e'}
print(symmetric_diff)                    # Elements in either but not both

# -----------------------------------------------------------------------------
# 3. SET METHODS (equivalent to operators above)
# -----------------------------------------------------------------------------
# union(), intersection(), difference(), symmetric_difference()
# These return NEW sets, don't modify originals
union_method = set1.union(set2)                          # Same as |
inter_method = set1.intersection(set2)                   # Same as &
diff_method = set1.difference(set2)                      # Same as -
sym_diff_method = set1.symmetric_difference(set2)        # Same as ^

# In-place versions (modify the set)
# set1.update(set2)                      # |= union in place
# set1.intersection_update(set2)         # &= intersection in place
# set1.difference_update(set2)           # -= difference in place
# set1.symmetric_difference_update(set2) # ^= symmetric diff in place

# -----------------------------------------------------------------------------
# 4. ADDING & REMOVING ELEMENTS
# -----------------------------------------------------------------------------
colors = {"red", "green"}

# Adding
colors.add("blue")                       # Add single element
colors.update(["yellow", "purple"])      # Add multiple elements (from iterable)

# Removing
colors.remove("red")                     # Removes element, KeyError if not found
colors.discard("orange")                 # Removes element, NO error if not found (SAFER)
popped = colors.pop()                    # Removes and returns arbitrary element
# colors.clear()                         # Removes all elements

# -----------------------------------------------------------------------------
# 5. SET COMPARISONS
# -----------------------------------------------------------------------------
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2, 3}

a.issubset(b)                            # True - a ⊆ b (or a <= b)
b.issuperset(a)                          # True - b ⊇ a (or b >= a)
a.isdisjoint({4, 5, 6})                  # True - no common elements
a == c                                   # True - same elements
a < b                                    # True - proper subset (a ⊂ b)

# -----------------------------------------------------------------------------
# 6. KEY POINTS TO REMEMBER
# -----------------------------------------------------------------------------
# - Sets are UNORDERED (no indexing, no slicing)
# - Elements must be IMMUTABLE (no lists or dicts as elements)
# - Use frozenset() for immutable sets
# - {} creates empty dict, not set! Use set() for empty set
# - Time Complexity: O(1) average for add, remove, lookup
# - Great for: removing duplicates, membership testing, set math