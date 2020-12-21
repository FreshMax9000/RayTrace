import numpy as np

from ray import Ray
from screen import Screen

class Camera:
    def __init__(self, heightpx: int, widthpx: int):
        """Constructor method
        """
        self.__cameraCords = np.array([0, 0, -1]) #maybe -1 for z doesnt work
        self.__heightpx = heightpx
        self.__widthpx = widthpx
        ratio = float(widthpx) / heightpx
        self._screen = Screen(-1/ratio, 1/ratio, 1, -1)

    def calculateRay(self, x: int, y: int):
        pixel_x_pos = x / self.__widthpx + self._screen.left
        pixel_y_pos = y / self.__heightpx + self._screen.bottom
        direction = np.array([pixel_x_pos, pixel_y_pos, 1])
        ray = Ray(self.__cameraCords, direction)
        return ray
    
