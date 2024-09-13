# Basics

## Overview

This section covers the basic building blocks of Python. Here, you’ll find explanations and code examples of:

- Variables and Data Types
- Conditionals
- Loops
- Functions

## Concepts

## 1. Variables | Data Types

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

## 1.2 Input/Output

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

## 2. Conditionals

### Overview

Conditionals allow you to make decisions in your code based on certain conditions. In Python, conditionals are controlled using if, elif, and else statements. They help execute specific code blocks only when certain conditions are true or false.

### Syntax

```python
if condition:
    # code block
```

### example

```python
age = 22;
if (age >= 45):
    print(f"Sorry you are not allowed, Maximum age required 45");
elif (age <= 18):
    print(f"Sorry you are not allowed, Minimum age required 18");
else:
    print("Welcome, you are allowed to enter.");
```

### Conditional Expressions (Ternary Operator)

### Example

```python
age = 22;
status = "Adult" if age >= 18 else "Minor"
print(status);
```

### Common Use Cases:

- Checking for even or odd numbers:

```python
number = int(input("Enter a number: "));
if (number % 2 == 0):
    print(f"{number} is even.")
else:
    print(f"{number} is odd");
```

## 3. Loop

### Overview

Loops allow you to repeat a block of code multiple times, which helps avoid repetition and makes your code more efficient. Python provides two primary types of loops: for loops and while loops.

### 1. For Loop

#Examples:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### range() Function

`range(start, stop, step)`

- start: The starting value (optional, defaults to 0).
- stop: The value at which the sequence ends (exclusive).
- step: The amount by which the value increments (optional, defaults to 1).

```python
for i in range(5):
    print(i) # Prints 0, 1, 2, 3, 4,

# Example
for i in range(1, 10, 2):
    print(i)  # Prints 1, 3, 5, 7, 9
```

### 2. While Loop

```python
#Examples:
i = 1
while i <= 5:
    print(i)
    i += 1  # Increment i by 1
# With break
for i in range(10):
    if i == 5:
        break  # Loop stops when i is 5
    print(i)

# With Skip
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Prints only odd numbers
```

### 3. Nested Loops

You can place one loop inside another loop to create a nested loop structure. The inner loop will execute completely for every iteration of the outer loop.

### Example:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
```

### Practical Examples of loops

```python
#Sum of Numbers from 1 to 10
sum = 0
for i in range(1, 11):
    sum += i
print("The sum is:", sum)
```
