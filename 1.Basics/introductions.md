# Basics

## Overview

This section covers the basic building blocks of Python. Here, you’ll find explanations and code examples of:

- Variables and Data Types
- Conditionals
- Loops
- Functions

## Concepts

### 1. Variables | Data Types

- Variables store data values.

```python
  varInt = 10;
  varString = "Hello, I'm Shihab!";
  varFloat = 10.5;
  varBoolean = False;
  varList = ["Maker", 25, 5.5, "Developer"];
  varTuple = ("Maker", 25, 5.5, "Developer");
  varDict = { "name": "Maker", "age": 25 } #key value pair
```

### 1.2 Input/Output

### Overview

In Python, Input/Output (I/O) refers to the operations of taking input from the user and providing output to the user. Python provides several functions to handle these operations.

### Input in Python

The `input()` function is used to get input from the user. The input is always returned as a string, so if you need a different data type, you must convert it.

### Syntax:

```python
input(prompt)
```

### Example

```python
name = input("Enter your name: ");
print(name);
```

### Type Casting Input:

To get input as a different data type (e.g., integer), you can use type conversion functions like int(), float(), etc.

```python
age = int(input("Enter your Age: "));
print(age);
```

### Output in Python

The print() function is used to display output to the user.

### Syntax:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False);
```

### Example:

```python
print("Hello World!");
print("Pyton", "is", "fun", sep=" - ", end="\n");
```

### Formatted Output

You can format the output using various methods such as f-strings, format(), or string concatenation.

### Example (f-string):

```python
name = "Shiahb";
age = 25;
print(f"My name is {name}, I'm {age} years old");
```

### Example (format()):

```python
print("My name is {}, I'm {} years old".format(name, age));
```

### Common Use Cases:

- Taking User Input:

```python
user_input = input("Enter something: ");
print(f"Your entered: {user_input}");
```
