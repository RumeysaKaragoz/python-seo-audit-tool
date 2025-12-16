import requests
from bs4 import BeautifulSoup

url = input("Analiz edilecek URL'yi girin: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.string if soup.title else "Bulunamadı"

print("Title:", title)
print("Title uzunluğu:", len(title))
                
