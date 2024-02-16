import librosa
import numpy as np
from pydub import AudioSegment

def remove_silence(audio_path, threshold=0.02, frame_length=2048):
    # Load audio file
    y, sr = librosa.load(audio_path, sr=None)

    # Convert frame_length to samples
    frame_length = int(sr * frame_length / 2048)

    # Compute energy
    energy = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=frame_length)[0]

    # Find segments with energy higher than the threshold
    segments = np.where(energy > threshold)[0]

    # Trim audio to segments with energy higher than the threshold
    trimmed_audio = y[segments[0]*frame_length:segments[-1]*frame_length]

    return trimmed_audio, sr

# # ```
# audio_path = 'audio1.mp3'
# trimmed_audio, sr = ls.remove_silence(audio_path)

# audio_segment = AudioSegment(trimmed_audio.tobytes(), frame_rate=sr, sample_width=trimmed_audio.dtype.itemsize, channels=1)

# output_path = 'trimmed_audio.mp3'
# audio_segment.export(output_path, format="mp3")
# ```