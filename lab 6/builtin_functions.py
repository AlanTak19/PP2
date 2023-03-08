##Task 1
from functools import reduce
import operator

# Define the list of numbers
numbers = [2, 3, 4, 5]

# Use reduce() to multiply all the numbers in the list
result = reduce(operator.mul, numbers)

# Print the result
print(result)

##Task 2
# Define the string
string = 'Hello World'

# Initialize counters for upper and lower case letters
upper_count = 0
lower_count = 0

# Loop through each character in the string
for char in string:
    # Check if the character is upper case
    if char.isupper():
        upper_count += 1
    # Check if the character is lower case
    elif char.islower():
        lower_count += 1

# Print the results
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")

##Task 3
# Define the string to check
string = 'racecar'

# Reverse the string
reversed_string = string[::-1]

# Check if the reversed string is equal to the original string
if string == reversed_string:
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')

##Task 4
import time
import math

# Define the number to compute the square root of
number = 25100

# Define the number of milliseconds to wait before computing the square root
wait_time = 2123 / 1000

# Wait for the specified amount of time
time.sleep(wait_time)

# Compute the square root
sqrt = math.sqrt(number)

# Print the result
print(f"Square root of {number} after {wait_time*1000:.0f} milliseconds is {sqrt}")

##Task 5
# Define the tuple to check
my_tuple = (True, True, True, False)

# Check if all elements of the tuple are true
if all(my_tuple):
    print('All elements of the tuple are true')
else:
    print('Not all elements of the tuple are true')
