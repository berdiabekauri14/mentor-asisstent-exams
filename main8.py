# Write a function that finds the k-th smallest element in an unsorted array.

# Input: arr = [3, 2, 1, 5, 6, 4], k = 2
# Output: 2
# Explanation: The 2nd smallest element in the array is 2.
# Input: arr = [3, 2, 1, 5, 6, 4], k = 4
# Output: 4
# Explanation: The 4th smallest element in the array is 4.
# Input: arr = [7, 10, 4, 3, 20, 15], k = 3
# Output: 7
# Explanation: The 3rd smallest element in the array is 7.
# Input: arr = [1, 2, 3, 4, 5], k = 1
# Output: 1
# Explanation: The 1st smallest element is 1.
# Input: arr = [1, 2, 3, 4, 5], k = 5
# Output: 5
# Explanation: The 5th smallest element is 5.

# Creating a function called kth_smallest_element wich will find the smallest element in the array
def kth_smallest_element(array):
    # Using the min function to find the smallest element in the array
    return min(array)

# Calling the function to check the result
print(kth_smallest_element([3, 2, 1, 5, 6, 4]))