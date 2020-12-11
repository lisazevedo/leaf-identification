import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

myFileList = createFileList('.')

for file in myFileList:
    src = cv.imread(file)
    scale_percent = 20

#calculate the 20 percent of original dimensions
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    # resize image
    img = cv.resize(src, dsize)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    edged=cv.Canny(gray,20,80)
    print(file)

    cv.imwrite("segmentation/"+file, edged)

