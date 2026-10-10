import numpy as np
import mediapipe as mp
import cv2 
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import Hand_traking



#mpDraw = mp.solutions.drawing_utils
camera = cv2.VideoCapture(0)
##base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
#options = vision.HandLandmarkerOptions(base_options=base_options,num_hands=2)
#detector = vision.HandLandmarker.create_from_options(options)##
newtimeframe=0
previoustimeframe=0

while True:
    work,frame = camera.read()
    
    #frame_t = cv2.resize(frame,(244(width),244(height))) used to resize my window
    if (work== False):
        print("No Camera Found")
        break
    
    #frame_flip = cv2.flip(frame,1)#flips the frame horizontally 
    
    Hand_traking.frame_collector(frame)
    
    #for hand detection
    #frameRgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)#change if frame to frame_flip we need to flip 
    #mp_image = mp.Image(image_format=mp.ImageFormat.SRGB,data=frameRgb) 
    #detection_result = detector.detect(mp_image)
    #if detection_result.hand_landmarks :
     #   for hand_landmarks in detection_result.hand_landmarks:
      #   Drawhand.draw_hand(frame,hand_landmarks)#change if frame to frame_flip we need to flip 
     
    newtimeframe= time.time()
    fps=1/(newtimeframe-previoustimeframe)
    previoustimeframe= newtimeframe
    fps=int(fps)
    cv2.putText(frame,str(fps),(6,30),cv2.FONT_ITALIC,1,(100,255,0),1)
    win_name="Camera"
    cv2.imshow(win_name,frame)#change if frame to frame_flip we need to flip 
    key = cv2.waitKey(1)
    cam_close= cv2.getWindowProperty(win_name,cv2.WND_PROP_VISIBLE) < 1 
    
    if key == ord('q') or cam_close:
     print("Exit")
     break
    
       
camera.release()
cv2.destroyAllWindows()