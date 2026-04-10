def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if input is a string
    if isinstance(s, str):
    # Using string slicing to reverse the string
        return s[::-1]

# Task 2
# Invoke the function "string_reverse" using the following scenarios:

# Scenario 1: "Hello World"
print("Original string: Hello World")
print(f"Reversed string: {string_reverse("Hello World")}")

# Scenario 2: "Python"
print("Original string: Python")
print(f"Reversed string: {string_reverse("Python")}")
