
import cv2 as OpenCV
import numpy as NP
import random

getMainFile = "iss2_lu.png"            
            
img =   OpenCV.imread('iss2_lu.png')  #  OpenCV.imdecode(NP.fromstring(getMainFile.read(), NP.uint8), OpenCV.IMREAD_UNCHANGED)
default_h = 200
default_w = 200
resizeImg = OpenCV.resize(img, (default_w, default_h))

print("w & h after resize: ", resizeImg.shape)
OpenCV.imshow("The Images", resizeImg)
print(type(resizeImg))

genInt = random.randint(1,3445565632)
storeImg = OpenCV.imwrite('{}.jpg'.format(genInt),  resizeImg)
# print(type(storeImg))
# print(storeImg)

OpenCV.waitKey(0)
OpenCV.destroyAllWindows()
print(type(img))
            