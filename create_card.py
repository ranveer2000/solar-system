import cv2

img = cv2.imread("solar-system.jpg")

sun = "Sun"
mercury = "Mercury"
venus = "Venus"
earth = "Earth"
mars = "Mars"
jupiter = "Jupiter"
saturn = "Saturn"
uranus = "Uranus"
neptune = "Neptune"

cv2.putText(img,  
           sun,
           (100,50),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,225)
           )

cv2.putText(img,  
           mercury,
           (125,250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(225,225,225)
           )

cv2.putText(img,  
           venus,
           (190,175),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(225,225,225)
           )
cv2.putText(img,  
           earth,
           (290,260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(225,225,225)
           )

cv2.putText(img,  
           mars,
           (390,175),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(225,225,225)
           )

cv2.putText(img,  
           jupiter,
           (550,400),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(225,225,225)
           )

cv2.putText(img,  
           saturn,
           (750,120),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(225,225,225)
           )

cv2.putText(img,  
           uranus,
           (975,300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(225,225,225)
           )

cv2.putText(img,  
           uranus,
           (1120,150),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(225,225,225)
           )

cv2.imshow("output",img)

cv2.waitKey(0)
