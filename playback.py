import cv2
import numpy as np


def play_video(video_path, fps, video_res, monochrome, target_path):
    v_width = int(video_res.split('*')[0])
    v_height = int(video_res.split('*')[1])
    fps = 1000/fps
    video_name = (video_path.split('/')[-1]).split('.')[0]
    cap = cv2.VideoCapture(video_path)
    #Removing background from the video
    fgbg = cv2.createBackgroundSubtractorMOG2()
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    if target_path == "":
        vpath = video_path.split(".")[:-1]
        out = cv2.VideoWriter(vpath+'_processed.mp4', fourcc,  fps , size)
    else:
        out = cv2.VideoWriter(target_path+video_name+'_processed.mp4', fourcc,  fps , size)
    while(cap.isOpened()):

        ret, frame = cap.read()
        # set the resolution 
        

        #Checking for monochrome and if not loading the original one
        if monochrome=="true":

            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
       
        #Applying the width and height as supplied
        cv2.namedWindow('frame', 0)
        cv2.resizeWindow('frame', v_width, v_height)
        fgmask = fgbg.apply(frame)
        output = cv2.cvtColor(fgmask, cv2.COLOR_BGR2RGB)
        out.write(output)
        cv2.imshow('frame',fgmask)

        #Pause functionality while using p button
        if cv2.waitKey(int(fps)) & 0xFF == ord('p'):
            cv2.waitKey(0)
            

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "drive-download-20190713T111647Z-001/video_2.mp4"
    fps = 50
    video_res = "640*480"
    monochrome = "false"
    target_path = "/Users/sufyjakate/Documents/Video_Play/"
    play_video(video_path, fps, video_res, monochrome, target_path)