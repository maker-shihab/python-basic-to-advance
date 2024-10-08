#Lists
numbers = []
for i in range(3):
    num = int(input("Enter a number: "))
    numbers.append(num)
print("You entered:", numbers)


#Tuples 
coordinates = (10, 20)
print(f"The x coordinate is {coordinates[0]} and the y coordinate is {coordinates[1]}")

#Set 
sentence = "Python is fun and Python is powerful"
unique_words = set(sentence.split())
print(unique_words)

#Dictionary
user_info = {
    "username": "shihab123",
    "email": "shihab@example.com",
    "password": "securepassword123"
}
print(f"Username: {user_info['username']}, Email: {user_info['email']}")

# Copying the Contents of One File to Another
with open("source.txt", "r") as source_file:
    with open("destination.txt", "w") as destination_file:
        content = source_file.read()
        destination_file.write(content)

# Counting the Number of Lines in a File
with open("user_data.txt", "w") as file:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

#  Writing User Input to a File
with open("user_data.txt", "w") as file:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")