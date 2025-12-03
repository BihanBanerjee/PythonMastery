daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = (sale for sale in daily_sales if sale > 7)  # This is a generator comprehension
# It is a generator object. Generator objects are needed to be consumed since they are streaming this one by one.
# What the generator allows you to do is that you can use in-built methods like sum(), min(), max(), filter() etc. etc.
# sum() function --> You provide a iterable to it and automatically makes the sum of it.
# Using generator it will be a memory effcient operation since you are not throwing all the values in the memory. 
# The values are given one by one to the sum function. The stream of calues are fed to the sum function one by one.
# This becomes a memory efficient operation.
print(total_cups)

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)

"""
================================================================================
MEMORY EFFICIENCY WITH GENERATORS - DETAILED EXPLANATION
================================================================================

Without Generator (List Comprehension):
-----------------------------------------
total_cups = [sale for sale in daily_sales if sale > 7]  # [10, 12, 8, 9, 15]
result = sum(total_cups)

Memory usage: Stores ALL filtered values [10, 12, 8, 9, 15] in memory


With Generator (Generator Comprehension):
------------------------------------------
total_cups = (sale for sale in daily_sales if sale > 7)  # <generator object>
result = sum(total_cups)

Memory usage: Only ONE value in memory at a time


How It Works:
-------------
When you do sum(sale for sale in daily_sales if sale > 5):

1. Generator produces: 10 → sum adds it → discards from memory
2. Generator produces: 12 → sum adds it → discards from memory
3. Generator produces: 7 → sum adds it → discards from memory
4. Generator produces: 8 → sum adds it → discards from memory
5. Generator produces: 9 → sum adds it → discards from memory
6. Generator produces: 15 → sum adds it → discards from memory

Result: Only 1 number in memory at any moment, not all 6!


Real-World Impact:
------------------
Small dataset (your example):
- List: [10, 12, 7, 8, 9, 15] - negligible difference
- Generator: One value at a time - negligible difference

Large dataset (imagine millions of records):
# BAD - stores 1 million values in memory!
huge_list = [x * 2 for x in range(1_000_000)]
result = sum(huge_list)

# GOOD - only 1 value in memory at a time!
result = sum(x * 2 for x in range(1_000_000))


Key Point:
----------
Generators stream values one-by-one instead of storing everything in memory.
This is crucial when working with large datasets, file processing, or infinite sequences!
"""