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

    timeStart = time.time()

    rayTracer.renderPicture()
        
        
    rayTracer.printImage("images/test")
    print("---Finished---")
    print("It took %.3fs"%(time.time() - timeStart))
