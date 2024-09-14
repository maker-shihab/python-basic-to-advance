# Data Structures (Lists, Tuples, Sets, Dictionaries)

## Overview

Data structures are used to store and organize data in Python. The most commonly used data structures are:

- Lists: Ordered, mutable collections.
- Tuples: Ordered, immutable collections.
- Sets: Unordered, mutable collections with no duplicate elements.
- Dictionaries: Unordered, mutable collections of key-value pairs.

## 1. Lists

A list is a collection of items in a particular order. Lists are mutable, which means you can modify their contents.

### Syntax:

```python
my_list = [item1, item2, item3]
```

### Example:

```python
fruits = ["apple", "orange", "banana", "cherry"]
print(fruits[0]) # Accessing the first item
fruits.append("orange") # Adding an item
fruits.remove("banana") # Removing an item
```

### Common List Operations:

- append(): Add an item to the end of the list.
- remove(): Remove the first occurrence of a value.
- pop(): Remove and return the last item or the item at the given index.
- sort(): Sort the list in ascending order.
- reverse(): Reverse the order of the list.

### Example of Operations:

```python
numbers = [1, 2, 3, 4, 5]
numbers.sort() # Sorts the list in place
print(numbers) # Output: [1, 2, 3, 4, 5]
```

## 2. Tuples

A tuple is similar to a list but is immutable, meaning it cannot be changed after it is created. Tuples are useful when you want to store data that should not be modified.

### Syntax

```python
my_tuple = (item1, item2, item3)
```

### Example:

```python
dimensions = (440, 50)
print(dimensions[0]) # Accessing the first item
```

Since tuples are immutable, you cannot modify their contents (e.g., you cannot `append()` or `remove()` items), but you can access and loop through them.

<b>Unpacking Tuples:</b>You can assign values in a tuple to multiple variables at once.

### Example:

```python
point = (10, 20)
x, y = point
print(x) # Output: 10
print(y) # Output: 20
```

## 3. Sets

A set is an unordered collection of unique items. Sets do not allow duplicate elements and are useful for performing mathematical set operations like union, intersection, etc.

### Syntax

```python
my_set = {item1, item2, item3}
```

### Example:

```python
unique_numbers = {1, 2, 3, 4, 2, 3, 5, 1} # Duplicates are automatically removed
print(unique_numbers) # Output: {1, 2, 3, 4, 5}
```

### Common Set Operations:

- `add()`: Add an element to the set.
- `remove()`: Remove an element from the set.
- `union()`: Return the union of two sets.
- `intersection()`: Return the intersection of two sets.

### Example of Set Operations:

```python
set_a = {1, 2, 3}
set_b = (3, 4, 5)

# Union: All unique elements from both sets
print(set_a.union(set_b)) # Output: {1, 2, 3, 4, 5}

# Intersection: Elements common to both sets
print(set_a.intersection(set_b)) # Output: {3}
```

## 4. Dictionaries

A dictionary is an unordered collection of key-value pairs. Each key must be unique, but the values can be duplicated. Dictionaries are mutable, meaning you can add, remove, and modify their contents.

### Syntax

```python
my_dist = {key1: value1, key2: value2, key3: value3}
```

### Example:

```python
person = {
  "name": "Shihab",
  "age": 25,
  "country": "Bangladesh"
}

print(person["name"]) # Accessing a value using a key
```

### Common Dictionary Operations:

- get(): Return the value for a key, or a default value if the key doesn't exist.
- items(): Return a view object with all key-value pairs.
- keys(): Return a view object with all the keys.
- values(): Return a view object with all the values.
- update(): Update the dictionary with key-value pairs from another dictionary.

### Example of Operations:

```python
person = {"name": "Shihab", "age": 25}

# Add or update a key-value pair
person["country"] = "Bangladesh"

# Remove a key-value pair
person.pop("age")

print(person) # Output: {'name': 'Shihab', 'country': 'Bangladesh'}
```
