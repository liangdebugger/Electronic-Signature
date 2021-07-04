import cv2
import numpy as np

# 加载一个图像
img = cv2.imread("D:/python/8585.jpg")
rows = img.shape[0]
cols = img.shape[1]
channels = img.shape[2]
new_img=np.zeros([rows,cols,channels],dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
        b = img[i, j][0]
        g = img[i, j][1]
        r = img[i, j][2]
        if b>100:
            new_b = 255
        else:
            new_b = b
        if g > 100:
            new_g = 255
        else:
            new_g = g
        if r > 100:
            new_r = 255
        else:
            new_r = r
        new_img[i, j][0] = new_b
        new_img[i, j][1] = new_g
        new_img[i, j][2] = new_r
cv2.imshow('img', new_img)
cv2.waitKey(0)
cv2.imwrite('new_img.jpg',new_img)
