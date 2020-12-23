
from ray_tracer import RayTracer
from timestopper import TimeStopper

if __name__ == "__main__":
    timerkek = TimeStopper()

    height = 300
    width = 400
    rayTracer = RayTracer(height, width, max_depth=3, randomShadowRays=4, systematicShadowRayRoot=5)

    for height_px in range(height):
        for width_px in range(width):
            rayTracer.traceRays(height_px, width_px)
        print("%d / %d . %s"%(height_px, height,timerkek.getPassedTimeString(height_px,height)))
        
    
    rayTracer.printImage("images/test_image")
    print("---Finished---")
    #print("The render took %fs\n"%(time.time() - startTime))
