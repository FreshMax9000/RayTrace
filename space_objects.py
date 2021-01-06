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


class ComplexSpaceObject:

    def __init__(self, origin, spaceObjectList):
        self.subObjList = spaceObjectList
        self.origin = origin

    def rotate(self, rotVec: np.ndarray):
        for obj in self.subObjList:
            obj.geoObj.rotate(self.origin, rotVec)

    def translate(self, transVec: np.ndarray):
        self.origin += transVec
        for obj in self.subObjList:
            obj.geoObj.move(transVec)


class SpaceObjects:

    def __init__(self, complexDict: dict):
        self.complexDict = complexDict

    def checkSingleObject(self, spaceObj: SpaceObject, ray: Ray):
        return spaceObj.getCollision(ray)

    def checkIfCollisionRay(self, ray: Ray):
        objList = []
        for complexObjKey in self.complexDict:
            objList.extend(self.complexDict[complexObjKey].subObjList)

        surfaceDistanceArray = np.array(list(map(self.checkSingleObject, objList, [ray]*len(objList))), dtype=object)
        
        minVal = surfaceDistanceArray.min(where=[False, True], initial = np.inf) 
        minimums = np.where(surfaceDistanceArray[:, 1] == minVal)
        r_val = surfaceDistanceArray[minimums[0]][0]
        return r_val
