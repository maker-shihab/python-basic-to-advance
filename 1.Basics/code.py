# Variable and Data Type
varInt = 10;
varString = "Hello, I'm Shihab!";
varFloat = 10.5;
varBoolean = False;
varList = ["Maker", 25, 5.5, "Developer"];
varTuple = ("Maker", 25, 5.5, "Developer");
varDict = { "name": "Maker", "age": 25 } #key value pair 


print(varInt);
print(varString);
print(varFloat);
print(varBoolean);
print(varList);
print(varTuple);
print(varDict);

# input
age = int(input("Enter your Age: "));
print(age);

# output
print("Hello World!");
print("Pyton", "is", "fun", sep=" - ", end="\n");

# Formatted Output

name = "Shihab"
age = 25
print(f"My name is {name} and I am {age} years old.");

# formate()
print("My name is {} and I am {} years old.".format(name, age))

user_input = input("Enter something: ");
print(f"Your entered: {user_input}");

# Conditionals
age = int(input("Enter your age: "));
if (age >= 45):
    print(f"Sorry you are not allowed {age}");
elif (age <= 18):
    print(f"Sorry you are not allowed {age}");
else: 
    print("Welcome, you are allowed to enter.");

# Checking even odd numbers
number = int(input("Enter a number: "));
if (number % 2 == 0):
    print(f"{number} is even.")
else:
    print(f"{number} is odd");

# Loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

sum = 0
for i in range(1, 11):
    sum += i
print("The sum is: ", sum)

# Factorial 
fNum = int(input("Enter your number: "))
factorial = 1
for i in range(1, fNum + 1):
    factorial *= i
print (f"The factorial is: {fNum} is {factorial}")


# While Loop
# Guessing Game with While Loop
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
print("Congratulations! You've guessed the number!")


# Function
def greet(name):
    print(f"Hello, {name}!")

greet("Shihab")

# Factorial in function
factorialNum = int(input("Enter your number: "));
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(factorialNum)) 

# Check if a Number is Prime with function
def is_prime(n):
    if n <=1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(11))

