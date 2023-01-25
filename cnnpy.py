import numpy as np 
import cv2
import os 
import random 

print('hello')

dir = r"img"
catagories = ['bbox','fbox']

data = list()
for catagory in catagories:
    folder = os.path.join(dir,catagory)
    print(folder)
    label = catagories.index(catagory)

    for img in os.listdir(folder):
        img = os.path.join(folder,img)
        print(img)
        img_arr = cv2.imread(img)
        data.append([img_arr,label])
random.shuffle(data)

print('Data is :')

x = list()
y = list()

for features,label in data:
    x.append(features)
    y.append(label)

x = np.array(x)
y = np.array(y)

x = x/255

print(x.shape)