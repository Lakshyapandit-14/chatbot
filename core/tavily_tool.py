
# core/tavily_tool.py

from tavily import TavilyClient
from core.interfaces import SearchService

class TavilySearch(SearchService):

    def __init__(self, api_key: str):
        self.client = TavilyClient(api_key=api_key)

    def search(self, query: str) -> str:
        """Call Tavily API and return human-readable response"""

        result = self.client.search(query=query, include_answer=True)

        answer = result.get("answer", "No summary available.")
        results = result.get("results", [])

        sources = "\n".join(
            f"- **{r.get('title')}** — {r.get('url')}"
            for r in results
        )

        return f"### 📌 Answer\n{answer}\n\n### 🔗 Sources\n{sources}"