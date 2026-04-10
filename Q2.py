def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val)
    in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Iterate through the list by index to modify it with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    return lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:

# Scenario 1: Replacing integers
scenario1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(f"Scenario 1 result: {scenario1}")

# Scenario 2: Replacing strings
scenario2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(f"Scenario 2 result: {scenario2}")