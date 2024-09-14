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

## 4. Functions

### Overview

Functions are blocks of reusable code that perform a specific task. They allow you to organize your code, avoid repetition, and make it more modular. In Python, functions are defined using the def keyword.

### Defining

```python
def function_name(parameters):
    # Code block (function body)
    return result  # Optional
```

- function_name: The name of the function.
- parameters: Inputs (optional) the function takes (also called arguments).
- return: The value that the function returns (optional).

### Example:

```python
def greet():
    print("Hello, World!")

greet()  # Calling the function
```

### Function with Parameters

You can pass data into functions using parameters.

### Example:

```python
def greet(name):
    print(f"Hello, World!")
greet("Shihab")
```

### Function with Return Value

A function can return a value using the `return` statement. This value can be used outside the function.

### Example:

```python
def add(a, b):
    result = a + b

result = add(2, 4)
print(f"This sum is {result}")
```

### Default Parameters

You can define default values for function parameters, which will be used if no argument is passed for that parameter.

### Example:

```python
def greet(name="Stranger"):
    print(f"Hello {name}")

greet()
greet("Shihab")
```

### Keyword Arguments

Functions can be called with keyword arguments, which makes the code more readable and allows arguments to be passed in any order.

### Example:

```python
def introduce(name, age):
    print(f"My name is {name} and age is {age}")

introduce(age=25, name="Shihab") # Arguments in reverse order using kewords
```

### Arbitrary Arguments

If we're unsure how many arguments will be passed, we can `*args` to handle an arbitrary number of arguments. `*args` collects the arguments into a tuple.

### Example:

```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_numbers(1, 2, 3, 4, 5)) #Output: 15
```

### Arbitrary Keyword Arguments (`**kwargs`)

Similarly, we can use `**kwargs` to accept an arbitrary number of keyword arguments. It collects the arguments into a dictionary.

### Example:

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_info(name="Shihab", age=25, country="Bangladesh")
```

### Practical Examples

### Calculate Factorial Using Recursion

Recursion is when a function calls itself. Here's an example of a recursive function to calculate the factorial of a number.

```python
def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5)) # Output: 120
```

### Find Maximum of Three Numbers

```python
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >= c:
        return b
    else:
        return c
print(find_max(10, 15, 7)) # Output: 15
```

### Check if a Number is Prime

```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(11)) # Output: True
print(is_prime(10)) # Output: False
```

### Key Points to Remember:

- Functions help in organizing your code by making it modular.
- Functions can take arguments, return values, and even have default or arbitrary parameters.
- Python supports recursion, but be cautious as too deep recursion can lead to errors.
