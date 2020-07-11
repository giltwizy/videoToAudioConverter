###############################################
# program:	videoToAudioConverter.py
# author:	Gilton Bosco
# twitter:	@giltwizy
# date:		11 July 2020
###############################################

# importing qrcode module
import moviepy.editor

# get the file from the directory
video = moviepy.editor.VideoFileClip("myVideo.mkv")
audio = video.audio
audio.write_audiofile("converted.mp3")
