from src.llm import run_ollama


def generate_summary(text: str) -> str:
    prompt = f"""
Summarize the following transcript clearly and concisely:

{text}
"""
    return run_ollama(prompt)


def generate_key_concepts(text: str) -> str:
    prompt = f"""
Extract major key concepts as bullet points:

{text}
"""
    return run_ollama(prompt)


def generate_notes(text: str) -> str:
    prompt = f"""
Create structured notes with headings and sub-points:

{text}
"""
    return run_ollama(prompt)


def generate_diagram(text: str) -> str:
    prompt = f"""
Create a concept diagram using Mermaid syntax.
Only output valid Mermaid code.

{text}
"""
    return run_ollama(prompt)
