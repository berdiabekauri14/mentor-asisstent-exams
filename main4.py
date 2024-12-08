# Write a function to generate Pascal's Triangle up to the specified number of rows.

# 1. Input: 1 → Output: [[1]]
# 2. Input: 2 → Output: [[1], [1, 1]]
# 3. Input: 3 → Output: [[1], [1, 1], [1, 2, 1]]
# 4. Input: 5 → Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6,
# 4, 1]]
# 5. Input: 0 → Output: []

# Creating a function called pascal wich will create a triangle
def pascal(num):
    # Creating a list to append the result
    result = []

    # Creating a for loop to triangle up to the specified number of rows
    for i in range(num):
        # Appending the result to the list
        result.append(i)

    # Printing the result
    print(result)

# Calling the function to check the result
pascal(6)