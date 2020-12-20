import numpy as np

from ray import Ray
from surfaces import Surfaces


def vector3d(x: float, y: float, z: float):
    return np.array([x, y, z])


class LightSource:

    def __init__(self, surfaces: Surfaces, supVec = vector3d(0, 0, 0), dirVec1 = vector3d(1, 0, 0),
        dirVec2 = vector3d(0, 1, 0), ambient = vector3d(1, 1, 1), diffuse = vector3d(1, 1, 1),
        specular = vector3d(1, 1, 1)):
        self._surfaces = surfaces
        self._supVec = supVec
        self._dirVec1 = dirVec1
        self._dirVec2 = dirVec2
        self._ambient = ambient
        self._diffuse = diffuse
        self._specular = specular
        self._middle = self._supVec + self._dirVec1 / 2 + self._dirVec2 / 2

    def _generateRandomShadowRay(self, sourcePos: np.ndarray):
        aim = self._supVec + np.random.rand() * self._dirVec1 + np.random.rand() * self._dirVec2
        return Ray(sourcePos, aim - sourcePos), np.linalg.norm(aim - sourcePos)

    def checkIfShadowed(self, position: np.ndarray, randomShadowRayCount = 64):
        shadowRayList = []
        shadowRayDistanceList = []
        #Generate shadow rays
        for i in range(randomShadowRayCount):
            ray, distance = self._generateRandomShadowRay(position)
            shadowRayList.append(ray)
            shadowRayDistanceList.append(distance)
        #check how many shadow rays hit an object
        blockedRays = 0
        for i, shadowRay in enumerate(shadowRayList):
            if self._surfaces.checkIfCollisionObj(shadowRay)[1] < shadowRayDistanceList[i]:
                blockedRays += 1
        return float(blockedRays) / randomShadowRayCount

    def getAmbient(self):
        return self._ambient

    def getDiffuse(self, surfNormV: np.ndarray, pos: np.ndarray):
        lightDir = Ray.normalizeVector(self._middle - pos)
        return self._diffuse * np.dot(lightDir, surfNormV)

    def getSpecular(self, surfNormV: np.ndarray, pos: np.ndarray, cameraPos: np.ndarray, shininess: float):
        lightDir = Ray.normalizeVector(self._middle - pos)
        cameraDir = Ray.normalizeVector(cameraPos - pos)
        optReflAxis = Ray.normalizeVector(lightDir + cameraDir)
        return self._specular * np.dot(surfNormV, optReflAxis) ** (shininess / 4)