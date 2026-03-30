import socket
from bs4 import BeautifulSoup

filename = "index.html"

with open(filename, "r") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

list = []

for li in soup.find_all('li'):
    li['class'] = "book"
    btn_tag = li.button
    btn_tag.decompose()

    li.find('img').parent['class'] = "image-container"

    

    img = li.find(class_="image-container")
    spans = []

    for s in li.find_all('span'):
        spans.append(s)

    data = (img, spans)
    list.append(data)
