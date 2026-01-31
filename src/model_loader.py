import whisper
import sys

# Load model (Turbo is essentially a faster version of 'large-v3')
try:
    print("Loading Whisper Turbo model...")
    model = whisper.load_model("turbo", device="cpu")
    print("Model loaded successfully")
except Exception as e:
    print(f"Failed to load model: {e}")
    sys.exit(1)
