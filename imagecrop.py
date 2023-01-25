import cv2
import numpy as np 

ind = 1
while ind <= 2:
    img = cv2.imread("img/test"+str(ind)+".jpg")
    img = cv2.resize(img,(625,810))
    print(img.shape)

    data = list()
    ini = 90
    crop_img = img[100:125,30:62]
    #plt.imshow(crop_img)

    for i in range(5):
        for j in range(4):
            crop_img = img[ini:ini+25,20:80]
            ini = ini+22
            pt = 'img/testData/'+str(ind)+'ci '+str(i)+' '+str(j)+'.jpg'
            cv2.imwrite(pt, crop_img)
            print('success : ',pt)
        ini = ini + 20
    ind = ind + 1

