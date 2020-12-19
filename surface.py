"""This moule contains the class Surface 
"""
import numpy as np

class Surface:

    def __init__(self, supVec: np.array, dirVec1: np.array, dirVec2: np.array, 
    ambient: np.array, diffuse: np.array, specular: np.array, shinyness: float, reflection: float):
        """Constructor method
        """
        self.__supVec = supVec
        self.__dirVec1 = dirVec1
        self.__dirVec2 = dirVec2
        self.__ambient = ambient
        self.__diffuse = diffuse
        self.__specular = specular
        self.__shinyness = shinyness
        self.__reflection = reflection


    @property
    def supVec(self):
        """Getter for supVec
        """
        return self.__supVec
        
    @property
    def dirVec1(self):
        """Getter for dirVec1
        """
        return self.__dirVec1

    @property
    def dirVec2(self):
        """Getter for dirVec2
        """
        return self.__dirVec2

    @property
    def ambient(self):
        """Getter for ambient
        """
        return self.__ambient
    
    @property
    def diffuse(self):
        """Getter for diffuse
        """
        return self.__diffuse

    @property
    def specular(self):
        """Getter for specular
        """
        return self.__specular

    @property
    def shinyness(self):
        """Getter for shinyness
        """
        return self.__shinyness    
            
    @property
    def reflection(self):
        """Getter for reflection
        """
        return self.__reflection
