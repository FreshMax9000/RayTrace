import numpy as np

class PhongProperties:
    def __init__(self, ambient: np.array, diffuse: np.array, specular: np.array):
        """Constructor method
        """
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular