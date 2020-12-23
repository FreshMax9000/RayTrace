"""This moule contains the class Surface 
"""
import numpy as np

from ray import Ray
from plane import Plane
from phong_properties import PhongProperties

class Surface:

    def __init__(self, plane: Plane, phongProp: PhongProperties, shinyness: float, reflection: float):
        """Constructor method
        """
        self.plane = plane
        self.phong = phongProp

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
        return self.plane.norm

    
