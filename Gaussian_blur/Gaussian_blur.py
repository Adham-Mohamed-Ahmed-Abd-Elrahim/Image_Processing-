import cv2
img=cv2.imread(don-colreon)
window_name='Blurred'
blur=cv2.GaussianBlur(img,(0,0),5)
cv2.imshow(window_name,blur)
