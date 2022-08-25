import cv2
img=cv2.imread('C:/Users/Sakshi/Desktop/python/pro104/images/PRO-104-Project-Image-main/solar-system.jpg')

cv2.putText(img, 'Sun', (60, 90), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=3, color=(0,0,255) ) 
cv2.putText(img, 'Mercury', (100, 190), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(255,255,255) ) 
cv2.putText(img, 'Venus', (190, 260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(255,255,255) ) 
cv2.putText(img, 'Earth', (280, 260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(255,255,255) ) 
cv2.putText(img, 'Mars', (380, 260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(255,255,255) ) 
cv2.putText(img, 'Jupiter', (470, 100), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(255,255,255) ) 
cv2.putText(img, 'Saturn', (760, 100), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(255,255,255) ) 
cv2.putText(img, 'Uranus', (960, 100), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(255,255,255) ) 
cv2.putText(img, 'Neptune', (1100, 100), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(255,255,255) ) 
cv2.imwrite('solar_system_with_name.jpg',img)

cv2.imshow('output',img)
cv2.waitKey(0)