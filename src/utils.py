from urllib.parse import urlparse, parse_qs


def clean_youtube_url(url: str) -> str:
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)

    if "v" in qs:
        return f"https://www.youtube.com/watch?v={qs['v'][0]}"

    return url
