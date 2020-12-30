import numpy as np

from ray import Ray
from screen import Screen

class Camera:
    def __init__(self, heightpx: int, widthpx: int):
        """Constructor method
        """
        self.cameraCords = np.array([0, 0, 1])
        self.heightpx = heightpx
        self.widthpx = widthpx
        self.ratio = float(widthpx) / heightpx
        self.screen = Screen(-1/self.ratio, 1/self.ratio, -1, 1)

    def calculateRay(self, x: int, y: int):
        pixel_x_pos = x * 2 / self.widthpx + self.screen.left
        pixel_y_pos = - y * (2 / self.ratio) / self.heightpx - self.screen.bottom
        direction = np.array([pixel_x_pos, pixel_y_pos, -1.25])
        ray = Ray(self.cameraCords, direction)
        return ray
    
