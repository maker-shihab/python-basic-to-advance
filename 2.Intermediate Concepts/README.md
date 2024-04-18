# Intermediate Concepts

- Data Structures (Lists, Tuples, Sets, Dictionaries)
- File Handling (read, write, append)
- Exception Handling (try, except, finally)
- Modules and Packages

## 1. Data Structures (Lists, Tuples, Sets, Dictionaries)

### Overview

Data structures are used to store and organize data in Python. The most commonly used data structures are:

- Lists: Ordered, mutable collections.
- Tuples: Ordered, immutable collections.
- Sets: Unordered, mutable collections with no duplicate elements.
- Dictionaries: Unordered, mutable collections of key-value pairs.

### 1.1 Lists

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

### Python List Methods

Python has many useful list methods that make it really easy to work with lists.

### Method Description

- append() Adds an item to the end of the list
- extend() Adds items of lists and other iterables to the end of the list
- insert() Inserts an item at the specified index
- remove() Removes the specified value from the list
- pop() Returns and removes item present at the given index
- clear() Removes all items from the list
- index() Returns the index of the first matched item
- count() Returns the count of the specified item in the list
- sort() Sorts the list in ascending/descending order
- reverse() Reverses the item of the list
- copy() Returns the shallow copy of the list

### Example of Operations:

```python
numbers = [1, 2, 3, 4, 5]
numbers.sort() # Sorts the list in place
print(numbers) # Output: [1, 2, 3, 4, 5]
```

## 1.2 Tuples

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

## 1.3 Sets

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

## 1.4 Dictionaries

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

## 2. File Handling (read, write, append)

### Overview

File handling in Python allows you to work with external files (text, CSV, etc.). The basic operations include reading from a file, writing to a file, and appending data. Python provides built-in functions like `open()`, `read()`, `write()`, and `close()` to work with files.

## 2.1 Opening and Closing Files

Before working with a file, you need to open it using the `open()` function. After you're done, it's good practice to close the file using the `close()` method to free up resources.

### Syntax

```python
file = open('filename', 'mode')
# Work with the file
file.close()
```

### File Modes:

- "r": Read (default mode). Opens the file for reading. The file must exist.
- "w": Write. Opens the file for writing. If the file already exists, it will be overwritten. If it doesn't exist, a new file will be created.
- "a": Append. Opens the file for appending new data at the end. If the file doesn't exist, a new file will be created.
- "r+": Read and write. The file must exist.
- "w+": Write and read. Overwrites the file if it exists or creates a new one.
- "a+": Append and read. Opens the file for appending and reading.

## 2.2 Reading Files

You can read the contents of a file using various methods like read(), readline(), or readlines().

- read(): Reads the entire file content as a string.
- readline(): Reads one line at a time.
- readlines(): Reads all lines into a list.

<b>Example: Reading the entire file content using</b> `read()`:

```python
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

<b>Example: Reading the file line by line using</b> `readline()`:

```python
file = open('example.txt', 'r')
line = file.readline()
while line:
  print(line, end="") # end='' prevents double new lines
  line = file.readline()
file.close()
```

<b>Example: Reading all lines into a list using</b> `readlines()`:

```python
file = open("example.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip()) # split() removes any trailing newlines
file.close()
```

## 2.3 Writing to a File

You can write data to a file using the `write()` method. If the file already exists, it will be overwritten unless you're in append mode.

<b>Example: Writing to a file using </b> `write()`:

```python
file = open("example.txt", "w")
file.write("Hello, world!\n")
file.write("This is a new file.")
file.close()
```
