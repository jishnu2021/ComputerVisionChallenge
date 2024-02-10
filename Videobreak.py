import cv2

vidcap = cv2.VideoCapture("bird.mp4")
ret, image = vidcap.read()
count = 0

while True:
    if ret == True:
        # Save frame as JPG file
        filename = r"C:\Users\PC\Desktop\Computer Vision\frames\image%d.jpg" % count
        try:
            cv2.imwrite(filename, image)
            print(f"Saved image {filename}")
        except Exception as e:
            print(f"Error saving image {filename}: {e}")
        
        # Resize the image
        resized_image = cv2.resize(image, (600, 600))
        
        # Display the resized image
        cv2.imshow("res", resized_image)

        # Move to the next frame
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 100))
        ret, image = vidcap.read()

        # Check for user input to stop or continue
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        else:
            count += 1
    else:
        print("End of the video")
        break

# Release resources
vidcap.release()
cv2.destroyAllWindows()
