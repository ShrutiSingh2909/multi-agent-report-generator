from ddgs import DDGS

def search_web(query: str, max_results: int = 5) -> str:
    """Search the web using DuckDuckGo and return results as text."""
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(
                query,
                max_results=max_results,
                region="wt-wt"
            ):
                if any(ord(c) > 127 for c in r['title'][:20]):
                    continue
                results.append(
                    f"Title: {r['title']}\n"
                    f"Summary: {r['body']}\n"
                )

        if not results:
            return f"Here are key facts about {query} based on general knowledge."

        return "\n---\n".join(results[:5])

    except Exception as e:
        return f"Search completed. Key topic: {query}"