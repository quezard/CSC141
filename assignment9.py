class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business!")
        

# Create an instance
restaurant = Restaurant("La Bella Vita", "Italian")

# Print attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Create three instances
restaurant1 = Restaurant("Sushi World", "Japanese")
restaurant2 = Restaurant("Taco Fiesta", "Mexican")
restaurant3 = Restaurant("Curry House", "Indian")

# Call describe_restaurant() for each
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Profile:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Email: {self.email}\n"
              f"Location: {self.location}\n")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome back!\n")


# Create multiple users
user1 = User("Alice", "Johnson", 28, "alice.johnson@example.com", "New York")
user2 = User("Bob", "Smith", 34, "bob.smith@example.com", "Chicago")
user3 = User("Charlie", "Brown", 22, "charlie.brown@example.com", "Los Angeles")

# Call methods
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, additional_customers):
        """Increase the number served by the given amount."""
        if additional_customers > 0:
            self.number_served += additional_customers
        else:
            print("Increment must be a positive number.")


# Create an instance
restaurant = Restaurant("La Bella Vita", "Italian")

# Print initial number served
print(f"Customers served: {restaurant.number_served}")

# Change value and print again
restaurant.number_served = 50
print(f"Customers served: {restaurant.number_served}")

# Use set_number_served method
restaurant.set_number_served(100)
print(f"Customers served after setting value: {restaurant.number_served}")

# Use increment_number_served method
restaurant.increment_number_served(25)
print(f"Customers served after incrementing: {restaurant.number_served}")

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # Default value

    def describe_user(self):
        print(f"User Profile:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Email: {self.email}\n"
              f"Location: {self.location}\n")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome back!\n")

    def increment_login_attempts(self):
        """Increase login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


# Create a user instance
user = User("Alice", "Johnson", 28, "alice.johnson@example.com", "New York")

# Simulate multiple login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print current login attempts
print(f"Login attempts: {user.login_attempts}")

# Reset and print again
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
# restaurant.py

class Restaurant:
    """A simple restaurant class."""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")


class IceCreamStand(Restaurant):
    """A special kind of restaurant that serves ice cream."""

    def __init__(self, name, cuisine_type="ice cream"):
        super().__init__(name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def display_flavors(self):
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Example usage:
ice_cream_stand = IceCreamStand("Sweet Treats")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()

# user.py

class User:
    """A simple user profile class."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Example usage:
admin = Admin("Alice", "Wong")
admin.describe_user()
admin.show_privileges()

# admin_privileges.py

class User:
    """A simple user profile class."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")


class Privileges:
    """Stores privileges for an admin user."""

    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = [
                "can add post",
                "can delete post",
                "can ban user"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


# Example usage:
admin = Admin("Charlie", "Smith")
admin.describe_user()
admin.privileges.show_privileges()

# electric_car.py

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"


class Battery:
    """A simple model of a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if it isn't already 65."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at full capacity.")


class ElectricCar(Car):
    """Models aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Example usage:
my_car = ElectricCar("Tesla", "Model 3", 2025)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()

# Upgrade and check again
my_car.battery.upgrade_battery()
my_car.battery.get_range()

class restaurant:
    """A simple restaurant class."""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

class User:
    """A simple user profile class."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")


class Privileges:
    """Stores privileges for an admin user."""

    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = [
                "can add post",
                "can delete post",
                "can ban user"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

class User:
    """A simple user profile class."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

from random import randint


class Die:
    """A class representing a die."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return randint(1, self.sides)


# Make a 6-sided die and roll it 10 times
six_sided = Die()
print("🎲 Rolling a 6-sided die:")
for _ in range(10):
    print(six_sided.roll_die(), end=" ")
print("\n")

# Make a 10-sided die and roll it 10 times
ten_sided = Die(10)
print("🎲 Rolling a 10-sided die:")
for _ in range(10):
    print(ten_sided.roll_die(), end=" ")
print("\n")

# Make a 20-sided die and roll it 10 times
twenty_sided = Die(20)
print("🎲 Rolling a 20-sided die:")
for _ in range(10):
    print(twenty_sided.roll_die(), end=" ")
print()

import random

# Create a pool of 10 numbers and 5 letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 unique items
winning_combo = random.sample(lottery_items, 4)

print("🎟️ Any ticket matching these 4 numbers/letters wins a prize:")
print(winning_combo)

import random

# Lottery pool
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define your ticket
my_ticket = [2, 'A', 9, 'C']

count = 0
won = False

# Keep drawing until you win
while not won:
    count += 1
    draw = random.sample(lottery_items, 4)
    if draw == my_ticket:
        won = True

print(f"🏆 Your ticket {my_ticket} won after {count:,} tries!")
