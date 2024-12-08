# Write a function to encrypt strings using a Caesar cipher with a given shift value

# 1. Input: ("abc", 2) → Output: "cde"
# 2. Input: ("xyz", 3) → Output: "abc"
# 3. Input: ("Hello, World!", 5) → Output: "Mjqqt, Btwqi!"
# 4. Input: ("Python", 0) → Output: "Python"
# 5. Input: ("abc", -1) → Output: "zab"

# Creating a function called caesar
def caesar(string, shift):
    # Creating a variable called alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Checking if the shift is equals to 0
    if shift == 0:
        return string
    
    # Creating a for loop to shift the amount
    for i in range(shift):
        # Shifting
        string.replace(string, alphabet)

# Calling the function to check the result
print(caesar("abc", 2))