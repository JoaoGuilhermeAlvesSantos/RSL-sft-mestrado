import requests
import feedparser

query = 'all:"Fine Tun*" AND all:"Language model" AND all:"Portuguese"'
base_url = "https://export.arxiv.org/api/query"

# Busca até 500 resultados
params = {
    "search_query": query,
    "start": 0,
    "max_results": 200,  # ajuste se quiser mais
    "sortBy": "lastUpdatedDate",
    "sortOrder": "descending"
}

response = requests.get(base_url, params=params)
feed = feedparser.parse(response.text)

bib_entries = []

for entry in feed.entries:
    arxiv_id = entry.id.split('/abs/')[-1]

    # endpoint bibtex oficial
    bib_url = f"https://arxiv.org/bibtex/{arxiv_id}"
    bib = requests.get(bib_url).text

    bib_entries.append(bib)

# salvar tudo em um único arquivo .bib
with open("arxiv_results.bib", "w", encoding="utf-8") as f:
    for bib in bib_entries:
        f.write(bib + "\n\n")

print(f"Arquivo salvo com {len(bib_entries)} entradas.")
