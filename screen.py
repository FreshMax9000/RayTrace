import numpy as np

class Screen:
    def __init__(self, bottom: float, top: float, left: float, right: float):
        self.__bottom = bottom
        self.__top = top
        self.__left = left
        self.__right = right

    @property
    def bottom(self):
        """Getter for bottom
        """
        return self.__bottom
        
    @property
    def top(self):
        """Getter for top
        """
        return self.__top
        
    @property
    def left(self):
        """Getter for left
        """
        return self.__left
        
    @property
    def right(self):
        """Getter for right
        """
        return self.__right