from typing import List, Dict

def format_transcript(segments: List[Dict]) -> str:
    lines = []
    for seg in segments:
        lines.append(
            f"[{seg['start']:.2f}s - {seg['end']:.2f}s] {seg['text']}"
        )
    return "\n".join(lines)
