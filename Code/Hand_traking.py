import cv2 
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

Hand_Marks = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

def draw_hand(frame,hand_landmarks):
    height,width,_=frame.shape

    landmarks_px=[
        (int(lm.x*width),int(lm.y*height))
        for lm in hand_landmarks
    ]

    for start,end in Hand_Marks:
        cv2.line(frame,landmarks_px[start],landmarks_px[end],(0,255,0),2)

    for pt in landmarks_px:
        cv2.circle(frame,pt,5,(0,0,225),cv2.FILLED)
        

def frame_collector (frame_collected):
    frame = frame_collected
    frameRgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB,data=frameRgb)
    detection_result = detector.detect(mp_image)
    if detection_result.hand_landmarks :
        for hand_landmarks in detection_result.hand_landmarks:
         draw_hand(frame,hand_landmarks)