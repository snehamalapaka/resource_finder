import requests

def get_github_search_api(query):
    url = "https://api.github.com/search/repositories"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        # Optional: add your token here if you hit rate limits
        # "Authorization": "token YOUR_GITHUB_TOKEN"
    }
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 5
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f" GitHub API error: {response.status_code}")
        return []

    data = response.json()
    results = []

    for repo in data.get("items", []):
        results.append(f"{repo['html_url']} Likes {repo['stargazers_count']}")

    return results
