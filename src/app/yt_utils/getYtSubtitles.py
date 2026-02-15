"""
Takes a youtube Video URL and returns the subtitles 
"""

from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()


def getTranscriptFromYtVideoId(videoId:str) -> str:
    result = ytt_api.fetch(videoId)
    print(result)
    return ""
