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



    def getCollisionObject(self, ray):
        #Initialiesieren der Matrixen für die  linalg.solve Funktion
        #Werden initialiesiert, sodass sie in for-Schleife Stück für Stück gesetzt werden können
        #Alle mit float, da sobald ein Wert in array --> alle float, generell keine häufigen Speicherzuweisungen durch diesen Stil
        coeffMatrix = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]) 
        resultMatrix = np.array([0.0,0.0,0.0])
        smallestMatrix = np.array([0.0,0.0,50000.0])

        for surface in self.__sflist: #iterieren mit jeder Fläche, sodass jeder mögliche Schnittpunkt gefunden wird
            for i in range(3):        #Aufbauen der Koeffizientenmatrix und der Ergebnismatirx zur Anwendung der .solve Funktion
                coeffMatrix[i] = [surface.dirVec1[i],surface.dirVec2[i], 0.0 - ray.normDirection[i]]
                resultMatrix[i] = ray.origin[i] -surface.supVec[i]
            try:                      #Gleichungssystem wird versucht zu lösem
                varMatrix = np.linalg.solve(coeffMatrix,resultMatrix)
            except:                   #Wenn nicht lösbar --> kein Schnittpunkt bzw. parrallel, nächste Fläche wird geprüft -->break
                break
                                      
            if varMatrix[0] > 1 or varMatrix[0] < 0 or varMatrix[1] > 1 or varMatrix[1] < 0 or varMatrix[2] <= 0:
                break
            if varMatrix[2] < smallestMatrix[2]:
                smallestMatrix = varMatrix
                associatedSurface = surface
        if smallestMatrix[2] != 50000.0:
            for i in range(0,2):
                resultMatrix[i] = associatedSurface.supVec[i]+associatedSurface.dirVec1[i]+associatedSurface.dirVec2[i]
                return resultMatrix
        else:
            return -1
        

        
    
