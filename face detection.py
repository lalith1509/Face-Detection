import cv2
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img = cv2.VideoCapture("school.jpg")
result,img = imp_img.read()
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = detect.detectMultiScale(grayscale,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(122,234,432),2)
cv2.imshow("ELON IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()