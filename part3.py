# import cv2
# import pafy

# url="https://www.youtube.com/watch?v=wIAs97ynODo&list=PLaHodugB5x-Ddy_H951h0VHjOjfzZNCBh&index=15"
# data=pafy.new(url) #fetch the data from url
# data=data.getbest(preftype="mp4")# get best format available for download

# print(data.url) #print the url of the video file to be downloaded
# cap = cv2.VideoCapture(data)

# if not cap.isOpened():
#     print("Error: Unable to open camera.")
#     exit()

# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret:
#         frame = cv2.resize(frame, (600, 600))
#         gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('Colorframe', frame)
#         cv2.imshow('gray', gray)
#         # output.write(frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2
import pafy
import urllib

# YouTube URL
url = "https://www.youtube.com/watch?v=wIAs97ynODo&list=PLaHodugB5x-Ddy_H951h0VHjOjfzZNCBh&index=15"

# Fetch the video
video = pafy.new(url)
best = video.getbest(preftype="mp4")

# Download the video locally
filename = best.download(filepath="video.mp4")

# Open the video file with OpenCV
cap = cv2.VideoCapture(filename)

if not cap.isOpened():
    print("Error: Unable to open video file.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (600, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Colorframe', frame)
        cv2.imshow('gray', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


