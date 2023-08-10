"""
A module containing a base class to manage the 'id' attribute for other classes.
"""

class Base:
    """
    The base class to manage the 'id' attribute for other classes.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number of objects created.
    """

    __nb_objects = 0  # Private class attribute to count the number of objects created

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): If provided, assigns the 'id' attribute with the specified value.
                               If None, increments __nb_objects and assigns the new value to 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1  # Increment the object counter
            self.id = Base.__nb_objects  # Assign the new value to the 'id' attribute

# Test
obj1 = MyClass1(name="Object 1")
obj2 = MyClass2(value="Value 1")
obj3 = MyClass1()
obj4 = MyClass2()

print(obj1.id)  # Output: 1
print(obj2.id)  # Output: 1
print(obj3.id)  # Output: 2
print(obj4.id)  # Output: 2