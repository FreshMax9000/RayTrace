"""This moule contains the class Surfaces
"""
import numpy as np

class Surfaces:

    def __init__(self, *surfacelist):
        """Constructor method
        """
        self.__sflist = surfacelist
        

    
    
    @property
    def sflist(self):
        #Getter for supVec
        
        return self.__sflist

    def checkIfCollisionObj(self, ray):
        #Initialiesieren der Matrixen für die  linalg.solve Funktion
        #Werden initialiesiert, sodass sie in for-Schleife Stück für Stück gesetzt werden können
        #Alle mit float, da sobald ein Wert in array --> alle float, generell keine häufigen Speicherzuweisungen durch diesen Stil
        coeffMatrix = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]) 
        resultMatrix = np.array([0.0,0.0,0.0])

        for surface in self.__sflist: #iterieren mit jeder Fläche, sodass jeder mögliche Schnittpunkt gefunden wird
            for i in range(3):        #Aufbauen der Koeffizientenmatrix und der Ergebnismatirx zur Anwendung der .solve Funktion
                coeffMatrix[i] = [surface.dirVec1[i],surface.dirVec2[i], 0.0 - ray.normDirection[i]]
                resultMatrix[i] = ray.origin[i] -surface.supVec[i]
            try:                      #Gleichungssystem wird versucht zu lösem
                varMatrix = np.linalg.solve(coeffMatrix,resultMatrix)
            except:                   #Wenn nicht lösbar --> kein Schnittpunkt bzw. parrallel, nächste Fläche wird geprüft -->break
                break
                                      #Wenn es über Fläche von geprüfter Oberfläche hinaushgeht oder Ray in falsche Richtung
                                      # --> kein Schnittpunkt --> break
            if varMatrix[0] > 1 or varMatrix[0] < 0 or varMatrix[1] > 1 or varMatrix[1] < 0 or varMatrix[2] <= 0:
                break
                                      #Wenn Funktion hier angelangt --> legitimer Schnittpunkt von Ray und irgendeiner Fläche
                                      #Eine 1 wird zurückgegeben
            return 1
                                      #Wenn alle Flächen durchlaufen und keine Schnittpunkt --> 0 zurückgeben
        return 0

        
    

        
    
