import numpy as np
import cv2 
import Hand_traking
import save_file

video = cv2.VideoCapture('D:\\Academic Downloads\\WLASL_100 Dataset\\WLASL_100\\train\\accident\\00623.mp4')

video_data=[]

while True:
    work,frame = video.read()
    if (work== False):
        print("video ended")
        break
    frame=cv2.resize(frame,(700,500))


    detection_result=Hand_traking.frame_collector(frame)
    if detection_result:
        video_data.append(detection_result)

    #print(len(video_data))
 
    win_name="Video"
    cv2.imshow(win_name,frame)
    key = cv2.waitKey(1)
    cam_close= cv2.getWindowProperty(win_name,cv2.WND_PROP_VISIBLE) < 1 
    
    if key == ord('q') or cam_close:
     print("Exit")
     break
    
print("Total frames in video:", int(video.get(cv2.CAP_PROP_FRAME_COUNT)))       
video.release()
cv2.destroyAllWindows()

save_file.save_data(video_data)
