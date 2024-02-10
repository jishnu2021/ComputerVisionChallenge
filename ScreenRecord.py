import cv2
import pyautogui as p
import numpy as np

# Get screen resolution
rs = p.size()

# Get filename and path from user
fn = input("Please enter the file name and path (e.g., C:\\path\\to\\file.mp4): ")

# Fix the frame rate
fps = 20.0

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter(fn, fourcc, fps, rs)

print('Recording started...')

# Create recording window
cv2.namedWindow("Live recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live recording", (600, 500))

while True:
    try:
        # Capture screenshot
        img = p.screenshot()

        # Convert screenshot to numpy array
        f = np.array(img)

        # Convert color space
        f = cv2.cvtColor(f, cv2.COLOR_BGR2BGRA)

        # Write the frame
        out.write(f)

        # Display the live recording
        cv2.imshow("Live recording", f)

        # Check for 'q' key to quit
        k = cv2.waitKey(1) & 0xff
        if k == ord('q'):
            break
    except Exception as e:
        print(f"Error occurred: {e}")
        break

# Release VideoWriter and destroy windows
out.release()
cv2.destroyAllWindows()
