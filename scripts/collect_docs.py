from pathlib import Path
from datetime import datetime
import re

import httpx
from bs4 import BeautifulSoup


OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


DOCUMENTS = [
    ("python_tutorial", "https://docs.python.org/3/tutorial/"),
    ("python_venv", "https://docs.python.org/3/library/venv.html"),
    ("python_asyncio", "https://docs.python.org/3/library/asyncio.html"),

    ("fastapi_tutorial", "https://fastapi.tiangolo.com/tutorial/"),
    ("fastapi_first_steps", "https://fastapi.tiangolo.com/tutorial/first-steps/"),
    ("fastapi_path_params", "https://fastapi.tiangolo.com/tutorial/path-params/"),
    ("fastapi_request_body", "https://fastapi.tiangolo.com/tutorial/body/"),

    ("pydantic", "https://docs.pydantic.dev/latest/"),
    ("pydantic_models", "https://docs.pydantic.dev/latest/concepts/models/"),

    ("httpx", "https://www.python-httpx.org/"),
    ("httpx_quickstart", "https://www.python-httpx.org/quickstart/"),

    ("pytest_getting_started", "https://docs.pytest.org/en/stable/getting-started.html"),
    ("pytest_how_to", "https://docs.pytest.org/en/stable/how-to/"),

    ("openapi", "https://spec.openapis.org/oas/latest.html"),

    ("langchain_overview", "https://docs.langchain.com/oss/python/langchain/overview"),
    ("langchain_rag", "https://docs.langchain.com/oss/python/langchain/rag"),

    ("langgraph_overview", "https://docs.langchain.com/oss/python/langgraph/overview"),

    ("chroma_overview", "https://docs.trychroma.com/docs/overview/introduction"),

    ("uvicorn", "https://www.uvicorn.org/"),

    ("requests", "https://requests.readthedocs.io/en/latest/"),

    ("starlette", "https://www.starlette.io/"),
]


def clean_text(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header",
        "noscript",
    ]):
        tag.decompose()

    main = soup.find("main") or soup.find("article") or soup.body

    if main is None:
        return ""

    text = main.get_text("\n")

    lines = []
    for line in text.splitlines():
        line = re.sub(r"\s+", " ", line).strip()

        if line:
            lines.append(line)

    return "\n".join(lines)


def main():
    headers = {
        "User-Agent": "iyuno-agent-portfolio/1.0"
    }

    success = 0
    failed = 0

    with httpx.Client(
        timeout=30.0,
        follow_redirects=True,
        headers=headers,
    ) as client:

        for name, url in DOCUMENTS:
            print(f"\n다운로드 중: {name}")

            try:
                response = client.get(url)
                response.raise_for_status()

                text = clean_text(response.text)

                if not text:
                    raise ValueError("본문을 추출하지 못했습니다.")

                file_path = OUTPUT_DIR / f"{name}.txt"

                file_path.write_text(
                    f"Source URL: {url}\n"
                    f"Retrieved: {datetime.now().isoformat()}\n\n"
                    f"{text}",
                    encoding="utf-8",
                )

                print(f"성공: {file_path}")
                success += 1

            except Exception as e:
                print(f"실패: {e}")
                failed += 1

    print("\n==============================")
    print(f"성공: {success}")
    print(f"실패: {failed}")
    print(f"전체: {len(DOCUMENTS)}")
    print("==============================")


if __name__ == "__main__":
    main()