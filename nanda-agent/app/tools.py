import httpx
from bs4 import BeautifulSoup


async def fetch_and_extract(url: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.get(url, follow_redirects=True)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            texts = [text.strip() for text in soup.stripped_strings]
            return " ".join(texts)[:15000]
    except Exception as exc:  # pragma: no cover - network-dependent
        return f"[fetch_error] {exc}"
