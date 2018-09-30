import requests
from bs4 import BeautifulSoup

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
# Usando requests
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

html = requisicao.text
soup = BeautifulSoup(html, "lxml")
list = []


tabela = soup.find_all("div", class_="tabela");

for linha in tabela:
    linhas = soup.find_all("div", class_="linha")
    for linha in linhas:

        list.append(linha.text)

sigla = input("Digite a sigla: ")

if sigla == "DF" or sigla == "df":
    print(list[0])
if sigla == "GO" or sigla == "go":
    print(list[1])
if sigla == "MT" or sigla == "mt":
    print(list[2])
if sigla == "MS" or sigla == "ms":
    print(list[3])