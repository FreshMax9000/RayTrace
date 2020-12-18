import numpy as np
from screen import Screen

class Camera:
    def __init__(self, cameraCords: np.array, heightpx: int, widthpx: int):
        """Constructor method
        """
        self._cameraCords = cameraCords
        self._heightpx = heightpx
        self._withpx = widthpx
        
        # screen = Screen()

    # def calculateRay(self, x: int, y: int):
        
    #    return  Ray
    
