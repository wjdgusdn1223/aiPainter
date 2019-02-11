import cv2 as cv
import numpy as np
import os
import math

class CanvasPainter:
    def __init__(self, height, width, pixel):
        self.canvas = np.full((height*pixel, width*pixel, 3), 255, np.uint8)

    def painting(self, pName, height, width, pixel, geneSave, gMax, pTerm):
        cX = cY = int(round((pixel-1)/2))
        
        try:
            if not(os.path.isdir("Result_" + pName)):
                os.makedirs(os.path.join("Result_" + pName))
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create directory!!")
                raise
            
        for n in range(math.ceil(gMax/pTerm) + 1):
            for y in range(height):
                for x in range(width):
                    color = tuple([int(geneSave[n, y, x]) for z in range(3)])
                    
                    self.canvas = \
                        cv.circle(self.canvas, (cX, cY), int(round((pixel+1)/2)), color, -1)
                    
                    cX += pixel
                else:
                    cX = int(round((pixel-1)/2))
                    cY += pixel
            else:
                cY = int(round((pixel-1)/2))
                if (n * pTerm) <= gMax:
                    cv.imwrite("Result_" + pName + "/" + str(n*pTerm) + "_gene.jpg", self.canvas)
                else:
                    cv.imwrite("Result_" + pName + "/" + str(gMax) + "_gene.jpg", self.canvas)
                self.canvas = cv.rectangle(self.canvas, (0,0), (width*pixel, height*pixel), (255,255,255), -1)

        #cv.imwrite(str(gNum) + '.jpg', self.canvas)
        #cv.namedWindow('img', cv.WINDOW_NORMAL)
        #cv.imshow('img', self.canvas)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
