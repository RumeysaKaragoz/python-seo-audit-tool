import requests
from bs4 import BeautifulSoup

url = input("Analiz edilecek URL'yi girin: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.string if soup.title else "Bulunamadı"

print("Title:", title)
print("Title uzunluğu:", len(title))

meta_description = soup.find("meta", attrs={"name": "description"})

if meta_description and meta_description.get("content"):
    description = meta_description["content"]
    print("Meta Description:", description)
    print("Meta Description uzunluğu:", len(description))
else:
    print("Meta Description: Bulunamadı")

if meta_description and meta_description.get("content"):
    length = len(description)
    if length < 50:
        print("⚠️ Meta description çok kısa.")
    elif length > 160:
        print("⚠️ Meta description çok uzun.")
    else:
        print("✅ Meta description uzunluğu ideal.")

                
