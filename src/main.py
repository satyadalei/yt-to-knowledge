from src.utils import clean_youtube_url
from dotenv import load_dotenv
import sys
from pathlib import Path
from src.downloader import download_audio
from app.yt_utils.getYtSubtitles import getTranscriptFromYtVideoId, extractYtVideoIdFromCleanYtUrl

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.main <youtube_url>")
        sys.exit(1)

    youtube_url = clean_youtube_url(sys.argv[1])
    print(f"YouTube URL: {youtube_url}")
    videoId = extractYtVideoIdFromCleanYtUrl(youtube_url)
    print(f"Video ID: {videoId}")
    # transcript = getTranscriptFromYtVideoId(videoId)
    # print(f"Transcript: {transcript}")



if __name__ == "__main__":
    main()
