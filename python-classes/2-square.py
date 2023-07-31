# 2-square.py

"""Square Module

This module defines the Square class, representing a square shape.

Example:
    Create a square with a size of 5 and calculates its area.
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
        self.__size = size

        # Perform size validation
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

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

