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
# age = int(input("Enter your Age: "));
# print(age);

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