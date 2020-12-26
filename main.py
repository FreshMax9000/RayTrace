import matplotlib.pyplot as plt

from ray_tracer import RayTracer
from timestopper import TimeStopper

if __name__ == "__main__":
    

    lines = 180
    ratio = 16/9   
    height = int(lines)
    width = int(lines * ratio)
    rayTracer = RayTracer(height, width, max_depth=3, randomShadowRays=0, systematicShadowRayRoot=2, liveDisplay=False)

    timerkek = TimeStopper()

    for height_px in range(height):
        for width_px in range(width):
            rayTracer.traceRays(height_px, width_px)
        print("%d / %d . %s"%(height_px, height,timerkek.getPassedTimeString(height_px,height)))
        rayTracer.display()
            
        
        
        
    rayTracer.printImage("images/test_image")
    print("---Finished---")
    plt.show()
    #print("The render took %fs\n"%(time.time() - startTime))
