"""
Module: geometry_classes

This module defines base and derived geometric classes.

Classes:
- BaseGeometry: A base class for geometric calculations.
- Rectangle: A class representing a rectangle.
- Square: A class representing a square, which is a specific type of rectangle.

Module Author:
Laurels Echichinwo

Last Updated:
04/08/2023

"""


class BaseGeometry:
    """
    A base class for geometric calculations.

    Methods:
    - area(): Raises an exception indicating calculation not implemented.
    - integer_validator(name, value): Validates a value as positive integer.

    Attributes:
    None
    """

    def area(self):
        """
        Calculate the area of geometric shape. Not implemented in base class.

        Raises:
        Exception: Indicates that area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Methods:
    - __init__(width, height): Initialize a Rectangle instance.
    - area(): Calculate the area of the rectangle.
    - __str__(): Return a string representation of the rectangle.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        str: A string in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    A class representing a square, which is a specific type of rectangle.

    Methods:
    - __init__(size): Initialize a Square instance with a size.
    - area(): Calculate the area of the square.

    Attributes:
    - __size (int): The size of the square, representing both width and height.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a size.

        Args:
        size (int): The size of the square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
