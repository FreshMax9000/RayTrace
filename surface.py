"""This moule contains the class Surface 
"""
import numpy as np

from ray import Ray
from plane import Plane
from phong_properties import PhongProperties

class Surface:

    def __init__(self, supVec: np.array, dirVec1: np.array, dirVec2: np.array, 
    ambient: np.array, diffuse: np.array, specular: np.array, shinyness: float, reflection: float):
        """Constructor method
        """
        self.plane = Plane(supVec, dirVec1, dirVec2)
        self.phongProperties = PhongProperties(ambient, diffuse, specular)

        self._shinyness = shinyness
        self._reflection = reflection

    @property
    def shinyness(self):
        """Getter for shinyness
        """
        return self._shinyness    
            
    @property
    def reflection(self):
        """Getter for reflection
        """
        return self._reflection

    @property
    def norm(self):
        """Normal vector of surface
        """
        return Ray.normalizeVector(np.cross(self.plane.dirVec1, self.plane.dirVec2))
