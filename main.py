from scraper.huggingface import get_huggingface_models
#from scraper.github import get_github_trending
#from scraper.github import get_github_search_results
from scraper.github import get_github_search_api 
from scraper.arxiv import get_arxiv_papers 
from llm.summarize import summarize_abstract
from nlp.summarize import summarize_text


if __name__ == "__main__":
    query = input("Enter a topic: ").strip()

    print("\n Hugging Face Models:")
    models = get_huggingface_models(query)
    for m in models:
        print("•", m)

    print("\n GitHub Repositories:")
    repos = get_github_search_api(query)
    if repos:
        for r in repos:
            print("•", r)
    else:
        print("No GitHub repos found.")

    
    
    
print("\nResearch Papers from arXiv:")
papers = get_arxiv_papers(query)
if papers:
    for p in papers:
        summary = summarize_text(f"{p['title']}. {p['summary']}")
        print(f"• {p['title']}\n  Link: {p['link']}\n  Summary: {summary}\n")
else:
    print("No relevant papers found.")
