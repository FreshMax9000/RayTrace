import numpy as np

from ray import Ray

class Plane:
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
