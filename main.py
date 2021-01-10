import matplotlib.pyplot as plt

from ray_tracer import RayTracer
from timestopper import TimeStopper

if __name__ == "__main__":
    

    lines = 200      #Height of picture
    ratio = 16/9    #Ratio of pic, width will be calculated 
    height = int(lines)
    width = int(lines * ratio)
    rayTracer = RayTracer(height, width, max_depth=4, randomShadowRays=0, systematicShadowRayRoot=2, liveDisplay=True)
                #max_depth, max number of a rays per pixel, randomShadow donot look good, systematicShadow details of shadows, live display try it 
    timerkek = TimeStopper()


 
    for height_px in range(height):
        for width_px in range(width):
            rayTracer.traceRays(height_px, width_px)
        print("%d / %d . %s"%(height_px, height,timerkek.getPassedTimeString(height_px,height)))
        rayTracer.display()
    print("%d / %d . %s"%(height_px, height,timerkek.getPassedTimeString(height,height)))
        
        
    rayTracer.printImage("images/test_image")
    print("---Finished---")
    plt.show()
    #print("The render took %fs\n"%(time.time() - startTime))
