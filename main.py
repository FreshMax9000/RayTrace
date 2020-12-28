from multiprocessing import Pool
import time

import numpy as np

from ray_tracer import RayTracer
from timestopper import TimeStopper


def calcLine(height_px, width, rayTracer):
    rayTracer._picturecap[height_px] = np.array(list(map(rayTracer.traceRays, [height_px]*width, list(range(width)))))
    print("%d / %d"%(height_px, height))
    return rayTracer._picturecap[height_px]

if __name__ == "__main__":
    

    lines = 90
    ratio = 16/9   
    height = int(lines)
    width = int(lines * ratio)
    rayTracer = RayTracer(height, width, max_depth=4, randomShadowRays=0, systematicShadowRayRoot=2)

    timeStart = time.time()

    rayTracer.renderPicture()
        
        
    rayTracer.printImage("multiTest")
    print("---Finished---")
    print("It took %.3fs"%(time.time() - timeStart))
