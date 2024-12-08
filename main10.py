# Write a function that sums two fractions and returns the result in its simplest form. The
# fractions will be given as two tuples, where each tuple consists of two integers: the
# numerator and the denominator. To simplify the result, you need to compute the Least
# Common Multiple (LCM) and Greatest Common Divisor (GCD) of the denominators.
# Then, simplify the result by dividing both the numerator and denominator by their GCD.

# Input: frac1 = (1, 2), frac2 = (1, 3)
# Output: (5, 6)
# Explanation: The LCM of 2 and 3 is 6. The sum is (1 * 3) / 6 + (1 * 2) / 6
# = 3/6 + 2/6 = 5/6.
# Input: frac1 = (1, 4), frac2 = (1, 4)
# Output: (1, 2)
# Explanation: The LCM of 4 and 4 is 4. The sum is (1/4 + 1/4) = 2/4 = 1/2.
# Input: frac1 = (2, 5), frac2 = (1, 5)
# Output: (3, 5)
# Explanation: The LCM of 5 and 5 is 5. The sum is (2/5 + 1/5) = 3/5.
# Input: frac1 = (3, 4), frac2 = (5, 6)
# Output: (19, 12)
# Explanation: The LCM of 4 and 6 is 12. The sum is (3 * 3) / 12 + (5 * 2) /
# 12 = 9/12 + 10/12 = 19/12.
# Input: frac1 = (5, 12), frac2 = (7, 15)
# Output: (139, 60)
# Explanation: The LCM of 12 and 15 is 60. The sum is (5 * 5) / 60 + (7 * 4)
# / 60 = 25/60 + 28/60 = 53/60.

# Creating 2 fractions called GCD and LCM
def frac1(num1, num2):
    # Divisioning
    if num1 % 2 == 0:
        return num1 // 2
    elif num1 % 2 != 0:
        return num1 // 3
    elif num1 % 3 != 0:
        return num1 // 5
    elif num1 % 5 != 0:
        return num1 // 7
    elif num1 % 7 != 0:
        return num1 // 8
    elif num1 % 8 != 0:
        return num1 // 9
    
    if num2 % 2 == 0:
        return num2 // 2
    elif num2 % 2 != 0:
        return num2 // 3
    elif num2 % 3 != 0:
        return num2 // 5
    elif num2 % 5 != 0:
        return num2 // 7
    elif num2 % 7 != 0:
        return num2 // 8
    elif num2 % 8 != 0:
        return num2 // 9
    
    return num1 * num2

def frac2(num1, num2):
    if num1 % 2 == 0:
        return num1 // 2
    elif num1 % 2 != 0:
        return num1 // 3
    elif num1 % 3 != 0:
        return num1 // 5
    elif num1 % 5 != 0:
        return num1 // 7
    elif num1 % 7 != 0:
        return num1 // 8
    elif num1 % 8 != 0:
        return num1 // 9
    
    if num2 % 2 == 0:
        return num2 // 2
    elif num2 % 2 != 0:
        return num2 // 3
    elif num2 % 3 != 0:
        return num2 // 5
    elif num2 % 5 != 0:
        return num2 // 7
    elif num2 % 7 != 0:
        return num2 // 8
    elif num2 % 8 != 0:
        return num2 // 9
    
    return num1 * num2

# Summing the fractions result
def sum_fracs():
    return frac1(1, 2) + frac2(2, 6)

# Calling the function to check the result
print(sum_fracs())