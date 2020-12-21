import numpy as np
import matplotlib.pyplot as plt

from camera import Camera
from surface import Surface
from surfaces import Surfaces
from ray import Ray
from light_source import LightSource


class RayTracer:

    def _init_room(self):
        leftWall = Surface(np.array([1.25, -0.75, 0]), np.array([0, 1.5, 0]), np.array([0, 0, 2.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        rightWall = Surface(np.array([-1.25, -0.75, 0]), np.array([0, 1.5, 0]), np.array([0, 0, 2.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        bottomWall = Surface(np.array([1.25, -0.75, 0]), np.array([0, 0, 2.5]), np.array([-2.5, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        topWall = Surface(np.array([1.25, 0.75, 0]), np.array([-2.5, 0, 0]), np.array([0, 0, 2.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        backWall = Surface(np.array([1.25, -0.75, 2.5]), np.array([-2.5, 0, 0]), np.array([0, 1.5, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        room = Surfaces(leftWall, rightWall, bottomWall, topWall, backWall)
        return room

    def _init_cuboid(self):
        frontRighttCuboid = Surface(np.array([-0.6, -0.75, 0.5]), np.array([0, 1, 0]), np.array([-0.25, 0, 0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        frontLeftCuboid = Surface(np.array([-0.6, -0.75, 0.5]), np.array([0, 1, 0]), np.array([0.25, 0, 0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        backLeftCuboid = Surface(np.array([-0.6, -0.75, 1]), np.array([0, 1, 0]), np.array([0.25, 0, -0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        backRightCuboid = Surface(np.array([-0.6, -0.75, 1]), np.array([0, 1, 0]), np.array([-0.25, 0, -0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        bottomCuboid = Surface(np.array([-0.6, -0.75, 0.5]), np.array([-0.25, 0, 0.25]), np.array([0.25, 0, 0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        topCuboid = Surface(np.array([-0.6, 0.25, 0.5]), np.array([-0.25, 0, 0.25]), np.array([0.25, 0, 0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        cuboid = Surfaces(frontRighttCuboid, frontLeftCuboid, backLeftCuboid, backRightCuboid, bottomCuboid, topCuboid)
        return cuboid

    def _init_cube(self):
        frontCube = Surface(np.array([0.75, -0.75, 0.5]), np.array([0, 0.5, 0]), np.array([-0.5, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        leftCube = Surface(np.array([0.75, -0.75, 0.5]), np.array([0, 0.5, 0]), np.array([0, 0, 0.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        bottomCube = Surface(np.array([0.75, -0.75, 0.5]), np.array([-0.5, 0, 0]), np.array([0, 0, 0.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        backCube = Surface(np.array([0.25, -0.25, 1]), np.array([0.5, 0, 0]), np.array([0, -0.5, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        rightCube = Surface(np.array([0.25, -0.25, 1]), np.array([0, 0, -0.5]), np.array([0, -0.5, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        topCube = Surface(np.array([0.25, -0.25, 1]), np.array([0, 0, -0.5]), np.array([0.5, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
        cube = Surfaces(frontCube, leftCube, bottomCube, backCube, rightCube, topCube)
        return cube

    def _initAllSurfaces(self):
        room = self._init_room()
        cuboid = self._init_cuboid()
        cube = self._init_cube()
        allSurfaceList = room.sflist
        allSurfaceList.extend(cuboid.sflist)
        allSurfaceList.extend(cube.sflist)
        allSurfaces = Surfaces(*allSurfaceList)
        return allSurfaces

    def _initLightSource(self):
        lightSource = LightSource(self.allSurfaces)
        return lightSource

    def __init__(self, heightpx, widthpx):
        self.camera = Camera(heightpx, widthpx)
        self.allSurfaces = self._initAllSurfaces()
        self.lightSource = self._initLightSource()
        self._picturecap = np.zeros((heightpx, widthpx, 3))
        self._max_depth = 5

    def _getPositiveNormVec(self, normVec, surfPos, origin):
        NormPointOrigVek= origin - (surfPos + normVec)
        AntiPointOrigVek= origin - (surfPos - normVec)
        distNOV = np.sqrt(np.square(NormPointOrigVek[0]) + np.square(NormPointOrigVek[1]) + np.square(NormPointOrigVek[2]))
        distAOV =np.sqrt(np.square(AntiPointOrigVek[0]) + np.square(AntiPointOrigVek[1]) + np.square(AntiPointOrigVek[2]))
        if distNOV < distAOV:
            return normVec
        elif distNOV > distAOV:
            return 0 - normVec

    def traceRays(self, heightPx, widthPx):
        ray = self.camera.calculateRay(widthPx, heightPx)
        color = np.zeros((3))
        reflection = 1
        for i in range(self._max_depth):
            collisionSurf, minDistance = self.allSurfaces.getCollisionObject(ray)
            if collisionSurf is None:
                break
            #pos auf der surface
            surfPos = ray.origin + minDistance * ray.normDirection
            #normVek der surface
            surfNorm = collisionSurf.norm
            surfNorm = self._getPositiveNormVec(surfNorm, surfPos, ray.origin)
            #shiftedPosVek des auftrittspunkt der surface
            surfShiftPos = surfPos + 1e-6 * surfNorm
            #define illumination var
            illumination = np.zeros((3))
            #calculate shaded part
            shadedPart = float(self.lightSource.checkIfShadowed(surfPos, randomShadowRayCount=0, systematicShadowRayCountRoot=2))
            if shadedPart != 1:
                illumination += self.lightSource.getAmbient()
                illumination += self.lightSource.getDiffuse(surfNorm, surfPos)
                illumination += self.lightSource.getSpecular(surfNorm, surfPos, self.camera.cameraCords,
                    collisionSurf.shinyness)
                color += reflection * illumination
            reflection *= collisionSurf.reflection
            ray.reflect(surfNorm, surfShiftPos)
        self._picturecap[heightPx, widthPx] = np.clip(color, 0, 1)




    def printImage(self, name: str):
        plt.imsave("%s.png"%name, self._picturecap)
