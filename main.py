
from ray_tracer import RayTracer
from timestopper import TimeStopper

if __name__ == "__main__":
    timerkek = TimeStopper()

    lines = 300
    ratio = 4/3  
    height = int(lines)
    width = int(lines * ratio)
    rayTracer = RayTracer(height, width, max_depth=4, randomShadowRays=0, systematicShadowRayRoot=1)


    #rayTracer.traceRays(479, 454)
    
    for height_px in range(height):
        for width_px in range(width):
            rayTracer.traceRays(height_px, width_px)
        print("%d / %d . %s"%(height_px, height,timerkek.getPassedTimeString(height_px,height)))
    
    
    rayTracer.printImage("images/test_image")
    print("---Finished---")
    #print("The render took %fs\n"%(time.time() - startTime))
