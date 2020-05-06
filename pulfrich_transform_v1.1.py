import numpy as np
import cv2


#create video object
cap = cv2.VideoCapture('iron_man_cropped.mp4')

#calculate millisecods per frame and stretch_ratio (<1 means video was rendered slowed down from original)
fps = cap.get(cv2.CAP_PROP_FPS)
#fps = 25
mspf = 1/fps*1000
int_mspf = round(mspf)
#mspf = round((1000/fps))
#render_fps = 1/mspf*1000
#stretch_ratio = fps/render_fps
print(int_mspf)



#get frame height and width
ret, frame = cap.read()
fheight = frame.shape[0]
fwidth = frame.shape[1]

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('speed_test2.avi',fourcc, 25.0, (fwidth*2,fheight))

#set starting frame to second frame
#cap.set(cv2.CAP_PROP_POS_FRAMES, 1)


while(cap.isOpened()):
    prev_frame = frame[:]
    cap.read()
    ret, frame = cap.read()
    
    if ret==True:
        
        #stretch right frame only
        #resized_frame = cv2.resize(frame, (fwidth+500, fheight), interpolation = cv2.INTER_AREA)
                
        # concat and write the frame
        sbs = np.concatenate((frame, prev_frame), axis = 1)
        out.write(sbs)

        cv2.imshow('frame', sbs)
        if cv2.waitKey(int_mspf) & 0xFF == ord('q'):
            break
    else:
        break
      
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
