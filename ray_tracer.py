import numpy as np
import matplotlib.pyplot as plt

from camera import Camera
from surface import Surface
from surfaces import Surfaces
from ray import Ray
from light_source import LightSource
from plane import Plane
from phong_properties import PhongProperties


class RayTracer:

    def _init_room(self):
        """
        rightWallPlane = Plane(np.array([1.25, -0.75, 0]), np.array([0, 1.5, 0]), np.array([0, 0, -2.5]))
        leftWallPlane = Plane(np.array([-1.25, -0.75, 0]), np.array([0, 1.5, 0]), np.array([0, 0, -2.5]))
        bottomWallPlane = Plane(np.array([1.25, -0.75, 0]), np.array([0, 0, -2.5]), np.array([-2.5, 0, 0]))
        topWallPlane = Plane(np.array([1.25, 0.75, 0]), np.array([-2.5, 0, 0]), np.array([0, 0, -2.5]))
        backWallPlane = Plane(np.array([1.25, -0.75, -2.5]), np.array([-2.5, 0, 0]), np.array([0, 1.5, 0]))
        """
        rightWallPlane = Plane(np.array([1.25, -0.75, 1.5]), np.array([0, 1.5, 0]), np.array([0, 0, -14]))
        leftWallPlane = Plane(np.array([-1.25, -0.75, 1.5]), np.array([0, 1.5, 0]), np.array([0, 0, -14]))
        bottomWallPlane = Plane(np.array([1.25, -0.75, 1.5]), np.array([0, 0, -14]), np.array([-2.5, 0, 0]))
        topWallPlane = Plane(np.array([1.25, 0.75, 1.5]), np.array([-2.5, 0, 0]), np.array([0, 0, -14]))
        backWallPlane = Plane(np.array([1.25, -0.75, -2.5]), np.array([-2.5, 0, 0]), np.array([0, 1.5, 0]))
        frontWallPlane = Plane(np.array([1.25, -0.75, 11.5]), np.array([-2.5, 0, 0]), np.array([0, 1.5, 0]))
        
        ambientMult = 0.1
        diffuseMult = 0.2
        specularMult = 1.0
        redColor = np.array([1, 0, 0])
        blueColor = np.array([0, 0, 1])
        whiteColor = np.array([1, 1, 1])
        redPhong = PhongProperties(redColor, ambientMult, diffuseMult, specularMult)
        bluePhong = PhongProperties(blueColor, ambientMult, diffuseMult, specularMult)
        whitePhong = PhongProperties(whiteColor, ambientMult, diffuseMult, specularMult)

        shinyness = 1
        reflection = 0.1

        #left wall red, right wall blue, rest white
        rightWall = Surface(leftWallPlane, bluePhong, shinyness, reflection)
        leftWall = Surface(rightWallPlane, redPhong, shinyness, reflection)
        bottomWall = Surface(bottomWallPlane, whitePhong, shinyness, reflection)
        topWall = Surface(topWallPlane, whitePhong, shinyness, reflection)
        backWall = Surface(backWallPlane, whitePhong, shinyness, reflection)
        frontWall = Surface(frontWallPlane, whitePhong, shinyness, 0.0)

        room = Surfaces(leftWall, rightWall, bottomWall, topWall, backWall)
        return room

    def _init_cuboid(self):
        frontRightCuboidPlane = Plane(np.array([0.6, 0.75, -1]), np.array([0, -1, 0]), np.array([0.25, 0, -0.25]))
        frontLeftCuboidPlane = Plane(np.array([0.6, 0.75, -1]), np.array([0, -1, 0]), np.array([-0.25, 0, -0.25]))
        backLeftCuboidPlane = Plane(np.array([0.6, 0.75, -1.5]), np.array([0, -1, 0]), np.array([-0.25, 0, 0.25]))
        backRightCuboidPlane = Plane(np.array([0.6, 0.75, -1.5]), np.array([0, -1, 0]), np.array([0.25, 0, 0.25]))
        #bottomCuboidPlane = Plane(np.array([0.6, -0.75, -0.5]), np.array([0.25, 0, 0.25]), np.array([0.25, 0, -0.25]))
        topCuboidPlane = Plane(np.array([0.6, -0.25, -1]), np.array([-0.25, 0, -0.25]), np.array([0.25, 0, -0.25]))

        ambientMult = 0.15
        diffuseMult = 0.2
        specularMult = 1.0
        whiteColor = np.array([1, 1, 1])
        whitePhong = PhongProperties(whiteColor, ambientMult, diffuseMult, specularMult)

        shinyness = 2.0
        reflection = 0.2

        frontRightCuboid = Surface(frontRightCuboidPlane, whitePhong, shinyness, reflection)
        frontLeftCuboid = Surface(frontLeftCuboidPlane, whitePhong, shinyness, reflection)
        backLeftCuboid = Surface(backLeftCuboidPlane, whitePhong, shinyness, reflection)
        backRightCuboid = Surface(backRightCuboidPlane, whitePhong, shinyness, reflection)
        #bottomCuboid = Surface(bottomCuboidPlane, whitePhong, shinyness, reflection)
        topCuboid = Surface(topCuboidPlane, whitePhong, shinyness, reflection)

        cuboid = Surfaces(frontRightCuboid, frontLeftCuboid, backLeftCuboid, backRightCuboid, topCuboid)
        return cuboid

    def _init_cube(self):
        frontCubePlane = Plane(np.array([-0.75, 0.75, -1]), np.array([0, -0.5, 0]), np.array([0.5, 0, 0]))
        leftCubePlane = Plane(np.array([-0.75, 0.75, -1]), np.array([0, -0.5, 0]), np.array([0, 0, -0.5]))
        bottomCubePlane = Plane(np.array([-0.75, 0.75, -1.5]), np.array([0.5, 0, 0]), np.array([0, 0, -0.5]))
        backCubePlane = Plane(np.array([-0.25, 0.25, -1.5]), np.array([-0.5, 0, 0]), np.array([0, 0.5, 0]))
        rightCubePlane = Plane(np.array([-0.25, 0.25, -1.5]), np.array([0, 0, 0.5]), np.array([0, 0.5, 0]))
        topCubePlane = Plane(np.array([-0.25, 0.25, -1.5]), np.array([0, 0, 0.5]), np.array([-0.5, 0, 0]))

        ambientMult = 0.15
        diffuseMult = 0.2
        specularMult = 1.0
        yellowColor = np.array([1, 1, 0])
        yellowPhong = PhongProperties(yellowColor, ambientMult, diffuseMult, specularMult)

        shinyness = 2.0
        reflection = 0.2

        frontCube = Surface(frontCubePlane, yellowPhong, shinyness, reflection)
        leftCube = Surface(leftCubePlane, yellowPhong, shinyness, reflection)
        bottomCube = Surface(bottomCubePlane, yellowPhong, shinyness, reflection)
        backCube = Surface(backCubePlane, yellowPhong, shinyness, reflection)
        rightCube = Surface(rightCubePlane, yellowPhong, shinyness, reflection)
        topCube = Surface(topCubePlane, yellowPhong, shinyness, reflection)

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
        supVec = np.array([0.1, -0.74, -1.6])
        dirVec1 = np.array([-0.2, 0, 0])
        dirVec2 = np.array([0, 0, -0.2])
        plane = Plane(supVec, dirVec1, dirVec2)
        phongProp = PhongProperties(np.array([1, 1, 1]), 1, 1, 0.7)
        lightSource = LightSource(self.allSurfaces, plane, phongProp)
        return lightSource

    def __init__(self, heightpx, widthpx, max_depth=3, randomShadowRays = 4, systematicShadowRayRoot = 2):
        self.camera = Camera(heightpx, widthpx)
        self.allSurfaces = self._initAllSurfaces()
        self.lightSource = self._initLightSource()
        self._picturecap = np.zeros((heightpx, widthpx, 3))
        self._max_depth = max_depth
        self._rSR = randomShadowRays
        self._sSRR = systematicShadowRayRoot

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
        for i in range(self._max_depth):
            collisionSurf, minDistance = self.allSurfaces.getCollisionObject(ray)
            if collisionSurf is None:
                break
            #pos auf der surface
            surfPos = ray.origin + minDistance * ray.normDirection
            #normVek der surface
            surfNorm = collisionSurf.plane.getPositiveNormVec(ray.origin)
            #shiftedPosVek des auftrittspunkt der surface
            surfShiftPos = surfPos + 1e-5 * surfNorm
            #define illumination var
            illumination = np.zeros((3))
            #calculate shaded part
            shadedPart = float(self.lightSource.checkIfShadowed(surfShiftPos, randomShadowRayCount=self._rSR, systematicShadowRayCountRoot=self._sSRR))
            #shadedPart = 0.0
            #illumination += collisionSurf.phong.ambient * self.lightSource.getAmbient()
            if shadedPart != 1:
                """
                illumination += collisionSurf.phong.diffuse * self.lightSource.getDiffuse(surfNorm, surfPos)
                
                illumination += collisionSurf.phong.specular * self.lightSource.getSpecular(surfNorm, surfPos,
                    self.camera.cameraCords, collisionSurf.shinyness)
                """
                if widthPx == 78 and heightPx == 17:
                    print("yahoo!")
                lightDiffuse, lightSpecular = self.lightSource.getIllumination(surfNorm, surfPos,
                    self.camera.cameraCords, collisionSurf.shinyness)
                #illumination += collisionSurf.phong.diffuse * lightDiffuse
                
                illumination += collisionSurf.phong.specular * lightSpecular
                
                illumination *= (1 - shadedPart)
                color += reflection * illumination
            reflection *= collisionSurf.reflection
            if reflection == 0:
                break
            ray.reflect(surfNorm, surfShiftPos)
        self._picturecap[heightPx, widthPx] = np.clip(color, 0, 1)




    def printImage(self, name: str):
        plt.imsave("%s.png"%name, self._picturecap)
