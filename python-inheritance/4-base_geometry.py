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

    Attributes:
    None
    """
    def area(self):
        """
        Calculate the area of a geometric shape. Not implemented in the base class.

        Raises:
        Exception: Indicates that area calculation is not implemented.
        """
        raise Exception("area() is not implemented")
