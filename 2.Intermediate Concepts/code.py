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
