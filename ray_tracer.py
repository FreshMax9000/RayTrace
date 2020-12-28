import numpy as np
import matplotlib.pyplot as plt

from camera import Camera
from surface import Surface
from surfaces import Surfaces
from ray import Ray
from light_source import LightSource
from plane import Plane
from phong_properties import PhongProperties


class PictureDisplay:

    def __init__(self, name: str):
        self.name = name
        fig, ax = plt.subplots(figsize=(4.0, 3.0))
        self.fig = fig
        self.ax = ax
        self.ax.set_title(name)

    def draw(self, image: np.ndarray):
        self.ax.cla()
        self.ax.imshow(image, interpolation="antialiased")        
        plt.pause(1e-10)       


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
        rightWall = Surface("rightWall",leftWallPlane, bluePhong, shinyness, reflection)
        leftWall = Surface("leftWall",rightWallPlane, redPhong, shinyness, reflection)
        bottomWall = Surface("bottomWall",bottomWallPlane, whitePhong, shinyness, reflection)
        topWall = Surface("topWall",topWallPlane, whitePhong, shinyness, reflection)
        backWall = Surface("backWall",backWallPlane, whitePhong, shinyness, reflection)
        frontWall = Surface("frontWall",frontWallPlane, whitePhong, shinyness, reflection)

        room = Surfaces(frontWall,leftWall, rightWall, bottomWall, topWall, backWall)
        return room

    def _init_cuboid(self):
        frontRightCuboidPlane = Plane(np.array([0.6, 0.75, -1]), np.array([0, -1, 0]), np.array([0.25, 0, -0.25]))
        frontLeftCuboidPlane = Plane(np.array([0.35, 0.75, -1.25]), np.array([0, -1, 0]), np.array([0.25, 0, 0.25]))
        backLeftCuboidPlane = Plane(np.array([0.6, 0.75, -1.5]), np.array([0, -1, 0]), np.array([-0.25, 0, 0.25]))
        backRightCuboidPlane = Plane(np.array([0.85, 0.75, -1.25]), np.array([0, -1, 0]), np.array([-0.25, 0, 0.25]))
        #bottomCuboidPlane = Plane(np.array([0.6, -0.75, -0.5]), np.array([0.25, 0, 0.25]), np.array([0.25, 0, -0.25]))
        topCuboidPlane = Plane(np.array([0.6, -0.25, -1]), np.array([-0.25, 0, -0.25]), np.array([0.25, 0, -0.25]))

        ambientMult = 0.15
        diffuseMult = 0.2
        specularMult = 1.0
        whiteColor = np.array([1, 1, 1])
        whitePhong = PhongProperties(whiteColor, ambientMult, diffuseMult, specularMult)

        shinyness = 2.0
        reflection = 0.25

        frontRightCuboid = Surface("frontRightCuboid",frontRightCuboidPlane, whitePhong, shinyness, reflection)
        frontLeftCuboid = Surface("frontLeftCuboid",frontLeftCuboidPlane, whitePhong, shinyness, reflection)
        backLeftCuboid = Surface("backLeftCuboid",backLeftCuboidPlane, whitePhong, shinyness, reflection)
        backRightCuboid = Surface("backRightCuboid",backRightCuboidPlane, whitePhong, shinyness, reflection)
        #bottomCuboid = Surface("bottomCuboid",bottomCuboidPlane, whitePhong, shinyness, reflection)
        topCuboid = Surface("topCuboid",topCuboidPlane, whitePhong, shinyness, reflection)

        cuboid = Surfaces(frontRightCuboid, frontLeftCuboid, backLeftCuboid, backRightCuboid, topCuboid)
        return cuboid

    def _init_cube(self):
        frontCubePlane = Plane(np.array([-0.75, 0.75, -1]), np.array([0, -0.5, 0]), np.array([0.5, 0, 0]))
        leftCubePlane = Plane(np.array([-0.75, 0.75, -1]), np.array([0, -0.5, 0]), np.array([0, 0, -0.5]))
        #bottomCubePlane = Plane(np.array([-0.75, 0.75, -1.5]), np.array([0.5, 0, 0]), np.array([0, 0, -0.5]))
        backCubePlane = Plane(np.array([-0.75, 0.75, -1.5]), np.array([0.5, 0, 0]), np.array([0, -0.5, 0]))
        rightCubePlane = Plane(np.array([-0.25, 0.25, -1.5]), np.array([0, 0, 0.5]), np.array([0, 0.5, 0]))
        topCubePlane = Plane(np.array([-0.2501, 0.25, -1.5]), np.array([0, 0, 0.5]), np.array([-0.5001, 0, 0]))

        ambientMult = 0.15
        diffuseMult = 0.2
        specularMult = 1.0
        yellowColor = np.array([1, 1, 0])
        yellowPhong = PhongProperties(yellowColor, ambientMult, diffuseMult, specularMult)

        shinyness = 2.0
        reflection = 0.1

        frontCube = Surface("frontCube",frontCubePlane, yellowPhong, shinyness, reflection)
        leftCube = Surface("leftCube",leftCubePlane, yellowPhong, shinyness, reflection)
        #bottomCube = Surface("bottomCube",bottomCubePlane, yellowPhong, shinyness, reflection)
        backCube = Surface("backCube",backCubePlane, yellowPhong, shinyness, reflection)
        rightCube = Surface("rightCube",rightCubePlane, yellowPhong, shinyness, reflection)
        topCube = Surface("topCube",topCubePlane, yellowPhong, shinyness, reflection)

        cube = Surfaces(frontCube, leftCube, backCube, rightCube, topCube)
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
        supVec = np.array([0.1, -0.7499999, -1.6])
        dirVec1 = np.array([-0.2, 0, 0])
        dirVec2 = np.array([0, 0, -0.2])
        plane = Plane(supVec, dirVec1, dirVec2)
        phongProp = PhongProperties(np.array([1, 1, 1]), 1, 1, 0.6)
        lightSource = LightSource(self.allSurfaces, plane, phongProp)
        return lightSource

    def __init__(self, heightpx, widthpx, max_depth=3, randomShadowRays = 4, systematicShadowRayRoot = 2, liveDisplay=True):
        self.camera = Camera(heightpx, widthpx)
        self.allSurfaces = self._initAllSurfaces()
        self.lightSource = self._initLightSource()
        self._picturecap = np.zeros((heightpx, widthpx, 3))
        self._max_depth = max_depth
        self._rSR = randomShadowRays
        self._sSRR = systematicShadowRayRoot
        if liveDisplay:
            self.picDisplay = PictureDisplay("render")

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
            illumination += collisionSurf.phong.ambient * self.lightSource.getAmbient()
            if shadedPart != 1:
                lightDiffuse, lightSpecular = self.lightSource.getIllumination(surfNorm, surfPos,
                    self.camera.cameraCords, collisionSurf.shinyness)
                illumination += collisionSurf.phong.diffuse * lightDiffuse
                
                illumination += collisionSurf.phong.specular * lightSpecular
                
                illumination *= (1 - shadedPart)
                color += reflection * illumination
            reflection *= collisionSurf.reflection
            if reflection == 0:
                break
            ray.reflect(surfNorm, surfShiftPos)
        self._picturecap[heightPx, widthPx] = np.clip(color, 0, 1)

    def display(self):
        if "picDisplay" in self.__dict__:
            self.picDisplay.draw(self._picturecap)

    def printImage(self, name: str):
        plt.imsave("%s.png"%name, self._picturecap)

