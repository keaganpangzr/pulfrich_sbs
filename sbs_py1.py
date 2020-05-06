from moviepy.editor import VideoFileClip, clips_array, vfx
#remove "-an" from VideoFileClip.py
#add comment # to destructor on line 93 of AudioFileClip.py
#BRANCH

video_clip = VideoFileClip("input.mp4", audio=True)
new_clip = VideoFileClip("input.mp4", audio=False)

#first_frame_marker = (1/video_clip.fps)
first_frame_marker = 0

#find duration up to timestamp of last frame
#last_frame_marker = (video_clip.duration - 1/video_clip.fps)

new_clip = new_clip.subclip(first_frame_marker)

final_clip = clips_array([[video_clip, new_clip],])


final_clip.write_videofile("output_benchmark.mp4", codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)


video_clip.close()
new_clip.close()
final_clip.close()