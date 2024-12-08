# Write a function that calculates the primorial of a number. The primorial of a number n is
# the product of all prime numbers less than or equal to n. For example, the primorial of 5 is
# the product of the primes less than or equal to 5: 2 * 3 * 5 = 30.
# Your function should take an integer n and return the primorial of that number.

# Input: n = 5
# Output: 30
# Explanation: The prime numbers less than or equal to 5 are 2, 3, and 5. Their product
# is 2 * 3 * 5 = 30.
# Input: n = 10
# Output: 210
# Explanation: The prime numbers less than or equal to 10 are 2, 3, 5, and 7. Their
# product is 2 * 3 * 5 * 7 = 210.
# Input: n = 1
# Output: 1
# Explanation: There are no primes less than or equal to 1, so the primorial is 1 by
# definition.

# Creating a function called primorial
def primorial(n):
    # Creating a for loop to multiply the range to the paramater n
    for i in n:
        # Multiplying
        return n * i

# Calling the function to check the result
print(primorial(5))