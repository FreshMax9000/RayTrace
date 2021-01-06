from multiprocessing import Pool
import time

import numpy as np

from ray_tracer import RayTracer


if __name__ == "__main__":
    

    lines = 90
    ratio = 16/9   
    height = int(lines)
    width = int(lines * ratio)
    rayTracer = RayTracer(height, width, max_depth=1, randomShadowRays=0, systematicShadowRayRoot=0)

    
    frameCount = 30
    for i in range (frameCount):
        timeStart = time.time()
        rayTracer.spaceObjects.complexDict["cube"].rotate(np.array([0.0, (np.pi / 2)*((1 / frameCount)), 0.0]))
        #rayTracer.spaceObjects.complexDict["cube"].rotate(np.array([0.0, np.pi / 4, 0.0]))
        

        rayTracer.renderPicture()
            
            
        rayTracer.printImage(f"images/animation1/{i}")
        print("---Finished---")
        print("It took %.3fs"%(time.time() - timeStart))
        
