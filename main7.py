# Write a function that takes two integers, start and end, and returns
# a list of all prime numbers in the range [start, end]. A prime
# number is a number greater than 1 that has no divisors other than 1
# and itself

# Input: start = 10, end = 20
# Output: [11, 13, 17, 19]
# Input: start = 1, end = 10
# Output: [2, 3, 5, 7]
# Input: start = 20, end = 30
# Output: [23, 29]
# Input: start = 24, end = 25
# Output: []
# Input: start = 1, end = 1
# Output: []

# Creating a function called find_prime_numbers wich will find prime numbers in a range
def find_prime_numbers(start, end):
    # Creating a list to append the prime numbers
    result = []
    
    # Creating a for loop to find the prime numbers
    for i in range(start, end):
        # Checking if the number is prime
        if i % 1 == 0 and i % i == 0:
            # Appending the prime number to the list
            result.append(i)

    # Returning the list
    return result

# Calling the function to check the result
print(find_prime_numbers(10, 20))