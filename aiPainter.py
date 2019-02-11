import os
import time

from picture import Picture
from generation import Generation
from canvasPainter import CanvasPainter

class AiPainter:

    def __init__(self, pName, gMax, gNum, size, pixel, pTerm):
        self.pObj = Picture(pName, size)
        self.gObj = Generation(gMax, gNum, self.pObj.height, self.pObj.width, pTerm)
        self.cObj = CanvasPainter(self.pObj.height, self.pObj.width, pixel)

        self.pName, self.gMax, self.gNum, self.size, self.pixel, self.pTerm = pName, gMax, gNum, size, pixel, pTerm

    def startPainting(self):
        start_time = time.time()
        for n in range(0, self.gMax):

            self.gObj.geneCreate(self.gNum, self.pObj.height, self.pObj.width, n) 

            self.gObj.scoreCheck(self.pObj.height, self.pObj.width, self.pObj.img, self.gNum, self.gMax, n, self.pTerm)
            
            if self.gObj.strongestGene[1] > 97:
                self.gMax = n
                print(n)
                break
        print("--- %s seconds ---" %(time.time() - start_time))

    def resultSave(self):
        self.cObj.painting(self.pName, self.pObj.height, self.pObj.width, self.pixel, self.gObj.geneSave, self.gMax, self.pTerm)


test = AiPainter("orora", 100000, 20, 200, 15, 10000)
test.startPainting()
test.resultSave()
