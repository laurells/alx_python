class Square:
    def __init__(self, size):
        """
        Initialize a Square object with the given size.

        Parameters:
            size (int): The size of the square.

        Raises:
            None

        Returns:
            None
        """
        self.__size = size

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

    def perimeter(self):
        """
        Calculate and return the perimeter of the square.

        Parameters:
            None

        Raises:
            None

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.__size

    def get_size(self):
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

    def set_size(self, size):
        """
        Set the size of the square to the given value.

        Parameters:
            size (int): The new size of the square.

        Raises:
            None

        Returns:
            None
        """
        self.__size = size
