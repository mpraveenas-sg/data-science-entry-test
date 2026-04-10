def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key exists in the dictionary before updating
    if key in dct:
        print("Original value before update:", dct[key])
    # Update the dictionary with new value
    dct[key] = value
    # Return the updated dictionary
    return dct


# Task 2
# Invoke the function "update_dictionary" using the provided scenarios:

# Scenario 1: {}, "name", "Alice"
result1 = update_dictionary({}, "name", "Alice")
print(f"Scenario 1 result after update: {result1}")

# Scenario 2: {"age": 25}, "age", 26
# This should print the original value (25) and then return the updated dict
result2 = update_dictionary({"age": 25}, "age", 26)
print(f"Scenario 2 result after update: {result2}")