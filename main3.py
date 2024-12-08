# Write a function that takes a sentence and reverses the order of its words.

# 1. Input: "Hello World" → Output: "World Hello"
# 2. Input: "Python is great" → Output: "great is Python"
# 3. Input: "a b c" → Output: "c b a"
# 4. Input: "" → Output: ""
# 5. Input: " Spaces " → Output: "Spaces"

# Creating a function called reverse_words_order wich will reverse the words order
def reverse_words_order(string):
    # Checking if the string is empty
    if string == "":
        return ""
    # Returning reversed order
    return string.replace(max(string), min(string))

# Calling the function to check the result
print(reverse_words_order("Hello world"))