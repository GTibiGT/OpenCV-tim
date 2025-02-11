import cv2, random
#BGR instead of rgb
#venom.png is (354, 652, 4)

img = cv2.imread('venom.png', -1)

tag = img[100:200, 100:200]
img[200:300, 200:300] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()