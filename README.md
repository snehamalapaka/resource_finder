#  Resource Finder

A Python-based tool to discover the latest Hugging Face models, GitHub repositories, and arXiv research papers related to a specific machine learning topic — all in one place, with concise summaries of relevant research.


##  Features

- Scrapes trending GitHub repositories using keyword matching.
- Pulls latest Hugging Face models relevant to your query.
- Fetches top arXiv papers (from cs.LG, cs.AI, stat.ML) based on keyword match.
- Summarizes abstracts using the `t5-small` model.
- Saves or prints useful summaries for research or exploration.

##  T5 Small Model:

- *Versatile NLP Model*: T5 Small is a compact yet powerful transformer model (60M parameters) capable of handling diverse NLP tasks like machine translation, sentiment analysis, and summarization.

- *Text-to-Text Framework*: Unlike traditional models, T5 reformulates all tasks as a text-in/text-out problem, offering a consistent and flexible approach to different NLP challenges.

- *Fine-Tunable & Efficient*: Developed by Google, it is pretrained on a massive dataset and can be fine-tuned for domain-specific tasks with excellent speed and efficiency.

- *Ideal for Developers & Researchers*: Its performance and simplicity make it a great tool for real-world applications like document summarization, question answering, and other generative NLP tasks.


##  File Structure
resource_finder/
├── main.py # Entry point
├── github.py # Scraper for GitHub repos
├── huggingfaces.py # Scraper for Hugging Face models
├── arxiv.py # Scraper for arXiv research papers
├── nlp_summarise.py # Summarizes using t5-small



##  How to Run

1. **Clone the repo:**

   ```bash
   git clone https://github.com/snehamalapaka/resource_finder.git
   cd resource_finder

