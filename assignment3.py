#3-1
names = ["tom","rebecca","murat"]
print(names[0])
print(names[1])
print(names[2])

#3-2

print(f"hello, {names[0]}")
print(f"hello, {names[1]}")
print(f"hello, {names[2]}")


for name in names:
    print(f"hello,{names}")
    
#3-3
name = ["ford","gmc"]
print(name[0])
print(name[1])

print(f"i want a {name[0]}")
print(f"i have a {name[1]}")

#3-4
invite = ["albert einstien","Maya Angelou"]


for invite in invite:
    print(f"Dear {invite}, I would be honored to invite you to dinner. It would be a pleasure to share an evening of great conversation and ideas with you.")
#3-5
    guest_list = ["Alice", "Bob", "Charlie"]

# One guest can't make it
unable_to_attend = "Charlie"
print(f"\nUnfortunately, {unable_to_attend} can't make it to the dinner.")

# Replace the guest
guest_list[guest_list.index(unable_to_attend)] = "Maya Angelou"

# Print updated invitations
print("\nUpdated Invitations:")
for guest in guest_list:
    print(f"Hi {guest}, you're still invited to dinner!")
    
#3-6
    print("\nGood news! We found a bigger dinner table!")

# Add more guests
guest_list.insert(0, "Eve")               # Beginning
guest_list.insert(len(guest_list)//2, "Frank")  # Middle
guest_list.append("Grace")                # End

# Print new invitations
print("\nNew Invitations:")
for guest in guest_list:
    print(f"Hi {guest}, you're invited to dinner!")
#3-7
    print("\nBad news! The new table won't arrive in time. I can only invite two people.")

# Remove guests until only two remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Inform the two remaining guests
print("\nStill Invited:")
for guest in guest_list:
    print(f"{guest}, you're still invited to dinner!")

# Empty the list
del guest_list[0]
del guest_list[0]

# Print final list to confirm it's empty
print("\nFinal guest list:", guest_list)


#3-8
places_to_visit = ["Japan", "Iceland", "New Zealand", "Switzerland", "Morocco"]

# Original order
print("Original order:")
print(places_to_visit)

# Alphabetical order (temporary)
print("\nAlphabetical order (temporary):")
print(sorted(places_to_visit))

# Original order again
print("\nStill original order:")
print(places_to_visit)

# Reverse alphabetical order (temporary)
print("\nReverse alphabetical order (temporary):")
print(sorted(places_to_visit, reverse=True))

# Original order again
print("\nStill original order:")
print(places_to_visit)

# Reverse the list (permanent)
places_to_visit.reverse()
print("\nReversed order (permanent):")
print(places_to_visit)

# Reverse it back to original
places_to_visit.reverse()
print("\nBack to original order:")
print(places_to_visit)

# Sort the list alphabetically (permanent)
places_to_visit.sort()
print("\nSorted alphabetically (permanent):")
print(places_to_visit)

# Sort in reverse alphabetical order (permanent)
places_to_visit.sort(reverse=True)
print("\nSorted in reverse alphabetical order (permanent):")
print(places_to_visit)

#3-9
guest_list = ["Alice", "Bob", "David"]  # Example list before shrinking

print(f"\nI am inviting {len(guest_list)} people to dinner.")
#3-10
languages = ["Python", "JavaScript", "C++", "Go"]

# append()
languages.append("Rust")
print("\nAfter append():", languages)

# insert()
languages.insert(2, "Java")
print("After insert():", languages)

# del
del languages[3]
print("After del:", languages)

# pop()
popped_lang = languages.pop()
print(f"Popped item: {popped_lang}")
print("After pop():", languages)

# remove()
languages.remove("JavaScript")
print("After remove():", languages)

# sorted()
print("Temporarily sorted:", sorted(languages))

# sort()
languages.sort()
print("After sort():", languages)

# reverse()
languages.reverse()
print("After reverse():", languages)

# len()
print(f"Total languages in the list: {len(languages)}")
#3-11