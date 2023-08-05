"""
Module: geometry_classes

This module defines base and derived geometric classes for calculations and validations.

Classes:
- BaseGeometry: A base class for geometric calculations.

Module Author:
Laurels Echichinwo

Last Updated:
04/08/2023

"""


class BaseGeometry:
    """
    A base class for geometric calculations.

    Methods:
    - area(): Raises an exception indicating that area calculation is not implemented.
    - integer_validator(name, value): Validates that a value is a positive integer.

    Attributes:
    None
    """

    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [
            item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list

    def area(self):
        """
        Calculate the area of a geometric shape. Not implemented in the base class.

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
