import numpy as np

class PhongProperties:
       
    def __init__(self, color: np.array, ambientMult: float, diffuseMult: float, specularMult: float):
        self.ambient = ambientMult * color
        self.diffuse = diffuseMult * color
        self.specular = specularMult * color