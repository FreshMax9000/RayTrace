import numpy as np
import matplotlib.pyplot as plt

from camera import Camera
from surface import Surface
from surfaces import Surfaces
from ray import Ray

screenHeight = 200
screenWidth = 300

camera = Camera(screenHeight, screenWidth) # height, width

# max_depth = 5

# room
leftWall = Surface(np.array([1.25, -0.75, 0]), np.array([0, 1.5, 0]), np.array([0, 0, 2.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
rightWall = Surface(np.array([-1.25, -0.75, 0]), np.array([0, 1.5, 0]), np.array([0, 0, 2.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
bottomWall = Surface(np.array([1.25, -0.75, 0]), np.array([0, 0, 3]), np.array([2.5, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
topWall = Surface(np.array([1.25, 0.75, 0]), np.array([2.5, 0, 0]), np.array([0, 0, 2.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
backWall = Surface(np.array([1.25, -0.75, 2.5]), np.array([-2.5, 0, 0]), np.array([0, 1.5, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)

room = Surfaces(leftWall, rightWall, bottomWall, topWall, backWall)

# cuboid
frontRighttCuboid = Surface(np.array([-0.6, -0.75, 0.5]), np.array([0, 1, 0]), np.array([-0.25, 0, 0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
frontLeftCuboid = Surface(np.array([-0.6, -0.75, 0.5]), np.array([0, 1, 0]), np.array([0.25, 0, 0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
backLeftCuboid = Surface(np.array([-0.6, -0.75, 1]), np.array([0, 1, 0]), np.array([0.25, 0, -0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
backRightCuboid = Surface(np.array([-0.6, -0.75, 1]), np.array([0, 1, 0]), np.array([-0.25, 0, -0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
bottomCuboid = Surface(np.array([-0.6, -0.75, 0.5]), np.array([-0.25, 0, 0.25]), np.array([0.25, 0, 0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
topCuboid = Surface(np.array([-0.6, 0.25, 0.5]), np.array([-0.25, 0, 0.25]), np.array([0.25, 0, 0.25]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)

cuboid = Surfaces(frontRighttCuboid, frontLeftCuboid, backLeftCuboid, backRightCuboid, bottomCuboid, topCuboid)

# cube
frontCube = Surface(np.array([0.75, -0.75, 0.5]), np.array([0, 0.5, 0]), np.array([-0.5, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
leftCube = Surface(np.array([0.75, -0.75, 0.5]), np.array([0, 0.5, 0]), np.array([0, 0, 0.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
bottomCube = Surface(np.array([0.75, -0.75, 0.5]), np.array([-0.5, 0, 0]), np.array([0, 0, 0.5]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
backCube = Surface(np.array([0.25, -0.25, 1]), np.array([0.5, 0, 0]), np.array([0, -0.5, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
rightCube = Surface(np.array([0.25, -0.25, 1]), np.array([0, 0, -0.5]), np.array([0, -0.5, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)
topCube = Surface(np.array([0.25, -0.25, 1]), np.array([0, 0, -0.5]), np.array([0.5, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), 1, 1)

cube = Surfaces(frontCube, leftCube, bottomCube, backCube, rightCube, topCube)

allSurfacesList = room.sflist
allSurfacesList.extend(cuboid.sflist)
allSurfacesList.extend(cube.sflist)

testRay = Ray(origin= np.array([0,0,-1]),direction=np.array([0,0,1]))
testval = room.getCollisionObject(testRay)
#Lichtquelle initialisieren

image = np.zeros((screenHeight, screenWidth, 3))


for  x in  range(0,screenWidth):
    for y in  range(0,screenHeight):
        startray = camera.calculateRay(x,y)


plt.imsave('image.png', image)