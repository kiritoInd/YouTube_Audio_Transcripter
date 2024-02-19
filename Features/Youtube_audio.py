from pytube import YouTube
from moviepy.editor import *
import os

def download_youtube_audio(video_url, output_path , i ):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        
        audio_path = os.path.join(output_path, f"audio{i}.mp3")
        print(audio_path)
        if os.path.exists(audio_path):
            os.remove(audio_path)
            print("Existing file deleted.")

        stream.download(output_path=output_path)
        
        video_clip = stream.default_filename
        audio_path_temp = video_clip.replace(".mp4", ".mp3")
        clip = AudioFileClip(video_clip)
        clip.write_audiofile(audio_path)

        os.remove(video_clip)

        print("Audio downloaded successfully as MP3!")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_path = "."  # Use the current directory
    download_youtube_audio(video_url, output_path)
