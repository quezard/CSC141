# 5-1. Conditional Tests

car = 'subaru'

# Test 1: Equality comparison for car
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True because the value of car is 'subaru'

# Test 2: Inequality comparison for car
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False because car is not 'audi'

# Test 3: String equality using the lower() method
name = 'Alice'
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')  # True because .lower() converts to lowercase

# Test 4: Inequality with string using lower() method
print("\nIs name.lower() != 'bob'? I predict True.")
print(name.lower() != 'bob')  # True because 'alice' is not equal to 'bob'

# Test 5: Numerical comparison (greater than)
number = 10
print("\nIs number > 5? I predict True.")
print(number > 5)  # True because 10 is greater than 5

# Test 6: Numerical comparison (less than)
print("\nIs number < 5? I predict False.")
print(number < 5)  # False because 10 is not less than 5

# Test 7: Numerical equality comparison
age = 30
print("\nIs age == 30? I predict True.")
print(age == 30)  # True because age is exactly 30

# Test 8: Logical 'and' condition
print("\nIs number > 5 and age == 30? I predict True.")
print(number > 5 and age == 30)  # True because both conditions are true

# Test 9: Logical 'or' condition
print("\nIs number > 5 or name == 'bob'? I predict True.")
print(number > 5 or name == 'bob')  # True because number > 5 is True

# Test 10: List membership (in)
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'banana' in fruits? I predict True.")
print('banana' in fruits)  # True because 'banana' is in the list

# Additional Tests: 5-2. More Conditional Tests

# Test 11: Item not in list (not in)
print("\nIs 'grape' not in fruits? I predict True.")
print('grape' not in fruits)  # True because 'grape' is not in the list

# Test 12: Greater than or equal to (>=)
print("\nIs age >= 30? I predict True.")
print(age >= 30)  # True because age is exactly 30

# Test 13: Less than or equal to (<=)
print("\nIs age <= 25? I predict False.")
print(age <= 25)  # False because age is not less than or equal to 25

# Test 14: Numerical inequality (not equal to)
print("\nIs age != 35? I predict True.")
print(age != 35)  # True because age is not equal to 35

# Test 15: Logical 'and' with multiple conditions
print("\nIs number > 5 and age > 20 and name == 'Alice'? I predict True.")
print(number > 5 and age > 20 and name == 'Alice')  # True because all conditions are true
# Alien color is green
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points for shooting the green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting the yellow alien!")
else:
    print("You earned 15 points for shooting the red alien!")
# Alien color is yellow
alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points for shooting the green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting the yellow alien!")
else:
    print("You earned 15 points for shooting the red alien!")
    # Alien color is red
alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points for shooting the green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting the yellow alien!")
else:
    print("You earned 15 points for shooting the red alien!")

# Age of the person
age = 25

if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")
    # List of favorite fruits
favorite_fruits = ['apple', 'banana', 'cherry']

# Checking each fruit
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'cherry' in favorite_fruits:
    print("You really like cherries!")
if 'grape' in favorite_fruits:
    print("You really like grapes!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")

# List of usernames
usernames = ['alice', 'bob', 'admin', 'charlie', 'david']

# Loop through the list of usernames
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
# List of usernames
usernames = []  # Empty list to test

# Check if the list is empty
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")
# List of current users
current_users = ['alice', 'bob', 'charlie', 'admin', 'david']

# List of new users
new_users = ['Alice', 'jane', 'Bob', 'emma', 'charlie']

# Make a lowercase copy of the current_users list for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Check if new usernames are available
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username {new_user} has already been used. Please choose a new username.")
    else:
        print(f"The username {new_user} is available.")

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the list
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")