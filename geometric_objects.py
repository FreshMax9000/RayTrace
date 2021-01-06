import numpy as np

from ray import Ray


class GeometricObject:

    def _rotMatrix(self, xRot, yRot, zRot):
        xRotMatrix = np.array([[1, 0, 0], [0, np.cos(xRot), np.sin(xRot)], [0, -np.sin(xRot), np.cos(xRot)]])
        yRotMatrix = np.array([[np.cos(yRot), 0, -np.sin(yRot)], [0, 1, 0], [np.sin(yRot), 0, np.cos(yRot)]])
        zRotMatrix = np.array([[np.cos(zRot), np.sin(zRot), 0], [-np.sin(zRot), np.cos(zRot), 0], [0, 0 , 1]])
        return (xRotMatrix.dot(yRotMatrix)).dot(zRotMatrix)

    def checkCollision(self, ray: Ray):
        pass

    def getNorm(self):
        pass

    def move(self, vector: np.ndarray):
        pass

    def rotate(self, origin: np.ndarray, direction: np.ndarray):
        pass


class Plane(GeometricObject):
    def __init__(self, supVec: np.array, dirVec1: np.array, dirVec2: np.array):
        """Constructor method
        """
        self.supVec = supVec
        self.dirVec1 = dirVec1
        self.dirVec2 = dirVec2
        self._trans2dTo3d = np.array([self.dirVec1, self.dirVec2])
        self._trans3dTo2d = np.linalg.pinv(self._trans2dTo3d)

    @property
    def norm(self):
        """Normal vector of surface
        """
        return Ray.normalizeVector(np.cross(self.dirVec1, self.dirVec2))

    def getPositiveNormVec(self, origin):
        """Returns the normal vector of the plane facing the point origin
        """
        distNOV = np.linalg.norm(origin - (self.supVec + self.norm))
        distAOV = np.linalg.norm(origin - (self.supVec - self.norm))
        return self.norm if distNOV < distAOV else -1 * self.norm

    def checkPointInBorders(self, point: np.ndarray):
        point2d = point.dot(self._trans3dTo2d)
        return np.all(np.logical_and(0 <= point2d,  point2d <= 1))

    def getClosestPoint(self, point: np.ndarray):
        point2d = point.dot(self._trans3dTo2d)
        closest2d = np.clip(point2d, 0, 1)
        return closest2d.dot(self._trans2dTo3d)

    def getFurthestPoint(self, point: np.ndarray):
        point2d = point.dot(self._trans3dTo2d)
        closest2d = np.clip(point2d, 0, 1)
        furthest2d = np.array([1, 1]) - closest2d
        return furthest2d.dot(self._trans2dTo3d)

    def checkCollision(self, ray: Ray):
        coeffMatrix = np.transpose([self.dirVec1,self.dirVec2, np.zeros(3) - ray.normDirection])
        resultMatrix = ray.origin - self.supVec
        try:                      #Gleichungssystem wird versucht zu lösem
            varMatrix = np.linalg.solve(coeffMatrix,resultMatrix)
        except:                   #Wenn nicht lösbar --> kein Schnittpunkt bzw. parrallel, nächste Fläche wird geprüft -->break
            return np.inf
        
        if varMatrix[0] >= -1.0e-8 and varMatrix[0] < 0.0:
            varMatrix[0] = 0.0
        if varMatrix[1] >= -1.0e-8 and varMatrix[1] < 0.0:
            varMatrix[1] = 0.0

        if varMatrix[0] > 1 or varMatrix[0] < 0 or varMatrix[1] > 1 or varMatrix[1] < 0 or varMatrix[2] <= 0:
            return np.inf
        return np.array([varMatrix[2]])

    def getNorm(self):
        return self.norm

    def move(self, vector: np.ndarray):
        self.supVec += vector

    def rotate(self, origin: np.ndarray, direction: np.ndarray):
        tempSupVec = self.supVec - origin
        tempDirVec1 = self.dirVec1 - origin + self.supVec
        tempDirVec2 = self.dirVec2 - origin + self.supVec
        rotMatrix = self._rotMatrix(direction[0], direction[1], direction[2])
        self.supVec = rotMatrix.dot(tempSupVec) + origin
        self.dirVec1 = rotMatrix.dot(tempDirVec1) + origin - self.supVec
        self.dirVec2 = rotMatrix.dot(tempDirVec2) + origin - self.supVec

