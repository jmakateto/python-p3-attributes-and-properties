from dog import Dog
from person import Person

# Creating a Dog and setting its properties
dog = Dog("Buddy", "Labrador")
dog.name = "Max"
dog.breed = "Poodle"  

# Creating a Person and setting its properties
person = Person("Alice", "Engineer")
person.name = "Bob"
person.job = "Artist"  

# Printing the updated information
print(f"Dog's Name: {dog.name}, Breed: {dog.breed}")
print(f"Person's Name: {person.name}, Job: {person.job}")
