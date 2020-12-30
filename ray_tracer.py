from multiprocessing import Pool

import numpy as np
import matplotlib.pyplot as plt

from camera import Camera
from space_objects import SpaceObject
from space_objects import SpaceObjects
from ray import Ray
from light_source import LightSource
from geometric_objects import Plane
from phong_properties import PhongProperties


class RayTracer:

    def _init_room(self):
        
        rightWallPlane = Plane(np.array([1.25, -0.75, 1.25]), np.array([0, 1.5, 0]), np.array([0, 0, -3.75]))
        leftWallPlane = Plane(np.array([-1.25, -0.75, 1.25]), np.array([0, 1.5, 0]), np.array([0, 0, -3.75]))
        topWallPlane = Plane(np.array([1.25, -0.75, 1.25]), np.array([0, 0, -3.75]), np.array([-2.5, 0, 0]))
        bottomWallPlane = Plane(np.array([1.25, 0.75, 1.25]), np.array([-2.5, 0, 0]), np.array([0, 0, -3.75]))
        backWallPlane = Plane(np.array([1.25, -0.75, -2.5]), np.array([-2.5, 0, 0]), np.array([0, 1.5, 0]))
        frontWallPlane = Plane(np.array([-1.25, 0.75, 1.25]), np.array([2.5, 0, 0]), np.array([0, -1.5, 0]))

        
        ambientMult = 0.1
        diffuseMult = 0.3
        specularMult = 0.7
        redColor = np.array([1, 0, 0])
        blueColor = np.array([0, 0, 1])
        whiteColor = np.array([1, 1, 1])
        redPhong = PhongProperties(redColor, ambientMult, diffuseMult, specularMult)
        bluePhong = PhongProperties(blueColor, ambientMult, diffuseMult, specularMult)
        whitePhong = PhongProperties(whiteColor, ambientMult, diffuseMult, specularMult)

        shinyness = 2.0
        reflection = 0.0

        #left wall red, right wall blue, rest white
        rightWall = SpaceObject(leftWallPlane, bluePhong, shinyness, reflection)
        leftWall = SpaceObject(rightWallPlane, redPhong, shinyness, reflection)
        bottomWall = SpaceObject(bottomWallPlane, whitePhong, shinyness, reflection)
        topWall = SpaceObject(topWallPlane, whitePhong, shinyness, reflection)
        backWall = SpaceObject(backWallPlane, whitePhong, shinyness, reflection)
        frontWall = SpaceObject(frontWallPlane, whitePhong, shinyness, reflection)
        
        return [frontWall,leftWall, rightWall, bottomWall, topWall, backWall]

    def _init_cuboid(self):
        frontRightCuboidPlane = Plane(np.array([0.6, 0.75, -1]), np.array([0, -1, 0]), np.array([0.25, 0, -0.25]))
        frontLeftCuboidPlane = Plane(np.array([0.35, 0.75, -1.25]), np.array([0, -1, 0]), np.array([0.25, 0, 0.25]))
        backLeftCuboidPlane = Plane(np.array([0.6, 0.75, -1.5]), np.array([0, -1, 0]), np.array([-0.25, 0, 0.25]))
        backRightCuboidPlane = Plane(np.array([0.85, 0.75, -1.25]), np.array([0, -1, 0]), np.array([-0.25, 0, 0.25]))
        #bottomCuboidPlane = Plane(np.array([0.6, -0.75, -0.5]), np.array([0.25, 0, 0.25]), np.array([0.25, 0, -0.25]))
        topCuboidPlane = Plane(np.array([0.6, -0.25, -1]), np.array([-0.25, 0, -0.25]), np.array([0.25, 0, -0.25]))

        ambientMult = 0.1
        diffuseMult = 0.2
        specularMult = 1.0
        whiteColor = np.array([1, 1, 1])
        whitePhong = PhongProperties(whiteColor, ambientMult, diffuseMult, specularMult)

        shinyness = 2.0
        reflection = 0.25

        frontRightCuboid = SpaceObject(frontRightCuboidPlane, whitePhong, shinyness, reflection)
        frontLeftCuboid = SpaceObject(frontLeftCuboidPlane, whitePhong, shinyness, reflection)
        backLeftCuboid = SpaceObject(backLeftCuboidPlane, whitePhong, shinyness, reflection)
        backRightCuboid = SpaceObject(backRightCuboidPlane, whitePhong, shinyness, reflection)
        #bottomCuboid = Surface(bottomCuboidPlane, whitePhong, shinyness, reflection)
        topCuboid = SpaceObject(topCuboidPlane, whitePhong, shinyness, reflection)

        return [frontRightCuboid, frontLeftCuboid, backLeftCuboid, backRightCuboid, topCuboid]

    def _init_cube(self):
        frontCubePlane = Plane(np.array([-0.75, 0.75, -1]), np.array([0, -0.5, 0]), np.array([0.5, 0, 0]))
        leftCubePlane = Plane(np.array([-0.75, 0.75, -1]), np.array([0, -0.5, 0]), np.array([0, 0, -0.5]))
        #bottomCubePlane = Plane(np.array([-0.75, 0.75, -1.5]), np.array([0.5, 0, 0]), np.array([0, 0, -0.5]))
        backCubePlane = Plane(np.array([-0.75, 0.75, -1.5]), np.array([0.5, 0, 0]), np.array([0, -0.5, 0]))
        rightCubePlane = Plane(np.array([-0.25, 0.25, -1.5]), np.array([0, 0, 0.5]), np.array([0, 0.5, 0]))
        topCubePlane = Plane(np.array([-0.2501, 0.25, -1.5]), np.array([0, 0, 0.5]), np.array([-0.5001, 0, 0]))

        ambientMult = 0.1
        diffuseMult = 0.2
        specularMult = 1.0
        yellowColor = np.array([1, 1, 0])
        yellowPhong = PhongProperties(yellowColor, ambientMult, diffuseMult, specularMult)

        shinyness = 2.0
        reflection = 0.1

        frontCube = SpaceObject(frontCubePlane, yellowPhong, shinyness, reflection)
        leftCube = SpaceObject(leftCubePlane, yellowPhong, shinyness, reflection)
        #bottomCube = Surface(bottomCubePlane, yellowPhong, shinyness, reflection)
        backCube = SpaceObject(backCubePlane, yellowPhong, shinyness, reflection)
        rightCube = SpaceObject(rightCubePlane, yellowPhong, shinyness, reflection)
        topCube = SpaceObject(topCubePlane, yellowPhong, shinyness, reflection)

        return [frontCube, leftCube, backCube, rightCube, topCube]

    def _initAllSpaceObjects(self):
        allSpaceObjectsList = self._init_room()
        allSpaceObjectsList.extend(self._init_cuboid())
        allSpaceObjectsList.extend(self._init_cube())
        allSpaceObjects = SpaceObjects(allSpaceObjectsList)
        return allSpaceObjects

    def _initLightSource(self):
        supVec = np.array([0.1, -0.7499999, -1.6])
        dirVec1 = np.array([-0.2, 0, 0])
        dirVec2 = np.array([0, 0, -0.2])
        plane = Plane(supVec, dirVec1, dirVec2)
        phongProp = PhongProperties(np.array([1.0, 1.0, 0.6]), 1, 1, 0.6)
        lightSource = LightSource(self.allSpaceObjects, plane, phongProp)
        return lightSource

    def __init__(self, heightpx, widthpx, max_depth=3, randomShadowRays = 4, systematicShadowRayRoot = 2, processCount=None):
        self.camera = Camera(heightpx, widthpx)
        self.allSpaceObjects = self._initAllSpaceObjects()
        self.lightSource = self._initLightSource()
        self._picturecap = np.zeros((heightpx, widthpx, 3))
        self._max_depth = max_depth
        self._rSR = randomShadowRays
        self._sSRR = systematicShadowRayRoot
        self._processCount = processCount


    def _getPositiveNormVec(self, normVec, surfPos, origin):
        NormPointOrigVek= origin - (surfPos + normVec)
        AntiPointOrigVek= origin - (surfPos - normVec)
        distNOV = np.linalg.norm(NormPointOrigVek)
        distAOV = np.linalg.norm(AntiPointOrigVek)
        if distNOV < distAOV:
            return normVec
        elif distNOV > distAOV:
            normVec *= -1
            return normVec

    def traceRays(self, heightPx, widthPx):
        ray = self.camera.calculateRay(widthPx, heightPx)
        color = np.zeros((3))
        reflection = 1
        for _ in range(self._max_depth):
            collisionObj, minDistance = self.allSpaceObjects.checkIfCollisionRay(ray)
            if collisionObj is None:
                break
            #pos auf der surface
            surfPos = ray.origin + minDistance * ray.normDirection
            #normVek der surface
            surfNorm = collisionObj.norm
            #shiftedPosVek des auftrittspunkt der surface
            surfShiftPos = surfPos + 1e-5 * surfNorm
            #define illumination var
            illumination = np.zeros((3))
            #calculate shaded part
            shadedPart = float(self.lightSource.checkIfShadowed(surfShiftPos, randomShadowRayCount=self._rSR, systematicShadowRayCountRoot=self._sSRR))
            shadedPart *= 0.9
            illumination += collisionObj.phong.ambient * self.lightSource.getAmbient()
            lightDiffuse, lightSpecular = self.lightSource.getIllumination(surfNorm, surfPos,
                self.camera.cameraCords, collisionObj.shinyness)
            illumination += collisionObj.phong.diffuse * lightDiffuse                
            illumination += collisionObj.phong.specular * lightSpecular                
            illumination *= (1 - shadedPart)
            color += reflection * illumination
            reflection *= collisionObj.reflection
            if reflection == 0:
                break
            ray.reflect(surfNorm, surfShiftPos)
        self._picturecap[heightPx, widthPx] = np.clip(color, 0, 1)
        return np.clip(color, 0, 1)

    def renderLine(self, height_px):
        return np.array(list(map(self.traceRays, [height_px]*self.camera.widthpx, list(range(self.camera.widthpx)))))

    def renderPicture(self):
        heightPxs = list(range(self.camera.heightpx))
        #self._picturecap = np.array(list(map(self.renderLine, heightPxs)))
        with Pool(self._processCount) as p:
            self._picturecap = np.array(list(p.map(self.renderLine, heightPxs)))
            p.close()
            p.terminate()

    def printImage(self, name: str):
        plt.imsave("%s.png"%name, self._picturecap)

