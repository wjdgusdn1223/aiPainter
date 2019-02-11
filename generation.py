import cv2 as cv
import numpy as np
import random
import math

class Generation:

    def __init__(self, gMax, gNum, height, width, pTerm):
        self.genes = np.random.randint(256, size = (2, gNum, height, width), dtype = "i")
        self.geneSave = np.zeros((math.ceil(gMax/pTerm)+1, height, width), dtype = "i")
        self.geneRank = np.zeros((gNum), dtype = "i")
        self.geneScore = np.zeros((gNum), dtype = "i")

        self.sampleList = [(y, x) for y in range(height) for x in range(width)]
        self.sampleNum = int(round(height*width/2))

        self.strongestGene = tuple([0, 0])

    def geneCreate(self, gNum, height, width, n):
        if n is 0:
            pass
        else:
            for i in range(math.ceil(gNum/4)):
                rank_1 = (np.reshape(self.genes[0, self.geneRank[0]], height*width)).copy()
                rank_2 = (np.reshape(self.genes[0, self.geneRank[1]], height*width)).copy()
                x = list([random.randint(1,height*width-1) for j in range(2)])
                x.sort()
            
                tmp_1, tmp_2 = rank_1[:x[0]].copy(), rank_1[-1*((height*width)-x[1]):].copy()
                rank_1[:x[0]], rank_1[-1*((height*width)-x[1]):] = rank_2[:x[0]], rank_2[-1*((height*width)-x[1]):]
                rank_2[:x[0]], rank_2[-1*((height*width)-x[1]):] = tmp_1, tmp_2
                self.genes[1, i*2] = np.reshape(rank_1,(height, width))
                if not ((i*2+1) > math.floor((gNum-1)/2)):
                    self.genes[1, i*2+1] = np.reshape(rank_2,(height, width))
            
            
            #sample = tuple([random.sample(self.sampleList, self.sampleNum) for x in range(int(round(gNum/2)))])

            #self.genes[1, range(int(round(gNum/2)))] = self.genes[0, self.geneRank[list([x%2 for x in range(int(round(gNum/2)))])]]
            
            #for i in range(int(round(gNum/2))):
                #for j in range(self.sampleNum):
                    #self.genes[1, i, sample[i][j][0], sample[i][j][1]] = self.genes[0, (i+1)%2, sample[i][j][0], sample[i][j][1]]

            mutant = tuple([random.sample(self.sampleList, 1) for x in range(int(round(gNum/2)))])
            
            self.genes[1, range(int(round(gNum/2)), gNum)] = self.genes[1, range(int(round(gNum/2)))]
            
            for i in range(int(round(gNum/2))):
                self.genes[1, i + int(round(gNum/2)), mutant[i][0][0], mutant[i][0][1]] = random.randint(0, 255)

            self.genes[0] = self.genes[1]
            
    def scoreCheck(self, height, width, img, gNum, gMax, n, pTerm):
        imgArr = np.array([img for x in range(gNum)])
        
        diff = np.abs(img - self.genes[0])
        dSum = (diff.sum(axis = 1)).sum(axis = 1)
        
        score = ((diff <= 1).sum(axis = 1)).sum(axis = 1)*100
        score += (np.logical_and(1 < diff, diff <= 3).sum(axis = 1)).sum(axis = 1)*30
        score += (np.logical_and(3 < diff, diff <= 10).sum(axis = 1)).sum(axis = 1)*10
        score += (np.logical_and(10 < diff, diff <= 30).sum(axis = 1)).sum(axis = 1)*3
        score += (np.logical_and(30 < diff, diff <= 100).sum(axis = 1)).sum(axis = 1)*1

        self.geneScore = score
        if score.max() > self.strongestGene[0] + 10000:
            self.strongestGene = score.max(), abs((dSum[score.argmax()]/(height*width*255)*100)-100)
            print(n+1, "세대", "점수 :", self.strongestGene[0], "일치율", self.strongestGene[1], "%")

        self.geneRank = np.argsort(-1 * (self.geneScore))

        if n == (gMax-1) or self.strongestGene[1] > 97:
            self.geneSave[math.ceil(n/pTerm)] = self.genes[0, self.geneRank[0]]
        elif (n % pTerm) is 0:
            self.geneSave[int(round((n+1)/pTerm))] = self.genes[0, self.geneRank[0]]
            
            
                    
