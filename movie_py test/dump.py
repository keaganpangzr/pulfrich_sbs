from moviepy.editor import *
from moviepy.config import change_settings
change_settings({"FFMPEG_BINARY": "ffmpeg"})



user_clip_1 = VideoFileClip('input.mp4')


# Adding our audio track
wav_file = "audio.m4a"
audio = AudioFileClip(wav_file)
final_clip = user_clip_1.set_audio(audio)

#final_clip.fps=30

# Writing the file to disk
final_clip.write_videofile('write.mp4', audio_codec='libfdk_aac')