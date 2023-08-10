"""
Module: rectangle.py
This module defines the Rectangle class, which inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle, a subclass of the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The unique identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        """
        self.validate_positive_integer(value, 'width')
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        """
        self.validate_positive_integer(value, 'height')
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.
        """
        self.validate_non_negative_integer(value, 'x')
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.
        """
        self.validate_non_negative_integer(value, 'y')
        self.__y = value

    def validate_positive_integer(self, value, attribute_name):
        """
        Validates that the given value is a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{attribute_name} must be a positive integer")

    def validate_non_negative_integer(self, value, attribute_name):
        """
        Validates that the given value is a non-negative integer.
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError(
                f"{attribute_name} must be a non-negative integer")
