from dotenv import load_dotenv
import sys
from pathlib import Path
from src.downloader import download_audio

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.main <youtube_url>")
        sys.exit(1)

    youtube_url = clean_youtube_url(sys.argv[1])
    print(f"YouTube URL: {youtube_url}")



if __name__ == "__main__":
    main()
