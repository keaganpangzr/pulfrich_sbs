import numpy as np
import cv2


#create video object
cap = cv2.VideoCapture('iron_man_cropped.mp4')

#calculate millisecods per frame and stretch_ratio (<1 means video was rendered slowed down from original)
fps = cap.get(cv2.CAP_PROP_FPS)
mspf = round((1000/fps))
render_fps = 1/mspf*1000
stretch_ratio = render_fps/fps

#get frame height and width
ret, frame = cap.read()
fheight = frame.shape[0]
fwidth = frame.shape[1]

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_frameindex.avi',fourcc, 20.0, (fwidth*2,fheight))

#set starting frame to second frame
cap.set(cv2.CAP_PROP_POS_FRAMES, 1)

while(cap.isOpened()):
    
    ret, frame = cap.read()
    
    if ret==True:
        # write the frame
        vis = np.concatenate((frame,frame), axis = 1)
        
        out.write(vis)

        cv2.imshow('frame', vis)
        if cv2.waitKey(mspf) & 0xFF == ord('q'):
            break
    else:
        break
      
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
