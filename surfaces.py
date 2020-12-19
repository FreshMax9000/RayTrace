"""This moule contains the class Surfaces
"""
import numpy as np

class Surfaces:

    def __init__(self, *surfacelist):
        """Constructor method
        """
        self.__sflist = surfacelist
        

    
    
    @property
    def sflist(self):
        #Getter for supVec
        
        return self.__sflist

    def checkIfCollisionObj(self, ray):
    

        
    
