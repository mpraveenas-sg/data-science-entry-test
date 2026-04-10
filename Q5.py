def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if the remainder is 0 using the modulo operator (%)
    if type(num) == int and type(divisor) == int:
        if num % divisor == 0:
            return True
        else:
            return False
    else:
        return -1

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:

# Scenario 1: 10, 2
result1 = check_divisibility(10, 2)
print(f"Is 10 divisible by 2? {result1}")

# Scenario 2: 7, 3
result2 = check_divisibility(7, 3)
print(f"Is 7 divisible by 3? {result2}")
