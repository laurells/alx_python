# 3-square.py

"""Square Module

This module defines the Square class, representing a square shape.

Example:
    Create a square with a size of 5, calculate its area and print its pattern.
    >>> square = Square(5)
    >>> square.area()
    25

Attributes:
    None

"""

class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize a Square object with the given size.
        area(self): Calculate and return the area of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a Square object with the given size.

        Parameters:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.

        Returns:
            None
        """
        self.size = size  # Using the setter to perform size validation

    @property
    def size(self):
        """
        Get the current size of the square.

        Parameters:
            None

        Raises:
            None

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square to the given value.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Parameters:
            None

        Raises:
            None

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
