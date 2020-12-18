"""This moule contains the class Surface
"""
import numpy as np

class Surface:

    def __init__(self, supVec: np.array, dirVec1: np.array, dirVec2: np.array, 
    ambient: np.array, diffuse: np.array, specular: np.array, shinyness: float, reflection: float):
        """Constructor method
        """
        self._supVec = supVec
        self._dirVec1 = dirVec1
        self._dirVec2 = dirVec2
        self._ambient = ambient
        self._diffuse = diffuse
        self._specular = specular
        self._shinyness = shinyness
        self._reflection = reflection


    @property
    def supVec(self):
        """Getter for supVec
        """
        return self._supVec
        
    @property
    def dirVec1(self):
        """Getter for dirVec1
        """
        return self._dirVec1

    @property
    def dirVec2(self):
        """Getter for dirVec2
        """
        return self._dirVec2

    @property
    def ambient(self):
        """Getter for ambient
        """
        return self._ambient
    
    @property
    def diffuse(self):
        """Getter for diffuse
        """
        return self._diffuse

    @property
    def specular(self):
        """Getter for specular
        """
        return self._specular

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
