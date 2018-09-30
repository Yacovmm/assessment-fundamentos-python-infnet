import requests
from bs4 import BeautifulSoup
url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
request = requests.get(url)
  # Testando se a conexão funcionou
if request.status_code != 200:
      request.raise_for_status()

request.encoding = 'utf-8' # Mudar o enconding (acentuação)
html = request.text
# print(html)
soup = BeautifulSoup(html, "lxml")
# print(soup)
#Tabela
for estados in soup.find_all('div', class_='tabela'):
    d = estados.text

print(d)