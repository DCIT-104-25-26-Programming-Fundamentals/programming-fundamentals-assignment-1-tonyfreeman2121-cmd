# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(numbers):
    """Return the sum of all numbers in the list (no built-in sum())."""
    total = 0
    for value in numbers:
        total += value
    return total
 
 
def calculate_average(numbers):
    """Return the average of the numbers in the list."""
    return calculate_sum(numbers) / len(numbers)
 
 
def calculate_max(numbers):
    """Return the largest value in the list (no built-in max())."""
    largest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
    return largest
 
 
def calculate_min(numbers):
    """Return the smallest value in the list (no built-in min())."""
    smallest = numbers[0]
    for value in numbers:
        if value < smallest:
            smallest = value
    return smallest
 
 
def get_numbers_from_user():
    """Prompt the user for N and then N numbers; return them as a list."""
    n = int(input("How many numbers? "))
 
    if n <= 0:
        print("Error: N must be a positive integer.")
        return None
 
    numbers = []
    for i in range(1, n + 1):
        value = float(input(f"Enter number {i}: ")).
        if value.is_integer():
            value = int(value)
        numbers.append(value)
 
    return numbers
 
 
def main():
    numbers = get_numbers_from_user()
 
    if numbers is None:
        return  
 
    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_max(numbers)
    minimum = calculate_min(numbers)
 
    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
 
 
if __name__ == "__main__":
    main()
 
