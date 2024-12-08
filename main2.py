# Write a function that counts the number of unique words in a string, ignoring case sensitivity
# and punctuation.

# 1. Input: "The quick brown fox jumps over the lazy dog" → Output: 8
# 2. Input: "Hello hello world!" → Output: 2
# 3. Input: "" → Output: 0
# 4. Input: "Python is fun. Python is cool." → Output: 5
# 5. Input: "One word" → Output: 2

# Creating a function called count_unique_words wich will count unique words in a string
def count_unique_words(string):
    # Creating a for loop to return the counted unique words
    for i in string:
        # Checking for case sensivity words to not count it
        if string != string.capitalized() or string != string.title():
            string.count(string.lower())
    # returning the result
    return i

# Calling the function to see the result
print(count_unique_words("Python is fun. Python is cool!"))