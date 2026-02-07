import ffmpeg
import torch
import torchaudio
from transformers import pipeline
from pathlib import Path
from typing import Union


def mp3_to_wav(audio_mp3_path: Union[str, Path], wav_path: Union[str, Path] = None) -> str:
    """Convert MP3 to 16kHz mono WAV for ASR using ffmpeg-python."""
    audio_mp3_path = Path(audio_mp3_path)
    if wav_path is None:
        wav_path = audio_mp3_path.with_suffix('.wav')
    
    stream = ffmpeg.input(str(audio_mp3_path))
    stream = ffmpeg.output(stream, str(wav_path), acodec='pcm_s16le', ac=1, ar=16000)
    ffmpeg.run(stream, overwrite_output=True, quiet=True)
    return str(wav_path)