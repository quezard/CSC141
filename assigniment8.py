def display_message():
    print("I'm learning about functions in this chapter.")

# Call the function
display_message()

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Call the function with a book title
favorite_book("Alice in Wonderland")

def make_shirt(size, message):
    print(f"The shirt is size {size} and will have the message: '{message}'")

# Call using positional arguments
make_shirt("M", "Keep Calm and Code On")

# Call using keyword arguments
make_shirt(message="Hello World!", size="L")

def make_shirt(size="L", message="I love Python"):
    print(f"The shirt is size {size} and will have the message: '{message}'")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size="M")

# Custom size and message
make_shirt(size="S", message="Debugging is my cardio")

def describe_city(city, country="USA"):
    print(f"{city} is in {country}.")

# Three cities
describe_city("New York")
describe_city("Los Angeles")
describe_city("Tokyo", "Japan")

def city_country(city, country):
    return f"{city}, {country}"

# Call the function with three city-country pairs
print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))

def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title
    }
    if songs is not None:
        album['songs'] = songs
    return album

# Create three albums
album1 = make_album("The Beatles", "Abbey Road")
album2 = make_album("Pink Floyd", "The Dark Side of the Moon")
album3 = make_album("Nirvana", "Nevermind", songs=12)

# Print albums
print(album1)
print(album2)
print(album3)

def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title
    }
    if songs:
        album['songs'] = songs
    return album

print("Enter album details. Type 'quit' to exit.")

while True:
    artist = input("Enter artist name: ")
    if artist.lower() == 'quit':
        break

    title = input("Enter album title: ")
    if title.lower() == 'quit':
        break

    songs_input = input("Enter number of songs (optional, press Enter to skip): ")
    if songs_input.lower() == 'quit':
        break

    if songs_input.strip() == "":
        album = make_album(artist, title)
    else:
        album = make_album(artist, title, songs=int(songs_input))

    print("Album created:", album)
    print("-" * 30)

def show_messages(messages):
    for message in messages:
        print(message)

# List of short text messages
messages = ["Hello!", "How are you?", "Don't forget the meeting.", "See you soon!"]

# Call the function
show_messages(messages)

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop(0)
        print(f"Sending message: {current}")
        sent_messages.append(current)

# Original list of messages
messages = ["Hello!", "How are you?", "Don't forget the meeting.", "See you soon!"]
sent_messages = []

# Call the function to send messages
send_messages(messages, sent_messages)

# Print both lists
print("\nOriginal messages list:", messages)
print("Sent messages list:", sent_messages)

def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop(0)
        print(f"Sending message: {current}")
        sent_messages.append(current)

# Reset lists
original_messages = ["Hello!", "How are you?", "Don't forget the meeting.", "See you soon!"]
sent_messages = []

# Send a copy of the original list
send_messages(original_messages[:], sent_messages)

# Print both lists to show original is unchanged
print("\nOriginal messages list (unchanged):", original_messages)
print("Sent messages list:", sent_messages)

def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!")

# Call the function three times with different numbers of arguments
make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("peanut butter", "jelly")
make_sandwich("ham", "cheese", "mustard", "pickles", "onions")

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Create a profile about yourself
my_profile = build_profile(
    "John", 
    "Doe", 
    location="New York", 
    profession="developer", 
    hobby="photography"
)

print(my_profile)

def make_car(manufacturer, model, **features):
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in features.items():
        car_info[key] = value
    return car_info

# Call the function with extra keyword arguments
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
