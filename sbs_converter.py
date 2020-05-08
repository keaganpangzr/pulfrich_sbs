from moviepy.editor import VideoFileClip, clips_array

class VideoClip:
    #file_name includes extension
    def __init__(self, file_name: str):
        self.file_name = file_name
        
    def convert(self):      
        '''Create stacked side-by-side video file with Pulfrich effect''' 
        
        left_viewport = VideoFileClip(self.file_name, audio=True)
        right_viewport = VideoFileClip(self.file_name, audio=False)
    
        first_frame_marker = (1/left_viewport.fps)
        right_viewport = right_viewport.subclip(first_frame_marker)
    
        stacked = clips_array([[left_viewport, right_viewport],])        
        stacked.write_videofile(self.file_name + '_sbs.mp4', codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)
        
        left_viewport.close()
        right_viewport.close()
            
if __name__ == '__main__':
    iron_man = VideoClip("iron_man_cropped.mp4")
    iron_man.convert()
        