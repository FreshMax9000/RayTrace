"""This moule contains the class Surface 
"""
import numpy as np

from ray import Ray
from plane import Plane
from phong_properties import PhongProperties

class Surface:

    def __init__(self, name: str, plane: Plane, phongProp: PhongProperties, shinyness: float, reflection: float):
        """Constructor method
        """
        self.name = name
        self.plane = plane
        self.phong = phongProp
        self.name = name
        self.shinyness = shinyness
        self.reflection = reflection

    @property
    def norm(self):
        """Normal vector of surface
        """
        return self.plane.norm

    
