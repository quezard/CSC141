# 10-1_learning_python.py
file_path = "learning_python.txt"

print("Reading the entire file:\n")
with open(file_path) as f:
    contents = f.read()
    print(contents)

print("\nReading line by line:\n")
with open(file_path) as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())

# 10-2_learning_c.py
file_path = "learning_python.txt"

with open(file_path) as f:
    for line in f:
        print(line.replace("Python", "C").strip())

# 10-3_simpler_reader.py
file_path = "learning_python.txt"

with open(file_path) as f:
    for line in f.read().splitlines():
        print(line)

# 10-4_guest.py
name = input("What is your name? ")
with open("guest.txt", "w") as f:
    f.write(name)
print("Thanks, your name has been stored.")

# 10-5_guest_book.py
print("Enter 'quit' to stop.")
with open("guest_book.txt", "w") as f:
    while True:
        name = input("Enter your name: ")
        if name.lower() == "quit":
            break
        print(f"Welcome, {name}!")
        f.write(name + "\n")

# 10-6_addition.py
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
except ValueError:
    print("Oops! Please enter numbers only.")
else:
    print(f"The sum is {a + b}")

# 10-7_addition_calculator.py
while True:
    print("\nEnter 'q' to quit.")
    a = input("First number: ")
    if a.lower() == "q":
        break
    b = input("Second number: ")
    if b.lower() == "q":
        break
    try:
        result = int(a) + int(b)
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print(f"Result: {result}")

# 10-8_cats_and_dogs.py
files = ["cats.txt", "dogs.txt"]

for file in files:
    try:
        with open(file) as f:
            print(f"\nContents of {file}:")
            print(f.read())
    except FileNotFoundError:
        print(f"Sorry, the file {file} was not found.")

# 10-9_silent_cats_and_dogs.py
files = ["cats.txt", "dogs.txt"]

for file in files:
    try:
        with open(file) as f:
            print(f.read())
    except FileNotFoundError:
        pass  # Fail silently

# 10-10_common_words.py
def count_word(filename, word="the "):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read().lower()
    except FileNotFoundError:
        print(f"{filename} not found.")
    else:
        count = contents.count(word)
        print(f"'{word.strip()}' appears {count} times in {filename}.")

# Example usage
files = ["book1.txt", "book2.txt"]
for file in files:
    count_word(file)

# 10-11_favorite_number_store.py
import json

number = input("What is your favorite number? ")
with open("favorite_number.json", "w") as f:
    json.dump(number, f)
print("Got it! Your number has been saved.")

# 10-11_favorite_number_store.py
import json

number = input("What is your favorite number? ")
with open("favorite_number.json", "w") as f:
    json.dump(number, f)
print("Got it! Your number has been saved.")

# 10-11_favorite_number_read.py
import json

with open("favorite_number.json") as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")

# 10-12_favorite_number_remembered.py
import json
from pathlib import Path

path = Path("favorite_number.json")

if path.exists():
    number = json.loads(path.read_text())
    print(f"I know your favorite number! It's {number}.")
else:
    number = input("What's your favorite number? ")
    path.write_text(json.dumps(number))
    print("I'll remember that next time!")

# 10-13_user_dictionary.py
import json
from pathlib import Path

user = {
    "username": input("Enter your name: "),
    "age": input("Enter your age: "),
    "city": input("Enter your city: "),
}

path = Path("user_info.json")
path.write_text(json.dumps(user))

data = json.loads(path.read_text())
print(f"\nHere's what I remember about you:")
for k, v in data.items():
    print(f"{k.title()}: {v}")

# 10-14_verify_user.py
import json
from pathlib import Path

path = Path("username.json")

def get_new_username():
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
    return username

def greet_user():
    if path.exists():
        username = json.loads(path.read_text())
        correct = input(f"Are you {username}? (y/n): ")
        if correct.lower() == "y":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you next time, {username}.")
    else:
        username = get_new_username()
        print(f"We'll remember you next time, {username}.")

greet_user()

