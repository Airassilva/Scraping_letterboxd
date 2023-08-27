import csv
import requests
from bs4 import BeautifulSoup

# URL da página que queremos fazer scraping
url = "https://letterboxd.com/jack/list/official-top-250-films-with-the-most-fans/detail/"

# Conexão: Enviar uma solicitação GET para a URL
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (status 200)
if response.status_code == 200:
    # Parse a página com o BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontre todos os elementos HTML que contêm as informações dos filmes
    reviews = soup.find_all("div", class_="film-detail-content")

    # Crie arquivo CSV
    file = open('export_data.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    headers = ['Top melhores filmes', 'Notas']
    writer.writerow(headers)

    # Loop pelos elementos e extrair informações
    for review in reviews:
        # Extrair o título do filme
        title = review.find("h2", class_="headline-2 prettify").text.strip()

        # Extrair as notas
        stars = review.find("p", class_="film-detail-meta rating-green").text.strip()

        # Escrever as informações no arquivo CSV
        row = [title, stars]
        writer.writerow(row)

    file.close()
    print("Dados exportados para export_data.csv.")

else:
    print("Falha ao acessar a página:", response.status_code)