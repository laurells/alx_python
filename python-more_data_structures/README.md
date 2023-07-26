# Python Data Structures and Functions

This README provides an overview of some important Python data structures and functions, including sets, dictionaries, lambda functions, and the `map`, `reduce`, and `filter` functions.

## Sets

### What are sets and how to use them?

Sets are unordered collections of unique elements in Python. They are defined using curly braces `{}` or the `set()` constructor.

```python
# Creating a set
my_set = {1, 2, 3}
```

### Common methods of sets and how to use them:

1. `add()`: Adds an element to the set.
2. `remove()`: Removes an element from the set. Raises an error if the element is not present.
3. `discard()`: Removes an element from the set if it exists. No error is raised if the element is not found.
4. `union()`: Returns the union of two sets.
5. `intersection()`: Returns the intersection of two sets.
6. `difference()`: Returns the difference between two sets.

### When to use sets versus lists?

Use sets when you need to store a collection of unique elements and don't require a specific order. Sets are more efficient for membership testing due to their hashing property.

### How to iterate into a set?

You can iterate through a set using a for loop:

```python
my_set = {1, 2, 3}
for item in my_set:
    print(item)
```

## Dictionaries

### What are dictionaries and how to use them?

Dictionaries are key-value pairs, where each key is unique and mapped to a corresponding value. They are defined using curly braces `{}` and colons `:` to separate keys and values.

```python
# Creating a dictionary
my_dict = {'name': 'John', 'age': 30}
```

### When to use dictionaries versus lists or sets?

Use dictionaries when you need to store data in key-value pairs for easy and efficient retrieval based on keys. Lists are used for ordered collections, and sets are used for unordered collections of unique elements.

### What is a key in a dictionary?

A key in a dictionary is a unique identifier for each value stored in the dictionary.

### How to iterate into a dictionary?

You can iterate through a dictionary using a for loop:

```python
my_dict = {'name': 'John', 'age': 30}
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

## Lambda Functions

### What is a lambda function?

A lambda function is an anonymous, one-line function defined using the `lambda` keyword. They are useful for creating small, throwaway functions without naming them.

```python
# Creating a lambda function that adds two numbers
add = lambda x, y: x + y
```

## Map, Reduce, and Filter Functions

### What is `map`, `reduce`, and `filter`?

These are higher-order functions in Python used to perform operations on iterables like lists or sets.

1. `map`: Applies a function to each item in an iterable and returns an iterator with the results.
2. `reduce`: Performs a rolling computation on an iterable to reduce it to a single value.
3. `filter`: Filters elements from an iterable based on a given function, returning an iterator with the filtered elements.

```python
# Example usage of map, reduce, and filter
numbers = [1, 2, 3, 4, 5]

# Map: Doubles each number in the list
result_map = list(map(lambda x: x * 2, numbers))

# Reduce: Calculates the product of all numbers in the list
from functools import reduce
result_reduce = reduce(lambda x, y: x * y, numbers)

# Filter: Filters even numbers from the list
result_filter = list(filter(lambda x: x % 2 == 0, numbers))
```

By understanding these concepts, you'll have a better understanding of Python data structures and functions, allowing you to use them effectively in your code. Happy coding!