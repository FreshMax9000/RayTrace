from multiprocessing import Pool
import time

import matplotlib.pyplot as plt
import numpy as np

from ray_tracer import RayTracer
from timestopper import TimeStopper


def calcLine(height_px, width, rayTracer):
    rayTracer._picturecap[height_px] = np.array(list(map(rayTracer.traceRays, [height_px]*width, list(range(width)))))
    print("%d / %d"%(height_px, height))
    return rayTracer._picturecap[height_px]

if __name__ == "__main__":
    

    lines = 480
    ratio = 16/9   
    height = int(lines)
    width = int(lines * ratio)
    rayTracer = RayTracer(height, width, max_depth=4, randomShadowRays=0, systematicShadowRayRoot=2, liveDisplay=False)

    #timerkek = TimeStopper()

    

    #rayTracer.traceRays(479, 454)
    argList = list(range(height))
    argList = [(line, width, rayTracer) for line in argList]
    #[width] * height, [rayTracer] * height, [timerkek] * height
    timeStart = time.time()
    with Pool(4) as p:
        rayTracer._picturecap = np.array(list(p.starmap(calcLine, argList)))

        
        
    rayTracer.printImage("W4multitest480sr2")
    print("---Finished---")
    print("It took %.3fs"%(time.time() - timeStart))
    plt.show()
    #print("The render took %fs\n"%(time.time() - startTime))
