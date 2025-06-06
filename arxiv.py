import feedparser

def get_arxiv_papers(query, max_results=5):
    base_url = "http://export.arxiv.org/api/query?"
    search_query = f"search_query=all:{query}&start=0&max_results={max_results}"
    url = base_url + search_query

    feed = feedparser.parse(url)
    papers = []

    for entry in feed.entries:
        title = entry.title.strip().replace("\n", " ")
        link = entry.link
        summary = entry.summary.strip().replace("\n", " ")

        papers.append({
            "title": title,
            "link": link,
            "summary": summary
        })

    return papers
