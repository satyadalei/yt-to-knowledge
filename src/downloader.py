import subprocess
from pathlib import Path


def download_audio(youtube_url: str) -> Path:
    output_dir = Path("data/audio")
    output_dir.mkdir(parents=True, exist_ok=True)

    # This will save the audio in the data/audio folder with the title of the video as the filename
    output_path = output_dir / "%(title)s.%(ext)s"

    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "-o", str(output_path),
        youtube_url,
    ]

    subprocess.run(command, check=True)

    # return latest downloaded file
    return max(output_dir.glob("*.mp3"), key=lambda f: f.stat().st_mtime)
