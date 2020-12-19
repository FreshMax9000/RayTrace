import numpy as np

class Screen:
    def __init__(self, bottom: float, top: float, left: float, right: float):
        self._bottom = bottom
        self._top = top
        self._left = left
        self._right = right

    @property
    def bottom(self):
        """Getter for bottom
        """
        return self._bottom
        
    @property
    def top(self):
        """Getter for top
        """
        return self._top
        
    @property
    def left(self):
        """Getter for left
        """
        return self._left
        
    @property
    def right(self):
        """Getter for right
        """
        return self._right