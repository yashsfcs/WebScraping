from bs4 import BeautifulSoup
import requests

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
response = requests.get('https://pythonhow.com/example.html', headers=header)


content=response.content

soup=BeautifulSoup(content, "html.parser")

all=soup.find_all("div",{"class":"cities"})

print(all[0].find("h2").text)

for each in all:
     print(each.find("h2").text)
     print(each.find("p").text)
     print("-----------------------------------------------------------")