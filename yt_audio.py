from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_youtube_audio_segments(video_url, output_path, segment_length=30 ):
    try:
        yt = YouTube(video_url)
        # Get the highest resolution audio stream available
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio
        audio_filename = audio_stream.download(output_path=output_path)

        # Convert the audio to an AudioFileClip
        audio_clip = AudioFileClip(audio_filename)

        # Calculate the number of segments
        total_duration = audio_clip.duration
        num_segments = int(total_duration // segment_length)
        # Remove existing audio files
        for i in range(num_segments):
            output_file = os.path.join(output_path, f"audio{i+1}.mp3")
            if os.path.exists(output_file):
                os.remove(output_file)
                print(f"Existing file {output_file} deleted.")
                
        for i in range(num_segments):
            start_time = i * segment_length
            end_time = min((i + 1) * segment_length, total_duration)  # Ensure end time doesn't exceed audio duration

            # Extract the segment
            segment_clip = audio_clip.subclip(start_time, end_time)

            # Define the output file name for the segment
            output_file = os.path.join(output_path, f"audio{i+1}.mp3")

            # Write the segment to a file
            segment_clip.write_audiofile(output_file, codec='mp3')

            print(f"Segment {i+1} downloaded successfully!")


        start_time = num_segments * segment_length
        end_time =  total_duration 
        remaining_audio_clip = audio_clip.subclip(start_time, end_time)
        remaining_audio_filename = os.path.join(output_path, f"audio{num_segments+1}.mp3")
        remaining_audio_clip.write_audiofile(remaining_audio_filename, codec='mp3')

        print(f"Segment {c+1} downloaded successfully!")

        return num_segments


    except Exception as e:
        print("Error:", str(e))
