car = ['ford', 'subaru', 'hondeezy']
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car.title()}.")

group_size = int(input("How many people are in your dinner group? "))

if group_size > 8:
    print("You’ll have to wait for a table.")
else:
    print("Your table is ready.")

number = int(input("Enter a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

while True:
    print("This loop will run forever! Press CTRL-C to stop.")

    age_input = input("Enter your age (or type 'quit' to exit): ")
    if age_input.lower() == 'quit':
        break

    age = int(age_input)
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'egg', 'pastrami']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

# Remove all 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process remaining orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let someone else respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False

# Display results
print("\n--- Dream Vacation Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
