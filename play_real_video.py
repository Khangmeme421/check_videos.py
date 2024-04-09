import os
from moviepy.editor import VideoFileClip
def play_video(file_path):
    try:
        video_clip = VideoFileClip(file_path)
        video_clip.preview()
        video_clip.close()
    except KeyboardInterrupt:
        video_clip.close()
def callback(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    video_file_path = os.path.join(script_dir,"videos" ,file_name)
    play_video(video_file_path)
