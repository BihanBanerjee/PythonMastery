# =============================================================================
# PYTHON TUPLES - Complete Guide
# =============================================================================
# Tuples are IMMUTABLE, ORDERED, and allow DUPLICATE elements
# Tuples can contain mixed data types

# -----------------------------------------------------------------------------
# 1. CREATING TUPLES - All Techniques
# -----------------------------------------------------------------------------

# Method 1: Using parentheses () (most common)
t = ("hello", 1, "hi", True, 3.14, {"Pi": 3.14})

# Method 2: Without parentheses (tuple packing)
coords = 10, 20, 30                      # (10, 20, 30)

# Method 3: Using tuple() constructor
from_list = tuple([1, 2, 3])             # (1, 2, 3)
from_string = tuple("hello")             # ('h', 'e', 'l', 'l', 'o')
from_range = tuple(range(5))             # (0, 1, 2, 3, 4)
empty_tuple = tuple()                    # ()

# Method 4: Single element tuple (MUST have trailing comma!)
single = (42,)                           # Correct: (42,)
not_tuple = (42)                         # Wrong: this is just int 42!

# Method 5: Empty tuple
empty1 = ()
empty2 = tuple()

# Method 6: Nested tuples
nested = ((1, 2), (3, 4), (5, 6))

# Method 7: Generator to tuple
gen_tuple = tuple(x**2 for x in range(5))  # (0, 1, 4, 9, 16)

# -----------------------------------------------------------------------------
# 2. ACCESSING ELEMENTS (Indexing & Slicing)
# -----------------------------------------------------------------------------
colors = ("red", "green", "blue", "yellow", "purple")

# Positive indexing (starts from 0)
first = colors[0]                        # "red"
third = colors[2]                        # "blue"

# Negative indexing (starts from -1 at the end)
last = colors[-1]                        # "purple"
second_last = colors[-2]                 # "yellow"

# Slicing: tuple[start:stop:step] (stop is exclusive)
first_three = colors[0:3]                # ("red", "green", "blue")
last_two = colors[-2:]                   # ("yellow", "purple")
every_second = colors[::2]               # ("red", "blue", "purple")
reversed_tuple = colors[::-1]            # Reverses the tuple

# -----------------------------------------------------------------------------
# 3. TUPLE UNPACKING (Very Pythonic!)
# -----------------------------------------------------------------------------
# Basic unpacking
(v1, v2, v3, v4, v5, v6) = t
print(v1)  # hello
print(v2)  # 1
print(v3)  # hi
print(v4)  # True
print(v5)  # 3.14
print(v6)  # {'Pi': 3.14}

# Unpacking without parentheses
x, y, z = (1, 2, 3)

# Swapping variables (Most Pythonic way!)
quant1, quant2 = 12, 35
print(f"Ratio of quantities: {quant1} : {quant2}")

quant1, quant2 = quant2, quant1  # Most pythonic way to swap the variables
print(f"Ratio of quantities: {quant1} : {quant2}")

# Extended unpacking with * (Python 3+)
first, *middle, last = (1, 2, 3, 4, 5)
# first = 1, middle = [2, 3, 4], last = 5

head, *tail = (1, 2, 3, 4, 5)
# head = 1, tail = [2, 3, 4, 5]

*init, last = (1, 2, 3, 4, 5)
# init = [1, 2, 3, 4], last = 5

# Ignoring values with underscore
x, _, z = (1, 2, 3)                      # Ignore middle value
x, *_, z = (1, 2, 3, 4, 5)               # Ignore all middle values

# -----------------------------------------------------------------------------
# 4. TUPLE METHODS (Only 2 methods!)
# -----------------------------------------------------------------------------
numbers = (1, 2, 3, 2, 4, 2, 5, 2)

# count() - returns number of occurrences
count_2 = numbers.count(2)               # 4

# index() - returns first index of value (raises ValueError if not found)
idx = numbers.index(2)                   # 1
# idx = numbers.index(2, 2)              # Start from index 2, returns 3

# -----------------------------------------------------------------------------
# 5. MEMBERSHIP & ITERATION
# -----------------------------------------------------------------------------
isAvailable = "hello" in t               # True
print(isAvailable)

not_in = "world" not in t                # True

# Iterating
for item in t:
    print(item)

# With index using enumerate
for idx, item in enumerate(t):
    print(f"{idx}: {item}")

# -----------------------------------------------------------------------------
# 6. TUPLE OPERATIONS
# -----------------------------------------------------------------------------
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation (creates new tuple)
combined = t1 + t2                       # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = t1 * 3                        # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Length
length = len(t1)                         # 3

# Min/Max/Sum (for numeric tuples)
nums = (5, 2, 8, 1, 9)
min(nums)                                # 1
max(nums)                                # 9
sum(nums)                                # 25

# Comparison (element by element)
(1, 2, 3) < (1, 2, 4)                    # True (compares third element)
(1, 2, 3) == (1, 2, 3)                   # True

# -----------------------------------------------------------------------------
# 7. CONVERTING TUPLES
# -----------------------------------------------------------------------------
my_tuple = (1, 2, 3)

# Tuple to list (for modification)
my_list = list(my_tuple)                 # [1, 2, 3]
my_list.append(4)
my_tuple = tuple(my_list)                # (1, 2, 3, 4)

# Tuple to set (removes duplicates)
my_set = set((1, 2, 2, 3))               # {1, 2, 3}

# Tuple to string
str_tuple = ('H', 'e', 'l', 'l', 'o')
joined = ''.join(str_tuple)              # "Hello"

# -----------------------------------------------------------------------------
# 8. NAMED TUPLES (from collections)
# -----------------------------------------------------------------------------
from collections import namedtuple

# Define a named tuple type
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')  # Space-separated also works

# Create instances
p1 = Point(10, 20)
person = Person("Alice", 30, "NYC")

# Access by name (more readable!)
print(p1.x, p1.y)                        # 10 20
print(person.name)                       # Alice

# Still works like regular tuple
print(p1[0], p1[1])                      # 10 20

# Convert to dict
person._asdict()                         # {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Create with defaults (Python 3.7+)
Point3D = namedtuple('Point3D', ['x', 'y', 'z'], defaults=[0])
p = Point3D(1, 2)                        # Point3D(x=1, y=2, z=0)

# -----------------------------------------------------------------------------
# 9. TUPLES AS DICTIONARY KEYS
# -----------------------------------------------------------------------------
# Tuples are hashable (immutable) so they can be dict keys!
locations = {
    (0, 0): "Origin",
    (1, 0): "East",
    (0, 1): "North"
}
print(locations[(0, 0)])                 # "Origin"

# Lists CANNOT be dict keys (mutable, unhashable)
# {[1, 2]: "value"}                      # TypeError!

# -----------------------------------------------------------------------------
# 10. TUPLES IN FUNCTION RETURNS
# -----------------------------------------------------------------------------
def get_stats(numbers):
    """Return multiple values as tuple"""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Unpack the returned tuple
minimum, maximum, average = get_stats([1, 2, 3, 4, 5])

# Or keep as tuple
stats = get_stats([1, 2, 3, 4, 5])       # (1, 5, 3.0)

# -----------------------------------------------------------------------------
# 11. KEY POINTS TO REMEMBER
# -----------------------------------------------------------------------------
# - Tuples are IMMUTABLE (cannot be changed after creation)
# - Tuples are ORDERED and allow DUPLICATES
# - Tuples are HASHABLE (can be dict keys, set elements)
# - Single element tuple needs trailing comma: (42,)
# - Tuples are slightly FASTER than lists
# - Tuples use LESS MEMORY than lists
# - Use tuples for:
#   * Fixed collections that shouldn't change
#   * Dictionary keys
#   * Function return values (multiple returns)
#   * Unpacking and swapping variables
# - Time Complexity:
#   * Access by index: O(1)
#   * Search (in operator): O(n)
#   * count() and index(): O(n)
# - Only 2 methods: count() and index()