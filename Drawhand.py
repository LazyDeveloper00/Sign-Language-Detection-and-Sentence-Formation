import cv2

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
