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
        smallestDistance = 100.0

        for surface in self.__sflist: #iterieren mit jeder Fläche, sodass jeder mögliche Schnittpunkt gefunden wird
            for i in range(3):        #Aufbauen der Koeffizientenmatrix und der Ergebnismatirx zur Anwendung der .solve Funktion
                coeffMatrix[i] = [surface.dirVec1[i],surface.dirVec2[i], 0.0 - ray.normDirection[i]]
                resultMatrix[i] = ray.origin[i] -surface.supVec[i]
            try:                      #Gleichungssystem wird versucht zu lösem
                varMatrix = np.linalg.solve(coeffMatrix,resultMatrix)
            except:                   #Wenn nicht lösbar --> kein Schnittpunkt bzw. parrallel, nächste Fläche wird geprüft -->break
                continue
            
            if varMatrix[0] > 1 or varMatrix[0] < 0 or varMatrix[1] > 1 or varMatrix[1] < 0 or varMatrix[2] <= 0:
                continue

            if varMatrix[2] < smallestDistance:
                smallestDistance = varMatrix[2]
                associatedSurface = surface
        if smallestDistance != 100.0:
            return (associatedSurface, smallestDistance)
        else:
            return (None, 0)
        

        
    
