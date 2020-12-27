from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np

from ray_tracer import RayTracer
from timestopper import TimeStopper


def calcLine(height_px, width, rayTracer, timerkek):
    rayTracer._picturecap[height_px] = np.array(list(map(rayTracer.traceRays, [height_px]*width, list(range(width)))))
    print("%d / %d . %s"%(height_px, height,timerkek.getPassedTimeString(height_px,height)))
    rayTracer.display()
    return rayTracer._picturecap[height_px]

if __name__ == "__main__":
    

    lines = 90
    ratio = 16/9   
    height = int(lines)
    width = int(lines * ratio)
    rayTracer = RayTracer(height, width, max_depth=4, randomShadowRays=0, systematicShadowRayRoot=2, liveDisplay=False)

    timerkek = TimeStopper()


    #rayTracer.traceRays(479, 454)
    argList = list(range(height))
    argList = [(line, width, rayTracer, timerkek) for line in argList]
    #[width] * height, [rayTracer] * height, [timerkek] * height
    with Pool(5) as p:
        rayTracer._picturecap = np.array(list(p.starmap(calcLine, argList)))

    print("%d / %d . %s"%(height, height,timerkek.getPassedTimeString(height,height)))
        
        
    rayTracer.printImage("images/test_imagemulti")
    print("---Finished---")
    plt.show()
    #print("The render took %fs\n"%(time.time() - startTime))
