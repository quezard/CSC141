# 4-1: Pizzas

# Step 1: Store pizza names in a list
pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']

# Step 2: Use a for loop to print a sentence about each pizza
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# Step 3: Add a line about how much you like pizza
print("\nI really love pizza!")


# 4-2: Animals

# Step 1: Store animal names in a list
animals = ['Dog', 'Cat', 'Rabbit']

# Step 2: Use a for loop to print a statement about each animal
for animal in animals:
    print(f"A {animal} would make a great pet.")

# Step 3: Add a line about what these animals have in common
print("\nAny of these animals would make a great pet!")

# 4-3: Counting to Twenty
for number in range(1, 21):  # range(1, 21) will generate numbers from 1 to 20
    print(number)

    # 4-4: One Million
numbers = list(range(1, 1000001))  # Generate numbers from 1 to 1 million
for number in numbers:
    print(number)

# 4-5: Summing a Million

# Generate numbers from 1 to 1 million
numbers = list(range(1, 1_000_001))

# Use min() and max() to check the start and end values
print("Minimum:", min(numbers))     # Should print 1
print("Maximum:", max(numbers))     # Should print 1,000,000

# Use sum() to calculate the sum of all numbers
total = sum(numbers)
print("Sum of numbers from 1 to 1 million:", total)

# 4-6: Odd Numbers
for number in range(1, 21, 2):  # range(1, 21, 2) generates odd numbers from 1 to 20
    print(number)

# 4-7: Threes
for number in range(3, 31, 3):  # range(3, 31, 3) generates multiples of 3 from 3 to 30
    print(number)

# 4-8: Cubes
for number in range(1, 11):  # Loop through numbers from 1 to 10
    cube = number ** 3  # Cube the number
    print(f"The cube of {number} is {cube}.")

# 4-9: Cube Comprehension
cubes = [number ** 3 for number in range(1, 11)]  # List comprehension for cubes from 1 to 10
print(cubes)

# 4-1: Pizzas
pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken', 'Hawaiian', 'Veggie']

# Print the message The first three items in the list are:
print("The first three items in the list are:", pizzas[:3])

# Print the message Three items from the middle of the list are:
middle_index = len(pizzas) // 2  # Get the middle index
print("Three items from the middle of the list are:", pizzas[middle_index-1:middle_index+2])

# Print the message The last three items in the list are:
print("The last three items in the list are:", pizzas[-3:])

# 4-1: Pizzas
my_pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']
friend_pizzas = my_pizzas.copy()  # Make a copy of the list

# Add a new pizza to the original list
my_pizzas.append('Hawaiian')

# Add a different pizza to the friend_pizzas list
friend_pizzas.append('Mushroom')

# Prove that you have two separate lists
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-1: Pizzas
pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken', 'Hawaiian', 'Veggie']

# First loop to print all pizzas
print("All pizzas:")
for pizza in pizzas:
    print(pizza)

# Second loop to print a customized message for each pizza
print("\nCustomized message for each pizza:")
for pizza in pizzas:
    print(f"I really love {pizza} pizza!")

# 4-13: Buffet

# Step 1: Store five basic foods in a tuple
menu = ('Pizza', 'Burger', 'Pasta', 'Salad', 'Soup')

# Step 2: Use a for loop to print each food the restaurant offers
print("The buffet offers the following foods:")
for food in menu:
    print(food)

# Step 3: Try to modify one of the items (this will cause an error)
# menu[0] = 'Sushi'  # This will raise a TypeError because tuples are immutable

# Step 4: The restaurant changes its menu
menu = ('Sushi', 'Ramen', 'Tempura', 'Curry', 'Dumplings')

# Step 5: Use a for loop to print each of the items on the revised menu
print("\nThe updated buffet menu is:")
for food in menu:
    print(food)
