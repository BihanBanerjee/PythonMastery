# =============================================================================
# PYTHON STRINGS - Complete Guide
# =============================================================================
# Strings are IMMUTABLE, ORDERED sequences of characters
# Strings are enclosed in single '', double "", or triple ''' """ quotes

# -----------------------------------------------------------------------------
# 1. CREATING STRINGS - All Techniques
# -----------------------------------------------------------------------------

# Method 1: Single quotes
s1 = 'Hello World'

# Method 2: Double quotes
s2 = "Hello World"

# Method 3: Triple quotes (multi-line strings)
s3 = """This is a
multi-line
string"""

s4 = '''Also works
with single
quotes'''

# Method 4: str() constructor
from_int = str(123)                      # "123"
from_float = str(3.14)                   # "3.14"
from_list = str([1, 2, 3])               # "[1, 2, 3]"

# Method 5: Empty string
empty = ""
empty2 = str()

# Method 6: Raw strings (ignores escape characters)
raw = r"C:\new\folder"                   # Backslashes treated literally

# Method 7: Bytes to string
byte_str = b"hello".decode('utf-8')      # "hello"

# -----------------------------------------------------------------------------
# 2. INDEXING & SLICING
# -----------------------------------------------------------------------------
string1 = "JayShreeRam"

print(string1)

print("--" * 20)
print(f"First Word: {string1[0:3]}")     # "Jay"
print(f"First Word: {string1[:3]}")      # More pythonic: avoid 0th index

print(f"Last Word: {string1[8:]}")       # "Ram"

# Negative indexing
print(f"Last char: {string1[-1]}")       # "m"
print(f"Last 3 chars: {string1[-3:]}")   # "Ram"

print("--" * 20)
print(f"Reversing: {string1[::-1]}")     # "maReerhSyaJ"

# String is NOT mutable - creates new object
string1 = string1[::-1]                  # string1 now refers to new string object
print(string1)

# Slicing syntax: string[start:stop:step]
text = "Python Programming"
text[0:6]                                # "Python"
text[7:]                                 # "Programming"
text[::2]                                # "Pto rgamn" (every 2nd char)
text[::-1]                               # Reverse string

# -----------------------------------------------------------------------------
# 3. STRING METHODS - Case Conversion
# -----------------------------------------------------------------------------
sample = "Hello World"

sample.lower()                           # "hello world"
sample.upper()                           # "HELLO WORLD"
sample.capitalize()                      # "Hello world" (first char upper)
sample.title()                           # "Hello World" (each word capitalized)
sample.swapcase()                        # "hELLO wORLD"
sample.casefold()                        # "hello world" (aggressive lowercase for comparison)

# -----------------------------------------------------------------------------
# 4. STRING METHODS - Search & Find
# -----------------------------------------------------------------------------
text = "Hello World, Hello Python"

# find() - returns first index, -1 if not found
text.find("Hello")                       # 0
text.find("Hello", 5)                    # 13 (start search from index 5)
text.find("Java")                        # -1

# rfind() - search from right
text.rfind("Hello")                      # 13

# index() - like find(), but raises ValueError if not found
text.index("World")                      # 6
# text.index("Java")                     # ValueError!

# count() - count occurrences
text.count("Hello")                      # 2
text.count("l")                          # 5

# startswith() / endswith()
text.startswith("Hello")                 # True
text.endswith("Python")                  # True
text.startswith(("Hello", "Hi"))         # True (tuple of prefixes)

# in operator - membership test
"World" in text                          # True
"Java" not in text                       # True

# -----------------------------------------------------------------------------
# 5. STRING METHODS - Modify (returns new string)
# -----------------------------------------------------------------------------
text = "  Hello World  "

# strip() - remove whitespace (or specified chars)
text.strip()                             # "Hello World"
text.lstrip()                            # "Hello World  "
text.rstrip()                            # "  Hello World"
"###Hello###".strip("#")                 # "Hello"

# replace()
"Hello World".replace("World", "Python") # "Hello Python"
"aaa".replace("a", "b", 2)               # "bba" (max 2 replacements)

# split() - string to list
"a,b,c,d".split(",")                     # ['a', 'b', 'c', 'd']
"Hello World".split()                    # ['Hello', 'World'] (default: whitespace)
"a,b,c,d".split(",", 2)                  # ['a', 'b', 'c,d'] (max 2 splits)

# rsplit() - split from right
"a,b,c,d".rsplit(",", 2)                 # ['a,b', 'c', 'd']

# splitlines() - split by line breaks
"Line1\nLine2\nLine3".splitlines()       # ['Line1', 'Line2', 'Line3']

# join() - list to string
",".join(['a', 'b', 'c'])                # "a,b,c"
" ".join(['Hello', 'World'])             # "Hello World"
"".join(['H', 'e', 'l', 'l', 'o'])       # "Hello"

# partition() - split into 3 parts (before, separator, after)
"hello@world.com".partition("@")         # ('hello', '@', 'world.com')

# -----------------------------------------------------------------------------
# 6. STRING METHODS - Padding & Alignment
# -----------------------------------------------------------------------------
text = "Hello"

# center(), ljust(), rjust() - pad to width
text.center(11)                          # "   Hello   "
text.center(11, "-")                     # "---Hello---"
text.ljust(10)                           # "Hello     "
text.rjust(10)                           # "     Hello"

# zfill() - pad with zeros (for numbers)
"42".zfill(5)                            # "00042"
"-42".zfill(5)                           # "-0042"

# expandtabs() - replace tabs with spaces
"Hello\tWorld".expandtabs(4)             # "Hello   World"

# -----------------------------------------------------------------------------
# 7. STRING METHODS - Validation (return bool)
# -----------------------------------------------------------------------------
# Character type checks
"hello".isalpha()                        # True (all letters)
"12345".isdigit()                        # True (all digits)
"12345".isnumeric()                      # True (numeric chars)
"hello123".isalnum()                     # True (letters or digits)
"   ".isspace()                          # True (all whitespace)

# Case checks
"HELLO".isupper()                        # True
"hello".islower()                        # True
"Hello World".istitle()                  # True (title case)

# Other checks
"hello".isascii()                        # True (all ASCII)
"print".isidentifier()                   # True (valid Python identifier)
"hello".isprintable()                    # True (all printable)
"".isspace()                             # False (empty string)

# -----------------------------------------------------------------------------
# 8. STRING FORMATTING
# -----------------------------------------------------------------------------
name = "Alice"
age = 30
price = 49.99

# Method 1: f-strings (Python 3.6+) - RECOMMENDED
greeting = f"Hello, {name}! You are {age} years old."
formatted = f"Price: ${price:.2f}"       # "Price: $49.99"

# f-string expressions
f"{2 + 2}"                               # "4"
f"{name.upper()}"                        # "ALICE"
f"{age:05d}"                             # "00030" (pad with zeros)

# Method 2: format() method
"Hello, {}!".format(name)                # "Hello, Alice!"
"Hello, {0}! {0} is {1}".format(name, age)  # Positional
"Hello, {name}!".format(name="Bob")      # Keyword

# Format specifiers
"{:>10}".format("hi")                    # "        hi" (right align)
"{:<10}".format("hi")                    # "hi        " (left align)
"{:^10}".format("hi")                    # "    hi    " (center)
"{:.2f}".format(3.14159)                 # "3.14" (2 decimal places)
"{:,}".format(1000000)                   # "1,000,000" (thousands separator)
"{:b}".format(10)                        # "1010" (binary)
"{:x}".format(255)                       # "ff" (hex)

# Method 3: % operator (older style)
"Hello, %s!" % name                      # "Hello, Alice!"
"Age: %d, Price: %.2f" % (age, price)    # "Age: 30, Price: 49.99"

# -----------------------------------------------------------------------------
# 9. ESCAPE CHARACTERS
# -----------------------------------------------------------------------------
# \n  - newline
# \t  - tab
# \\  - backslash
# \'  - single quote
# \"  - double quote
# \r  - carriage return
# \b  - backspace

print("Line1\nLine2")                    # Two lines
print("Col1\tCol2")                      # Tab separated
print("Path: C:\\Users\\Name")           # Backslashes

# Raw strings ignore escapes
print(r"C:\new\folder")                  # Prints literally

# -----------------------------------------------------------------------------
# 10. STRING OPERATIONS
# -----------------------------------------------------------------------------
s1 = "Hello"
s2 = "World"

# Concatenation
combined = s1 + " " + s2                 # "Hello World"

# Repetition
repeated = s1 * 3                        # "HelloHelloHello"

# Length
len(s1)                                  # 5

# Membership
"ell" in s1                              # True

# Comparison (lexicographic)
"apple" < "banana"                       # True
"Hello" == "hello"                       # False (case sensitive)
"Hello".lower() == "hello".lower()       # True

# Iteration
for char in "Hello":
    print(char)

# Enumerate
for idx, char in enumerate("Hello"):
    print(f"{idx}: {char}")

# -----------------------------------------------------------------------------
# 11. USEFUL STRING PATTERNS
# -----------------------------------------------------------------------------
# Check if string is empty
s = ""
if not s:                                # Pythonic way
    print("Empty")

# Remove specific characters
"hello123world".translate(str.maketrans('', '', '0123456789'))  # "helloworld"

# Check palindrome
text = "radar"
is_palindrome = text == text[::-1]       # True

# Count words
sentence = "Hello World Python"
word_count = len(sentence.split())       # 3

# Reverse words
" ".join("Hello World".split()[::-1])    # "World Hello"

# Check if all words start with uppercase
"Hello World".istitle()                  # True

# Create character frequency
from collections import Counter
Counter("hello")                         # {'l': 2, 'h': 1, 'e': 1, 'o': 1}

# -----------------------------------------------------------------------------
# 12. KEY POINTS TO REMEMBER
# -----------------------------------------------------------------------------
# - Strings are IMMUTABLE (cannot be changed in place)
# - Strings are SEQUENCES (ordered, indexable, iterable)
# - Use f-strings for formatting (Python 3.6+)
# - String methods return NEW strings (don't modify original)
# - Use raw strings r"..." for regex and file paths
# - Single, double, and triple quotes all create strings
# - Time Complexity:
#   * Access by index: O(1)
#   * Slicing: O(k) where k is slice length
#   * Concatenation with +: O(n+m)
#   * join(): O(n) - more efficient for multiple strings
#   * find/index: O(n)
#   * replace: O(n)
# - For heavy string manipulation, consider using list then join()
