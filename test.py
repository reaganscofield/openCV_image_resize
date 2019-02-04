import cv2 as cv
import random
import numpy as NP


img = cv.imread('iss2_lu.png')
print('image shape is : {}'.format(img.shape))
print('imgae ndim is : {}'.format(img.ndim))

print(type(img))

genInt = random.randint(1,3445565632)

print(img.shape)

default_h = 3264
default_w = 4896

w = img.shape[0]
h = img.shape[1]

print('width: {}'.format(w))
print('height: {}'.format(h))


resizeImg = cv.resize(img, (default_w, default_h))
print('image shape after resize {}'.format(resizeImg.shape))
#print('resize value :::::', resizeImg)
print(type(resizeImg))





numpyValue =  NP.fromstring(img, dtype=NP.uint8) #NP.asarray(bytearray(resizeImg), dtype="uint8")
print(type(numpyValue), "type of numpyValue")
print(numpyValue, "numpyValue vlaue")


getValue = cv.imdecode(
    numpyValue, 1  #cv.IMREAD_COLOR
)
print(type(getValue))
print(getValue)



name = "{}.jpg".format(genInt)
print("name before write: ", name)

storeImg = cv.imwrite(name,  resizeImg)   #'{}.jpg'.format(genInt),
print(storeImg)
print(type(storeImg))

print("name after write: ", resizeImg)



cv.imshow('0', resizeImg)
cv.waitKey(9000)  #pass 0 for manual close and mil second for auto close
cv.destroyAllWindows()

















# width = input("Enter width: ")
# height = input("Enter Height: ")
# convertIntWidth = int(width)
# convertIntHeight = int(height)

# def square(w, y):
#     results = convertIntHeight + convertIntHeight
#     print(results)

# #call function
# square(convertIntHeight, convertIntHeight)







# from tkinter import *
# window=Tk()

# def from_kg():
#     width  = int(w_value.get()) #convert value to int
#     heigh = 10  #auto height you can do manual by getting it value
#     results = width + heigh
#     print(results) # printing the results
#     t1.insert(END,results) # output results in the screen

# w_value = StringVar() 
# e2=Entry(window,textvariable = w_value)
# e2.grid(row=0, column=1)

# b1=Button(window,text="Submit",command=from_kg)  #when button click its call the function   from_keg
# b1.grid(row=0,column=2)

# t1=Text(window,height=1,width=20,)
# t1.grid(row=1,column=0)
 
# window.mainloop()