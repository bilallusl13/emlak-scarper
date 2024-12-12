# Emlakjet Scraper

Bu proje, web sitesinden kiralık daire verilerini çekmekte ve bu verileri ilçelere göre ayırarak bir Excel dosyasına aktarmaktadır.

## Özellikler

- Muğla ilindeki kiralık dairelerin fiyatlarını ve ilçelerini toplar.
- Verileri ilçelere göre ayırır.
- Toplanan verileri `ilceler_ve_fiyatlar.xlsx` adlı bir Excel dosyasına kaydeder.
- Marmaris ilçesi için ortalama kiralık fiyatı hesaplar.

## Kullanım

### Gereksinimler

Bu proje için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- `BeautifulSoup`
- `selenium`
- `pandas`
- `openpyxl`

Bu kütüphaneleri yüklemek için terminalde şu komutu çalıştırın:

```bash
pip install beautifulsoup4 selenium pandas openpyxl
