import whisper
from typing import List, Dict, Tuple
import sys
import os

from src.model_loader import model

def transcribe(audio_path: str) -> Tuple[List[Dict], str]:
    if not os.path.exists(audio_path):
        print(f"Error: The file '{audio_path}' was not found.")
        return [], "unknown"

    try:
        print("Transcribing (this may take a while)...")
        result = model.transcribe(audio_path, verbose=True)
        print("result", result["text"])
        # write to a text file or Json file
        with open("transcript.txt", "w") as f:
            f.write(result["text"])
        return result["text"], result["language"]
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [], "unknown"