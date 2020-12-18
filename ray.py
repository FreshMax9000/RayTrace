"""This module contains the class Ray, which represents a raytracing ray.
"""
import numpy as np


class Ray:
    """Represents a ray for raytracing.
    """

    def __init__(self, origin: np.ndarray, direction: np.ndarray):
        """Constructor method
        """
        self.origin = origin
        self.normDirection = direction

    @property
    def normDirection(self):
        """Getter for normDirection
        """
        return self._normDirection

    @normDirection.setter
    def normDirection(self, new_dir: np.ndarray):
        """Setter for normDirection
        """
        self._normDirection = Ray.normalizeVector(new_dir)

    @staticmethod
    def normalizeVector(vector: np.ndarray):
        """Returns a normalized vector
        """
        return vector / np.linalg.norm(vector)
