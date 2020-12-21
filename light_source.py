import numpy as np

from ray import Ray
from surfaces import Surfaces


def vector3d(x: float, y: float, z: float):
    return np.array([x, y, z])


class LightSource:

    def __init__(self, surfaces: Surfaces, supVec = vector3d(0.25, 0.75, 1), dirVec1 = vector3d(-0.2, 0, 0),
        dirVec2 = vector3d(0, 0, 0.2), ambient = vector3d(1, 1, 1), diffuse = vector3d(1, 1, 1),
        specular = vector3d(1, 1, 1)):
        self._surfaces = surfaces
        self._supVec = supVec
        self._dirVec1 = dirVec1
        self._dirVec2 = dirVec2
        self._ambient = ambient
        self._diffuse = diffuse
        self._specular = specular
        self._middle = self._supVec + self._dirVec1 / 2 + self._dirVec2 / 2

    def _generate_aim(self, aimX: float, aimY: float):
        return self._supVec + aimX * self._dirVec1 + aimY * self._dirVec2

    def _generateShadowRay(self, aim, sourcePos):
        return Ray(sourcePos, aim - sourcePos), np.linalg.norm(aim - sourcePos)

    def _generateRandomShadowRay(self, sourcePos: np.ndarray):
        aim = self._generate_aim(np.random.rand(), np.random.rand())
        return self._generateShadowRay(aim, sourcePos)

    def _generateSystematicShadowRayList(self, sourcePos, systematicShadowRayCountRoot):
        x = np.linspace(0, 1, systematicShadowRayCountRoot)
        aimCords = list(np.array(np.meshgrid(x, x)).T.reshape(-1, 2)) #list might be slow
        rayDistanceList = []
        for aimCord in aimCords:
            rayDistanceList.append(self._generateShadowRay(self._generate_aim(aimCord[0], aimCord[1]), sourcePos))
        return rayDistanceList

    def checkIfShadowed(self, position: np.ndarray, randomShadowRayCount = 64,
        systematicShadowRayCountRoot = 8):
        """Estimates the percentages this point is blocked from a rectangular light source

        This is done by generating random and systematic shadow rays which are cast to points (aim)
        on the rectangular light source. Depending on how much of these are interrupted by objects
        on their way, a float value between 0 (not blocked at all) and 1 (fully blocked from the
        light source) is returned.

        Args:
            position(numpy 3d vector): The position for which the shadowed percentage shall be
                determined
            randomShadowRayCount(int): The count of random shadow rays to be cast
            systematicShadowRayCountRoot(int): The square root of the count of the sytematic shadow rays
                to be cast. 
        
        Returns: 
            float: A value between 0 and 1 depending how much the given point is blocked from the light
            source. 0 = not blocked and 1 = fully blocked
        """
        shadowRayDistanceList = []
        #Generate random shadow rays
        for i in range(randomShadowRayCount):
            shadowRayDistanceList.append(self._generateRandomShadowRay(position))
        #Generate systematic shadow rays
        shadowRayDistanceList.extend(self._generateSystematicShadowRayList(position,
            systematicShadowRayCountRoot))
        #check how many shadow rays hit an object
        blockedRays = 0
        for rayDistance in shadowRayDistanceList:
            if self._surfaces.getCollisionObject(rayDistance[0])[1] < rayDistance[1]:
                blockedRays += 1
        return float(blockedRays) / (randomShadowRayCount + systematicShadowRayCountRoot ** 2)

    def getAmbient(self):
        return self._ambient

    def getDiffuse(self, surfNormV: np.ndarray, pos: np.ndarray):
        lightDir = Ray.normalizeVector(self._middle - pos)
        return self._diffuse * np.dot(lightDir, surfNormV)

    def getSpecular(self, surfNormV: np.ndarray, pos: np.ndarray, cameraPos: np.ndarray,
        shininess: float):
        lightDir = Ray.normalizeVector(self._middle - pos)
        cameraDir = Ray.normalizeVector(cameraPos - pos)
        optReflAxis = Ray.normalizeVector(lightDir + cameraDir)
        return self._specular * np.dot(surfNormV, optReflAxis) ** (shininess / 4)
