import requests
from bs4 import BeautifulSoup

def get_huggingface_models(query):
    url = f"https://huggingface.co/models?search={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: Failed to fetch models. Status code {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    model_links = []

    for link in soup.find_all("a", href=True):
        href = link['href']
        if href.startswith("/") and href.count("/") == 2 and not href.endswith("/likes"):
            full_url = "https://huggingface.co" + href
            if full_url not in model_links:
                model_links.append(full_url)

    return model_links[:5]
