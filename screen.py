import numpy as np

class Screen:
    def __init__(self, bottomLeft: np.array, bottomRight: np.array, topLeft: np.array, topRight: np.array):
        self._bottomLeft = bottomLeft
        self._bottomRight = bottomRight
        self._topLeft = topLeft
        self._topRight = topRight

    @property
    def bottomLeft(self):
        """Getter for bottomLeft
        """
        return self._bottomLeft
        
    @property
    def bottomRight(self):
        """Getter for bottomRight
        """
        return self._bottomRight
        
    @property
    def topLeft(self):
        """Getter for topLeft
        """
        return self._topLeft
        
    @property
    def topRight(self):
        """Getter for topRight
        """
        return self._topRight