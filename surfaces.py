"""This moule contains the class Surfaces
"""
import numpy as np

class Surfaces:

    def __init__(self, *surfacetupel):
        """Constructor method
        """
        self.__sflist = list(surfacetupel)        
    
    @property
    def sflist(self):
        #Getter for supVec
        
        return self.__sflist

    def checkSingleObject(self, surface, ray):
        coeffMatrix = np.transpose([surface.plane.dirVec1,surface.plane.dirVec2, np.zeros(3) - ray.normDirection])
        resultMatrix = ray.origin - surface.plane.supVec
        try:                      #Gleichungssystem wird versucht zu lösem
            varMatrix = np.linalg.solve(coeffMatrix,resultMatrix)
        except:                   #Wenn nicht lösbar --> kein Schnittpunkt bzw. parrallel, nächste Fläche wird geprüft -->break
            return None, np.inf
        
        if varMatrix[0] >= -1.0e-8 and varMatrix[0] < 0.0:
            varMatrix[0] = 0.0
        if varMatrix[1] >= -1.0e-8 and varMatrix[1] < 0.0:
            varMatrix[1] = 0.0

        if varMatrix[0] > 1 or varMatrix[0] < 0 or varMatrix[1] > 1 or varMatrix[1] < 0 or varMatrix[2] <= 0:
            return None, np.inf
        return np.array([surface, varMatrix[2]])
        """
        if varMatrix[2] < smallestDistance:
            smallestDistance = varMatrix[2]
            associatedSurface = surface
            associatedVarMatrix = varMatrix
        elif varMatrix[2] == smallestDistance:
            
            if self.checkIfNewSurfCloser(self.getNearPoint(associatedVarMatrix,associatedSurface),self.getNearPoint(varMatrix,surface), ray.origin):
                smallestDistance = varMatrix[2]
                associatedSurface = surface
                associatedVarMatrix = varMatrix
        """

    def getCollisionObject(self, ray):
        #Initialiesieren der Matrixen für die  linalg.solve Funktion
        #Werden initialiesiert, sodass sie in for-Schleife Stück für Stück gesetzt werden können
        #Alle mit float, da sobald ein Wert in array --> alle float, generell keine häufigen Speicherzuweisungen durch diesen Stil
        
        #smallestDistance = np.inf
        #associatedSurface = None
        surfaceDistanceArray = np.array(list(map(self.checkSingleObject, self.__sflist, [ray]*len(self.__sflist))))
            
        minVal = surfaceDistanceArray.min(where=[False, True], initial = np.inf) 
        minimums = np.where(surfaceDistanceArray[:, 1] == minVal)
        r_val = surfaceDistanceArray[minimums[0]][0]
        return r_val
        #return (associatedSurface, smallestDistance)

    def getNearPoint(self,varMatrix, surface):
        if varMatrix[0] == 0:
            xVek = 0.01
        else:
            xVek = varMatrix[0] * 0.9
        if varMatrix[1] == 0:
            yVek = 0.01
        else:
            yVek = varMatrix[1] * 0.9
        returnVek = np.array([0.0,0.0,0.0])
        for iter in range(3):
            returnVek[iter] = surface.plane.supVec[iter]+ surface.plane.dirVec1[iter]*xVek+surface.plane.dirVec2[iter]*yVek
        return returnVek

    def checkIfNewSurfCloser(self,oldSurfPoint, newSurfPoint,origin):
        oldCombVek = origin - oldSurfPoint
        newCombVek = origin - newSurfPoint
        oldLength = np.sqrt(np.square(oldCombVek[0])+np.square(oldCombVek[1])+np.square(oldCombVek[2]))
        newLength = np.sqrt(np.square(newCombVek[0])+np.square(newCombVek[1])+np.square(newCombVek[2]))

        if newLength < oldLength:
            return True
        elif newLength > oldLength:
            return False
        

        
    
