import numpy as np

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
