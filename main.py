from pet import Pet  # Import the Pet class from pet.py

# Create a pet object with a name Pixel
my_pet = Pet("Pixel") 

# Display the pet's initial status
print("Initial Pet Status:")
my_pet.get_status()

# Simulate actions with the pet
print("\nFeeding the pet...")
my_pet.eat()

print("\nPlaying with the pet...")
my_pet.play()

print("\nPutting the pet to sleep...")
my_pet.sleep()

# Display the updated status of the pet
print("\nUpdated Pet Status:")
my_pet.get_status()

# Teach the pet some tricks
print("\nTeaching the pet new tricks...")
my_pet.train("Sit")
my_pet.train("Roll Over")

# Show all tricks the pet has learned
print("\nTricks learned by the pet:")
my_pet.show_tricks()

# Final status of the pet
print("\nFinal Pet Status:")
my_pet.get_status()
