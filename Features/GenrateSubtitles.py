import whisper
import os
from pydub import AudioSegment
import Transcipt_segment_classification as tsc
import Youtube_audio as yta
import Youtube_audio_segments as syta
import csv

def generate_transcriptions(file_path, output_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        i = 1
        for row in reader:
            link = row[0]
            yta.download_youtube_audio(link, output_path, i)
            i += 1

    model = whisper.load_model("base")
    with open("transcription_output.csv", "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Video', 'Transcription']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for x in range(1, i): 
            result = model.transcribe(f"audio{x}.mp3")
            transcription_text = result["text"]

            writer.writerow({'Video': f"Video {x}", 'Transcription': transcription_text})

            print(f"Video {x} transcription:")
            print(transcription_text)

    print("Transcription output saved to 'transcription_output.csv'")
