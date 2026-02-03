# =============================================================================
# PYTHON DICTIONARIES - Complete Guide
# =============================================================================
# Dictionaries are MUTABLE, ORDERED (Python 3.7+), and store KEY-VALUE pairs
# Keys must be IMMUTABLE and UNIQUE (strings, numbers, tuples)
# Values can be any type and can be duplicated

# -----------------------------------------------------------------------------
# 1. CREATING DICTIONARIES
# -----------------------------------------------------------------------------
empty_dict = {}                          # Empty dictionary
empty_dict2 = dict()                     # Using dict() constructor

# Basic dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using dict() with keyword arguments
person2 = dict(name="Bob", age=25, city="Boston")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_tuples = dict(pairs)                # {"a": 1, "b": 2, "c": 3}

# From two lists using zip
keys = ["x", "y", "z"]
values = [10, 20, 30]
from_zip = dict(zip(keys, values))       # {"x": 10, "y": 20, "z": 30}

# Using dict.fromkeys() - all keys get same value
default_dict = dict.fromkeys(["a", "b", "c"], 0)  # {"a": 0, "b": 0, "c": 0}

# Nested dictionary
nested = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}

# -----------------------------------------------------------------------------
# 2. ACCESSING VALUES
# -----------------------------------------------------------------------------
student = {"name": "John", "grade": "A", "score": 95}

# Using square brackets (raises KeyError if key doesn't exist)
name = student["name"]                   # "John"
# missing = student["age"]               # KeyError!

# Using get() - returns None (or default) if key doesn't exist (SAFER)
grade = student.get("grade")             # "A"
age = student.get("age")                 # None (no error)
age = student.get("age", 18)             # 18 (custom default)

# Accessing nested dictionary
nested = {"outer": {"inner": "value"}}
inner_val = nested["outer"]["inner"]     # "value"
# Safe nested access
inner_safe = nested.get("outer", {}).get("inner", "default")

# -----------------------------------------------------------------------------
# 3. ADDING & UPDATING ELEMENTS
# -----------------------------------------------------------------------------
data = {"a": 1, "b": 2}

# Add/Update single key-value pair
data["c"] = 3                            # Add new: {"a": 1, "b": 2, "c": 3}
data["a"] = 100                          # Update existing: {"a": 100, "b": 2, "c": 3}

# update() - add/update multiple key-value pairs at once
data.update({"d": 4, "e": 5})            # Add multiple
data.update(a=200, b=300)                # Update using keyword args

# setdefault() - returns value if key exists, else sets and returns default
data.setdefault("f", 6)                  # Sets "f": 6 and returns 6
data.setdefault("a", 999)                # Returns 200 (key exists, doesn't change)

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2                   # {"a": 1, "b": 2, "c": 3, "d": 4}
# dict1 |= dict2                         # In-place merge

# -----------------------------------------------------------------------------
# 4. REMOVING ELEMENTS
# -----------------------------------------------------------------------------
info = {"name": "Alice", "age": 30, "city": "NYC", "job": "Engineer"}

# pop() - removes key and RETURNS its value (KeyError if not found)
age = info.pop("age")                    # Returns 30, key removed
missing = info.pop("salary", "N/A")      # Returns "N/A" (default, no error)

# popitem() - removes and returns LAST inserted key-value pair (LIFO)
last_item = info.popitem()               # Returns ("job", "Engineer")

# del - removes key (KeyError if not found)
del info["city"]                         # Removes "city" key

# clear() - removes ALL items
# info.clear()                           # {}

# -----------------------------------------------------------------------------
# 5. DICTIONARY VIEWS (keys, values, items)
# -----------------------------------------------------------------------------
product = {"name": "Laptop", "price": 999, "stock": 50}

# keys() - returns view of all keys
all_keys = product.keys()                # dict_keys(['name', 'price', 'stock'])

# values() - returns view of all values
all_values = product.values()            # dict_values(['Laptop', 999, 50])

# items() - returns view of all key-value tuples
all_items = product.items()              # dict_items([('name', 'Laptop'), ...])

# Convert views to lists if needed
keys_list = list(product.keys())         # ['name', 'price', 'stock']

# Views are DYNAMIC - they update when dict changes
product["brand"] = "Dell"
# all_keys now includes 'brand' automatically!

# -----------------------------------------------------------------------------
# 6. CHECKING MEMBERSHIP
# -----------------------------------------------------------------------------
config = {"debug": True, "version": "1.0", "timeout": 30}

# Check if KEY exists (default behavior)
has_debug = "debug" in config            # True
no_port = "port" not in config           # True

# Check if VALUE exists (need to use .values())
has_true = True in config.values()       # True

# -----------------------------------------------------------------------------
# 7. ITERATING OVER DICTIONARIES
# -----------------------------------------------------------------------------
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Iterate over keys (default)
for name in scores:
    print(name)                          # Alice, Bob, Charlie

# Iterate over keys explicitly
for name in scores.keys():
    print(name)

# Iterate over values
for score in scores.values():
    print(score)                         # 95, 87, 92

# Iterate over key-value pairs (MOST COMMON)
for name, score in scores.items():
    print(f"{name}: {score}")

# With enumerate (if you need index)
for idx, (name, score) in enumerate(scores.items()):
    print(f"{idx}. {name}: {score}")

# -----------------------------------------------------------------------------
# 8. DICTIONARY COMPREHENSIONS
# -----------------------------------------------------------------------------
# Basic: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Transform existing dictionary
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
doubled = {k: v * 2 for k, v in prices.items()}

# Swap keys and values
swapped = {v: k for k, v in prices.items()}  # {1.0: "apple", ...}

# Filter dictionary
expensive = {k: v for k, v in prices.items() if v > 1.0}

# From two lists
names = ["a", "b", "c"]
nums = [1, 2, 3]
combined = {k: v for k, v in zip(names, nums)}

# -----------------------------------------------------------------------------
# 9. COPYING DICTIONARIES
# -----------------------------------------------------------------------------
original = {"a": 1, "b": {"nested": 2}}

# SHALLOW COPY - nested objects share reference
shallow1 = original.copy()               # Using copy()
shallow2 = dict(original)                # Using dict()
shallow3 = {**original}                  # Using unpacking

# DEEP COPY - fully independent copy
import copy
deep = copy.deepcopy(original)

# Shallow copy pitfall (same as lists!)
original["b"]["nested"] = 999
# shallow1["b"]["nested"] is also 999!
# deep["b"]["nested"] is still 2

# -----------------------------------------------------------------------------
# 10. MERGING & UNPACKING
# -----------------------------------------------------------------------------
defaults = {"color": "blue", "size": "medium", "price": 10}
custom = {"color": "red", "quantity": 5}

# Using ** unpacking (later values override)
merged = {**defaults, **custom}          # color is "red"

# Using update() - modifies in place
defaults.update(custom)

# Using | operator (Python 3.9+)
merged = defaults | custom

# Unpacking in function calls
def greet(name, age):
    print(f"{name} is {age}")

person = {"name": "Alice", "age": 30}
greet(**person)                          # Unpacks to greet(name="Alice", age=30)

# -----------------------------------------------------------------------------
# 11. DEFAULT VALUES & HANDLING MISSING KEYS
# -----------------------------------------------------------------------------
# Using get() with default
count = {}
word = "hello"
count[word] = count.get(word, 0) + 1     # Initialize to 0 if missing

# Using setdefault() for mutable defaults
groups = {}
groups.setdefault("fruits", []).append("apple")
groups.setdefault("fruits", []).append("banana")
# groups = {"fruits": ["apple", "banana"]}

# Using collections.defaultdict (auto-creates default values)
from collections import defaultdict

# Default to 0 for counting
word_count = defaultdict(int)
word_count["hello"] += 1                 # No KeyError, auto-initializes to 0

# Default to empty list for grouping
grouped = defaultdict(list)
grouped["fruits"].append("apple")        # No KeyError, auto-creates []

# Default to set
unique_items = defaultdict(set)
unique_items["category"].add("item1")

# -----------------------------------------------------------------------------
# 12. ORDERED DICT & COUNTER (from collections)
# -----------------------------------------------------------------------------
from collections import OrderedDict, Counter

# OrderedDict - maintains insertion order (less needed in Python 3.7+)
# Useful for: move_to_end(), comparing order
od = OrderedDict([("a", 1), ("b", 2)])
od.move_to_end("a")                      # Move "a" to end

# Counter - count occurrences
text = "mississippi"
letter_count = Counter(text)             # {'i': 4, 's': 4, 'p': 2, 'm': 1}

# Counter methods
letter_count.most_common(2)              # [('i', 4), ('s', 4)] - top 2
Counter("aab") + Counter("bcc")          # Add counters: {'a': 2, 'b': 2, 'c': 2}
Counter("aab") - Counter("ab")           # Subtract: {'a': 1}

# Count from list
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_freq = Counter(words)               # {'apple': 3, 'banana': 2, 'cherry': 1}

# -----------------------------------------------------------------------------
# 13. USEFUL PATTERNS & TRICKS
# -----------------------------------------------------------------------------
# Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

# Group items by a key
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"}
]
by_grade = defaultdict(list)
for s in students:
    by_grade[s["grade"]].append(s["name"])
# {"A": ["Alice", "Charlie"], "B": ["Bob"]}

# Dictionary as switch/case (before Python 3.10 match)
def get_day_type(day):
    return {
        "Monday": "Weekday",
        "Saturday": "Weekend",
        "Sunday": "Weekend"
    }.get(day, "Weekday")

# Flatten nested dict keys
nested = {"a": {"b": {"c": 1}}}
# Access safely with reduce or custom function

# Sort dictionary by value
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
# {"Alice": 95, "Charlie": 92, "Bob": 87}

# Sort dictionary by key
sorted_by_key = dict(sorted(scores.items()))

# -----------------------------------------------------------------------------
# 14. KEY POINTS TO REMEMBER
# -----------------------------------------------------------------------------
# - Dictionaries are MUTABLE
# - Keys must be IMMUTABLE (str, int, float, tuple) and UNIQUE
# - Values can be ANY type and can be duplicated
# - Dictionaries are ORDERED (insertion order preserved, Python 3.7+)
# - Time Complexities (average case with good hash):
#   * Access by key: O(1)
#   * Insert: O(1)
#   * Delete: O(1)
#   * Search by key: O(1)
#   * Search by value: O(n)
# - Use get() instead of [] to avoid KeyError
# - Use defaultdict for automatic default values
# - Use Counter for counting occurrences
# - Dictionary comprehensions are Pythonic and efficient
# - Be careful with shallow vs deep copy for nested dicts
# - Views (keys, values, items) are dynamic and memory-efficient
