# 6-1. Person
person = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'New York'
}

print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

# 6-2. Favorite Numbers
favorite_numbers = {
    'Tom': 7,
    'Lily': 3,
    'Sam': 42,
    'Nina': 9,
    'Ben': 27
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

# 6-3. Glossary
glossary = {
    'variable': 'A container for storing data values.',
    'loop': 'A way to repeat a block of code multiple times.',
    'function': 'A named section of a program that performs a specific task.',
    'dictionary': 'A collection of key-value pairs.',
    'list': 'An ordered collection of items.'
}

for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")

# 6-4. Glossary 2
glossary = {
    'variable': 'A container for storing data values.',
    'loop': 'A way to repeat a block of code multiple times.',
    'function': 'A named section of a program that performs a specific task.',
    'dictionary': 'A collection of key-value pairs.',
    'list': 'An ordered collection of items.',
    'tuple': 'An immutable sequence of values.',
    'boolean': 'A data type with only two values: True and False.',
    'if statement': 'Allows you to conditionally execute code.',
    'comment': 'A note in the code for the programmer, ignored by Python.',
    'indentation': 'The space used at the beginning of a line to define code blocks.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")

# 6-5. Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Print sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountries included:")
for country in rivers.values():
    print(f"- {country.title()}")

# 6-6. Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# List of people who should take the poll
people_to_poll = ['jen', 'sarah', 'mike', 'anna', 'edward']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for already taking the poll!")
    else:
        print(f"{person.title()}, please take our favorite programming language poll!")

# 6-7. People
person1 = {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 28, 'city': 'New York'}
person2 = {'first_name': 'Bob', 'last_name': 'Smith', 'age': 34, 'city': 'Chicago'}
person3 = {'first_name': 'Clara', 'last_name': 'Lee', 'age': 25, 'city': 'San Francisco'}

people = [person1, person2, person3]

for person in people:
    print(f"\nFull Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")

# 6-8. Pets
pet1 = {'animal': 'dog', 'owner': 'Liam'}
pet2 = {'animal': 'cat', 'owner': 'Mia'}
pet3 = {'animal': 'parrot', 'owner': 'Noah'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\nAnimal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")

# 6-9. Favorite Places
favorite_places = {
    'Alice': ['Paris', 'Tokyo', 'New York'],
    'Bob': ['London', 'Amsterdam'],
    'Clara': ['Rome']
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")

# 6-10. Favorite Numbers
favorite_numbers = {
    'Tom': [7, 12],
    'Lily': [3],
    'Sam': [42, 9],
    'Nina': [9, 10, 11],
    'Ben': [27]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")

# 6-11. Cities
cities = {
    'new york': {
        'country': 'USA',
        'population': '8.5 million',
        'fact': 'Known as the city that never sleeps.'
    },
    'tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Home to the busiest train station in the world.'
    },
    'paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Famous for the Eiffel Tower.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")

# 6-12. Extended Cities Example
cities = {
    'new york': {
        'country': 'USA',
        'population': '8.5 million',
        'area_km2': 783.8,
        'fact': 'Known as the city that never sleeps.'
    },
    'tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'area_km2': 2194,
        'fact': 'Home to the busiest train station in the world.'
    },
    'paris': {
        'country': 'France',
        'population': '2.1 million',
        'area_km2': 105.4,
        'fact': 'Famous for the Eiffel Tower.'
    }
}

for city, info in cities.items():
    print("\n" + "="*40)
    print(f"City: {city.title()}")
    print(f"Country:     {info['country']}")
    print(f"Population:  {info['population']}")
    print(f"Area:        {info['area_km2']} km²")
    print(f"Fact:        {info['fact']}")
    print("="*40)
