import time

from ray_tracer import RayTracer

if __name__ == "__main__":
    startTime = time.time()

    height = 200
    width = 300
    rayTracer = RayTracer(height, width)

    for height_px in range(height):
        for width_px in range(width):
            rayTracer.traceRays(height_px, width_px)
        print("%d / %d"%(height_px, height))
    
    rayTracer.printImage("images/test_image")
    print("---Finished---")
    print("The render took %fs\n"%(time.time() - startTime))
