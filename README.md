

project requirements

```text
I want to build a python project which takes a yotube url & then extracts the audio & then generates the transcripts or tranlates (if hindi then to english) & then from that using locall Ollama LLM generates 

1. summary 
2. pure transcript with time stamp
3. Major key concepts
4. All notes
5. Concept diagrams

etc
```


youtube-ai-notes/
│
├── pyproject.toml        # managed by uv
├── uv.lock               # exact dependency versions
├── README.md
│
├── data/
│   ├── audio/            # extracted mp3 files
│   ├── transcripts/      # raw + translated transcripts
│   └── outputs/          # final LLM-generated content
│       ├── summary.md
│       ├── notes.md
│       ├── concepts.md
│       └── diagrams.md
│
├── src/
│   ├── __init__.py
│
│   ├── downloader.py     # YouTube → audio
│   ├── transcriber.py    # Whisper transcription
│   ├── translator.py     # Hindi → English logic
│   ├── formatter.py      # timestamps, cleaning text
│   ├── llm.py            # Ollama interface
│   ├── generators.py     # summary, notes, concepts, diagrams
│   └── main.py           # entry point
│
└── scripts/
    └── run.sh             # optional CLI shortcut

```bash
uv run python -m src.main "https://www.youtube.com/watch?v=r6zFZQm0hcc"
```

uv run python -m src.main "https://www.youtube.com/watch?v=iBnWHZmlIyY"