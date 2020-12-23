import numpy as np

from ray import Ray

class Plane:
    def __init__(self, supVec: np.array, dirVec1: np.array, dirVec2: np.array):
        """Constructor method
        """
        self.supVec = supVec
        self.dirVec1 = dirVec1
        self.dirVec2 = dirVec2

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
