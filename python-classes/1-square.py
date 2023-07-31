class Square:
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
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

    def set_size(self, size=0):
        """
        Set the size of the square to the given value.

        Parameters:
            size (int, optional): The new size of the square. Defaults to 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
