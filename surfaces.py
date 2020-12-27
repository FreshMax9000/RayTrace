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

    #def getCollisionObject(self, ray):
        

    def getCollisionObject(self, ray):
        #Initialiesieren der Matrixen für die  linalg.solve Funktion
        #Werden initialiesiert, sodass sie in for-Schleife Stück für Stück gesetzt werden können
        #Alle mit float, da sobald ein Wert in array --> alle float, generell keine häufigen Speicherzuweisungen durch diesen Stil
        coeffMatrix = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]) 
        resultMatrix = np.array([0.0,0.0,0.0])
        smallestDistance = 100.0

        for surface in self.__sflist: #iterieren mit jeder Fläche, sodass jeder mögliche Schnittpunkt gefunden wird
            """
            if ray.origin[2] == 1 and surface.plane.supVec[0] == - 1.25 and surface.plane.supVec[1] == 0.75 and surface.plane.supVec[2] == 0:
                continue
            """
            for i in range(3):        #Aufbauen der Koeffizientenmatrix und der Ergebnismatirx zur Anwendung der .solve Funktion
                coeffMatrix[i] = [surface.plane.dirVec1[i],surface.plane.dirVec2[i], 0.0 - ray.normDirection[i]]
                resultMatrix[i] = ray.origin[i] -surface.plane.supVec[i]
            try:                      #Gleichungssystem wird versucht zu lösem
                varMatrix = np.linalg.solve(coeffMatrix,resultMatrix)
            except:                   #Wenn nicht lösbar --> kein Schnittpunkt bzw. parrallel, nächste Fläche wird geprüft -->break
                continue
            
            if varMatrix[0] >= -1.0e-8 and varMatrix[0] < 0.0:
                varMatrix[0] = 0.0
            if varMatrix[1] >= -1.0e-8 and varMatrix[1] < 0.0:
                varMatrix[1] = 0.0

            if varMatrix[0] > 1 or varMatrix[0] < 0 or varMatrix[1] > 1 or varMatrix[1] < 0 or varMatrix[2] <= 0:
                continue
            
            if varMatrix[2] < smallestDistance:
                smallestDistance = varMatrix[2]
                associatedSurface = surface
                associatedVarMatrix = varMatrix
            elif varMatrix[2] == smallestDistance:
                
                if self.checkIfNewSurfCloser(self.getNearPoint(associatedVarMatrix,associatedSurface),self.getNearPoint(varMatrix,surface), ray.origin):
                    smallestDistance = varMatrix[2]
                    associatedSurface = surface
                    associatedVarMatrix = varMatrix
            
        if smallestDistance != 100.0:
            return (associatedSurface, smallestDistance)
        else:
            return (None, smallestDistance)

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
        

        
    
