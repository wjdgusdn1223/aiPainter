import cv2 as cv
import matplotlib.pyplot as plt

class Picture:

    def __init__(self, pName, size):
        self.orgImg = cv.imread(pName + ".jpg", cv.IMREAD_GRAYSCALE)
        
        self.img    = cv.imread(pName + ".jpg", cv.IMREAD_GRAYSCALE)
        self.imgResize(size)

        self.height, self.width = self.img.shape
        
    def imgResize(self, size):
        resizeX = 1

        while (self.img.shape[0] / resizeX >= size) or (self.img.shape[1] / resizeX >= size):
            resizeX += 1

        self.img = cv.resize(self.img, dsize=None, fx=(1/resizeX), fy=(1/resizeX))
        print(self.img.shape, resizeX)

        plt.figure(figsize = (10,10))
        plt.axis('off')
        plt.imshow(self.img, cmap='gray')
        plt.show()
