import cv2
import numpy as np

count = 0

def rust_detect_frame(frame):
    global count
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 70, 70])
    upper_red = np.array([20, 200, 150])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
    
    lower_red = np.array([170, 70, 70])
    upper_red = np.array([180, 200, 150])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    
    mask = mask0 + mask1
    
    output_img = cv2.bitwise_and(frame, frame, mask=mask)
    
    print("\n\n\n Number of pixels depicting rust \n >> %d" % (np.sum(mask) / 255))
    
    frame_with_red = frame.copy()
    frame_with_red[mask == 255] = [0, 0, 255]

    return frame_with_red

video_path = 'Videos/Bridge Construction Inspection_simple_compose.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

output_video_path = 'output_video_with_red_highlight.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    count += 1
    processed_frame = rust_detect_frame(frame)
    
    out.write(processed_frame)
    
    cv2.imshow('Rust Detection', processed_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
