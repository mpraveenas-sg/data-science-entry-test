def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    # Check if x and y are numeric
    if (type(x) in (int, float)) and (type(y) in (int, float)):
        # swap the value of x and y using only x and y
        x = x + y
        y = x - y
        x = x - y
        print("Swapped values:", x, y)
    else:
        return -1


# Task 2
# Invoke the function "swap" using the following scenarios:
print(swap("Apple", 10))  # Should return -1
swap(9, 17)  # Should print swapped values
