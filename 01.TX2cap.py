import cv2


#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)680, height=(int)480, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! appsink")

while True:
    _, frame = cap.read()
    cv2.imshow("00", frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

