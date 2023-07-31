class Square:
    def __init__(self, size=0):
        self.__size = size

        # Perform size validation
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2