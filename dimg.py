import cv2
img = cv2.imread('0089.jpg')
img = cv2.resize(img,(640,408))
cv2.imwrite('00_1.png',img)