import subprocess


def run_ollama(prompt: str, model: str = "phi3:3.8b") -> str:
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
