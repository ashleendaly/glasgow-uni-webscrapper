import requests
import csv
from bs4 import BeautifulSoup

urls = []

with open("GUSS_AI_Target_Webpages.csv", "r") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for url in csvreader:
        urls.append("https://" + url[1])


url = urls[0] # using student finances url for report

def extract_text(url):
    data = requests.get(url)
    html = BeautifulSoup(data.text, "html.parser")

    main = html.find("main")
    content = main.findAll("div", {"class": "maincontent"})

    text = ""

    for item in content:
        text += item.get_text()

    return text

for i, url in enumerate(urls):
    with open(f".\\llms\\aiseo\\out\\url_{i}.txt", "w", encoding='utf-8') as file:
        text = extract_text(url)
        safe_text = text.encode('cp1252', errors='ignore').decode('cp1252')
        file.write(safe_text)