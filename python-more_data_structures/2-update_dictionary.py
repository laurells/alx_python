def update_dictionary(a_dictionary, key, value):
    if not isinstance(key, str):
        raise TypeError("Key must be a string")

    # Check if the dictionary is None or empty
    if a_dictionary is None:
        a_dictionary = {}  # Create an empty dictionary

    # Update the dictionary with the key-value pair
    a_dictionary[key] = value
    return a_dictionary
