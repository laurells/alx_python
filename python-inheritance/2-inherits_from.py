def inherits_from(obj, a_class):
    """
    Check if an object inherits (directly or indirectly) from a specified class.

    Args:
    obj: The object to be checked for inheritance.
    a_class (class): The class to check against.

    Returns:
    bool: True if the object inherits from the specified class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
