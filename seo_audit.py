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
        print("Meta description çok kısa.")
    elif length > 160:
        print("Meta description çok uzun.")
    else:
        print("Meta description uzunluğu ideal.")

h1_tags = soup.find_all("h1")
h2_tags = soup.find_all("h2")

print("\nH1 Analizi:")
print("H1 sayısı:", len(h1_tags))

if len(h1_tags) == 0:
    print("H1 etiketi bulunamadı.")
elif len(h1_tags) == 1:
    print("H1 etiketi ideal (1 adet).")
else:
    print("Birden fazla H1 etiketi var.")

print("\nH2 Analizi:")
print("H2 sayısı:", len(h2_tags))
                
