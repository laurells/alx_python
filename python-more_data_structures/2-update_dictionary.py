def update_dictionary(a_dictionary, key, value):
    if not isinstance(key, str):
        raise TypeError("Key must be a string")
    
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # If the key exists, update the value
        a_dictionary[key] = value
    else:
        # If the key doesn't exist, add a new key-value pair
        a_dictionary[key] = value
