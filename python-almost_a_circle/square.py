"""
Module: square.py
This module defines the Square class, which inherits from the Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, a subclass of the Rectangle class.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The unique identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides the __str__ method to provide a custom string representation.

        Returns:
            str: A formatted string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
