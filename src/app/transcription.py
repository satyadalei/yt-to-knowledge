import torch
from transformers import pipeline, AutoProcessor, AutoModelForCTC
import torchaudio
from datasets import load_dataset  # Or use librosa for local files

def transcribe_hindi(audio_path: str) -> str:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Load pipeline (auto-downloads ~300MB model)
    pipe = pipeline(
        "automatic-speech-recognition",
        # model="ai4bharat/indicwav2vec-hindi",
        model="ai4bharat/indic-conformer-600m-multilingual",
        device=device
    )
    
    # Load/resample audio to 16kHz (required)
    audio, sr = torchaudio.load(audio_path)
    if sr != 16000:
        resampler = torchaudio.transforms.Resample(sr, 16000)
        audio = resampler(audio).squeeze().numpy()
    
    # Transcribe (outputs Devanagari Hindi text)
    result = pipe(audio)
    return result["text"]
