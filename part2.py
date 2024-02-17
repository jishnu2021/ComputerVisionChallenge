import cv2

cam = "http://192.168.0.4:8080/video"
cap = cv2.VideoCapture(cam)

if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("result.mp4", fourcc, 30.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (600, 600))
        cv2.imshow('Colorframe', frame)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
output.release()
cv2.destroyAllWindows()
