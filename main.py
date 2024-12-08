# Write a function that determines if two strings are anagrams of each other.

# 1. Input: ("listen", "silent") → Output: True
# 2. Input: ("triangle", "integral") → Output: True
# 3. Input: ("apple", "pale") → Output: False
# 4. Input: ("a", "a") → Output: True
# 5. Input: ("rat", "car") → Output: False

# Creating a function called anagram and giving 2 parameters
def anagram(str1, str2):
    # Writing if/else statemants to check if the 2 strings are anagrams
    if str1 == str2:
        return True
    elif str1[0] != str2[0]:
        return True
    elif str1[1] != str2[1]:
        return True
    elif str1[0] != str2[0] and max(str1) != max(str2):
        return False
    else:
        return False

# calling the function to check result
print(anagram("listen", "silent"))