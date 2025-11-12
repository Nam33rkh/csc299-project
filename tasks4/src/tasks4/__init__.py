from typing import Iterable, List
from openai import OpenAI

MODEL = "gpt-5-mini"

def _fallback_summary(text: str, limit: int = 10) -> str:
    """
    Rule-based fallback: return up to `limit` words from the input,
    stripped of linebreaks. Ensures we never print blank lines.
    """
    words = text.replace("\n", " ").split()
    if not words:
        return "Task summary unavailable"
    return " ".join(words[:limit])

def summarize_paragraphs(paragraphs: Iterable[str]) -> List[str]:
    client = OpenAI()  # reads OPENAI_API_KEY from env
    summaries: List[str] = []
    for para in paragraphs:
        messages = [
            {"role": "system", "content": "Return ONLY a very short task title (max 10 words). No punctuation at end."},
            {"role": "user", "content": f"Summarize this task as a short phrase:\n\n{para}"},
        ]
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                # temperature omitted (some models only allow default)
                max_completion_tokens=30,
            )
            content = (resp.choices[0].message.content or "").strip()
        except Exception:
            content = ""

        if not content:
            content = _fallback_summary(para)

        summaries.append(content)
    return summaries

def main():
    paragraphs = [
        ("Build a JSON-backed CLI that supports adding, listing, searching, and "
         "deleting tasks, with clean code structure and unit tests using pytest."),
        ("Import notes from a Markdown folder into a SQLite-backed PKMS and provide "
         "a text UI to link and search notes by tags and backlinks."),
    ]
    for i, s in enumerate(summarize_paragraphs(paragraphs), start=1):
        print(f"{i}. {s}")

if __name__ == "__main__":
    main()