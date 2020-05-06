#ffmpeg implementation of sbs

command = 'ffmpeg -i input1.mp4 -i input2.mp4 \ -filter_complex \ "[0:v]pad=iw*2:ih[int]; \ [int][1:v]overlay=W/2:0[vid]" \ -map "[vid]" \ -c:v libx264 -crf 23 \ output.mp4'
.\ffmpeg -i input1.mp4 -i input2.mp4 -filter_complex "[0:v]pad=iw*2:ih[int]; [int][1:v]overlay=W/#2:0[vid]" -map "[vid]" -c:v libx264 -crf 23 output_ffmpeg.mp4