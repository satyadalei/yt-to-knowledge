
import sys
from pathlib import Path
print("Downloading downloader...")
from src.downloader import download_audio
print("Downloading transcriber...")
from src.transcriber import transcribe
print("Downloading translator...")
from src.translator import translate_if_needed
print("Downloading formatter...")
from src.formatter import format_transcript
print("Downloading generators...")
from src.generators import (
    generate_summary,
    generate_key_concepts,
    generate_notes,
    generate_diagram,
)
print("Downloading utils...")
from src.utils import clean_youtube_url


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.main <youtube_url>")
        sys.exit(1)

    youtube_url = clean_youtube_url(sys.argv[1])
    print(f"YouTube URL: {youtube_url}")

    print("⬇️ Downloading audio...")
    audio_path = download_audio(youtube_url)

    print("📝 Transcribing...")
    transcript, language = transcribe(str(audio_path))
    
    print(f"🌍 Detected language: {language}")
    print("transcript", transcript)
    # if language == "hi":
    #     print("🔄 Translating Hindi → English...")
    #     transcript = translate_if_needed(str(audio_path), language)

    # print("transcript", transcript)
    # print("Formatting transcript...")
    # formatted_text = format_transcript(transcript)
    # print("formatted_text", formatted_text)
    
    # output_dir = Path("data/outputs")
    # output_dir.mkdir(parents=True, exist_ok=True)

    # print("🧠 Generating summary...")
    # (output_dir / "summary.md").write_text(generate_summary(formatted_text))

    # print("🧠 Generating key concepts...")
    # (output_dir / "concepts.md").write_text(generate_key_concepts(formatted_text))

    # print("🧠 Generating notes...")
    # (output_dir / "notes.md").write_text(generate_notes(formatted_text))

    # print("🧠 Generating diagram...")
    # (output_dir / "diagrams.md").write_text(generate_diagram(formatted_text))

    # print("✅ Done! Check data/outputs/")


if __name__ == "__main__":
    main()
