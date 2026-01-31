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
        # task="translate" will turn Hindi (or any lang) into English
        # Remove task="translate" if you want the original language
        result = model.transcribe(audio_path, verbose=False)
        
        results = []
        for segment in result['segments']:
            results.append({
                "start": segment['start'],
                "end": segment['end'],
                "text": segment['text'].strip()
            })
            # Optional: Print progress
            print(f"[{segment['start']:.2f}s]: {segment['text'].strip()}")
        
        print("result", result)
        detected_lang = result.get("language", "unknown")
        print(f"Transcription completed. Language: {detected_lang}")
        
        return results, detected_lang

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [], "unknown"