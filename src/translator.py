import whisper
from typing import List, Dict

from src.model_loader import model

def translate_if_needed(audio_path: str, detected_language: str) -> List[Dict]:
    """
    If the detected language is Hindi ('hi'), it re-processes the audio 
    to translate it into English.
    """
    if detected_language != "hi":
        print(f"Language is {detected_language}, skipping translation.")
        return []

    print("Hindi detected. Translating to English...")
    
    try:
        # task="translate" always translates the source audio into English
        result = model.transcribe(audio_path, task="translate")

        translated = []
        for segment in result['segments']:
            translated.append({
                "start": segment['start'],
                "end": segment['end'],
                "text": segment['text'].strip()
            })

        return translated

    except Exception as e:
        print(f"Translation failed: {e}")
        return []