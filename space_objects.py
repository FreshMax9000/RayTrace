import numpy as np

from ray import Ray
from geometric_objects import Plane
from phong_properties import PhongProperties
from geometric_objects import GeometricObject

class SpaceObject:

    def __init__(self, geoObj: GeometricObject, phongProp: PhongProperties, shinyness: float, reflection: float):
        """Constructor method
        """
        self.geoObj = geoObj
        self.phong = phongProp
        self.shinyness = shinyness
        self.reflection = reflection

    def getCollision(self, ray):
        return (self, self.geoObj.checkCollision(ray))

    @property
    def norm(self):
        """Normal vector of surface
        """
        return self.geoObj.getNorm()

class SpaceObjects:

    def __init__(self, objList):
        self.objList = objList

    def checkSingleObject(self, spaceObj: SpaceObject, ray: Ray):
        return spaceObj.getCollision(ray)

    def checkIfCollisionRay(self, ray: Ray):
        surfaceDistanceArray = np.array(list(map(self.checkSingleObject, self.objList, [ray]*len(self.objList))), dtype=object)
            
        minVal = surfaceDistanceArray.min(where=[False, True], initial = np.inf) 
        minimums = np.where(surfaceDistanceArray[:, 1] == minVal)
        r_val = surfaceDistanceArray[minimums[0]][0]
        return r_val
