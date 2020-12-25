import numpy as np

from ray import Ray
from surfaces import Surfaces
from plane import Plane
from phong_properties import PhongProperties


def vector3d(x: float, y: float, z: float):
    return np.array([x, y, z])


class LightSource:

    def __init__(self, surfaces: Surfaces, plane: Plane, phongProp: PhongProperties):
        self._surfaces = surfaces
        self._plane = plane
        self._phong = phongProp
        self._middle = self._plane.supVec + self._plane.dirVec1 / 2 + self._plane.dirVec2 / 2

    def _generate_aim(self, aimX: float, aimY: float):
        return self._plane.supVec + aimX * self._plane.dirVec1 + aimY * self._plane.dirVec2

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

    #def _

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
            _, closestDistance = self._surfaces.getCollisionObject(rayDistance[0])
            if closestDistance < rayDistance[1]:
                blockedRays += 1
        return float(blockedRays) / (randomShadowRayCount + systematicShadowRayCountRoot ** 2)

    def getAmbient(self):
        return self._phong.ambient

    def getClosestPointOfLight(self, ray: Ray):
        #lightN = self._plane.getPositiveNormVec(ray.origin)
        lightN = self._plane.norm
        scalarLightNDir = np.dot(lightN, ray.normDirection)
        if scalarLightNDir == 0:
            n = 10000
        else:
            if scalarLightNDir > 0:
                n = (np.dot(lightN, self._plane.supVec) - np.dot(lightN, ray.origin)) / scalarLightNDir
            else:
                n = (np.dot(lightN, self._plane.supVec) - np.dot(lightN, ray.origin)) / scalarLightNDir
        lightPlaneIntersec = ray.calcPos(n)
        Ps = lightPlaneIntersec - self._plane.supVec
        closestPoint = self._plane.getClosestPoint(Ps)
        return closestPoint + self._plane.supVec # The point as viewed from the cartesian origin

    def getIllumination(self, surfNormV: np.ndarray, pos: np.ndarray, cameraPos: np.ndarray,
        shinyness: float):
        #diffuse
        lightDir = Ray.normalizeVector(self.getClosestPointOfLight(Ray(pos, self._middle - pos)) - pos)
        diffuse = self._phong.diffuse * np.dot(lightDir, surfNormV)
        #specular
        vectorFromCam = pos - cameraPos
        reflectedVector = vectorFromCam - 2 * (np.dot(vectorFromCam, surfNormV) * surfNormV)
        LightDir = Ray.normalizeVector(self.getClosestPointOfLight(Ray(pos, reflectedVector)) - pos)
        cameraDir = Ray.normalizeVector(cameraPos - pos)
        optReflAxis = Ray.normalizeVector(lightDir + cameraDir)
        specular = self._phong.specular * np.dot(surfNormV, optReflAxis) ** shinyness
        return (diffuse, specular)
