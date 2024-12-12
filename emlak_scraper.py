from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
import pandas as pd

liste=[]

driver_path=""#chromium yolu
service=Service(driver_path)
browser=webdriver.Chrome(service=service)
browser.get("url")#kaynak alınacak emlak sitesi
kaynak=browser.page_source
soup=BeautifulSoup(kaynak,"html.parser")
fiyatlar=soup.find_all("div",class_="_3Q-7xT")
ilceler=soup.find_all("div",class_='manJWF')
ilceler_listesi=[]
for ilce in ilceler:
    ilce_tag = ilce.find("div", class_='_2wVG12')
    if ilce_tag:
        full_text = ilce_tag.text.strip()  # Örneğin: "Muğla - Marmaris - Hisarönü Mh."
        parts = full_text.split(" - ")  # "-" ile metni böler
        if len(parts) > 1:
            ilce_name = parts[1]  # İkinci kısım ilçedir
            ilceler_listesi.append(ilce_name)
fiyat_listesi=[]
for fiyat in fiyatlar:

    fiyat_tag= fiyat.find("p",class_='_2C5UCT')
    if fiyat_tag:

        fiyat_listesi.append(fiyat_tag.text.strip())
max_len = max(len(ilceler_listesi), len(fiyat_listesi))

# Kısa olan listeleri None ile dolduruyoruz
ilceler_listesi += [None] * (max_len - len(ilceler_listesi))
fiyat_listesi += [None] * (max_len - len(fiyat_listesi))
data = {
    'İlçe': ilceler_listesi,
    'Fiyat': fiyat_listesi
}

# DataFrame oluşturma
df = pd.DataFrame(data)

# DataFrame'i Excel dosyasına kaydetme
df.to_excel('ilceler_ve_fiyatlar.xlsx', index=False, engine='openpyxl')
marmaris_data = df[df['İlçe'] == 'Marmaris']
marmaris_data['Fiyat'] = marmaris_data['Fiyat'].str.replace(' TL', '').str.replace(',', '').astype(float)
ortalama_fiyat = marmaris_data['Fiyat'].mean()

print(f"Marmaris ilçesinin ortalama fiyatı: {ortalama_fiyat:.2f} TL")
browser.quit()
