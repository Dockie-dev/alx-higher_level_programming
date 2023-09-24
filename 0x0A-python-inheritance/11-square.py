#!/usr/bin/python3
"""Module for the Square class."""

class BaseGeometry:
    """A BaseGeometry class."""
    
    def area(self):
        """Calculate the area (not implemented)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """A Rectangle class."""
    
    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
