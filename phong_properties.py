import numpy as np

class PhongProperties:
       
    def __init__(self, color: np.array, ambientMult: float, diffuseMult: float, specularMult: float,
    specularWhite=True):
        self.ambient = ambientMult * color
        self.diffuse = diffuseMult * color
        if specularWhite:
            self.specular = specularMult * np.array([1, 1, 1])
        else:
            self.specular = specularMult * color