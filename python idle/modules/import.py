import modules

print(modules.add)


# Import the 'random' module, which is a built-in module for random number generation
import random
 
# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print("Random Number:", random_number)


import math

# Initialize the number of items to choose from
n = 7

# Initialize the number of possibilities to choose
k = 4

# Print total number of possible combinations
print (math.comb(n, k))
