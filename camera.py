import numpy as np

from ray import Ray
from screen import Screen

class Camera:
    def __init__(self, heightpx: int, widthpx: int):
        """Constructor method
        """
        self._cameraCords = np.array([0, 0, -1]) #maybe -1 for z doesnt work
        self._heightpx = heightpx
        self._withpx = widthpx
        ratio = float(widthpx) / heightpx
        self._screen = Screen(-1/ratio, 1/ratio, -1, 1)

    def calculateRay(self, x: int, y: int):
        pixel_x_pos = x / self._withpx + self._screen.left
        pixel_y_pos = y / self._heightpx + self._screen.bottom
        direction = np.array([pixel_x_pos, pixel_y_pos, 0])
        ray = Ray(self._cameraCords, direction)
        return ray
    
