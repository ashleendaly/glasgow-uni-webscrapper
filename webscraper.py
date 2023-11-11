import requests
import csv
from bs4 import BeautifulSoup

urls = []

with open("GUSS_AI_Target_Webpages.csv", "r") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for url in csvreader:
        urls.append("https://" + url[1])

url = urls[0]

data = requests.get(url)
html = BeautifulSoup(data.text, "html.parser")

content = html.find("main").get_text()
print(content)