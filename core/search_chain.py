# core/search_chain.py

from langchain_core.runnables import RunnableLambda
from core.interfaces import SearchService

class SearchChain:

    def __init__(self, service: SearchService):
        self.service = service
        self.chain = RunnableLambda(self._run)

    def _run(self, query: str) -> str:
        """Executes the search pipeline"""
        return self.service.search(query)

    def run(self, query: str) -> str:
        return self.chain.invoke(query)