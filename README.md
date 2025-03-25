# README

## Proje Açıklaması
Bu Python projesi, ayakkabı NFT'leri oluşturmak için bir otomasyon sağlar. Ayakkabı üst ve taban katmanlarını birleştirerek farklı kombinasyonlar oluşturur ve ayrıca önceden tanımlanmış ek bileşenleri ("attachments") NFT görsellerine ekleyerek çeşitlendirilmiş koleksiyonlar üretir.

## Gereksinimler
Bu kodun çalışması için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

```bash
pip install pillow
```

## Kullanılan Kütüphaneler
- `PIL (Pillow)`: Görselleri işlemek ve manipüle etmek için kullanılır.
- `IPython.display`: Görsellerin Jupyter Notebook içinde görüntülenmesini sağlar.
- `random`: Rastgele işlemler için kullanılır (bu kodda kullanılmıyor, ancak gelecekteki geliştirmeler için eklenmiş olabilir).
- `json`: JSON formatında veri işlemleri için kullanılır (bu kodda doğrudan kullanılmıyor).
- `os`: Dosya ve dizin işlemleri için kullanılır.
- `itertools`: Farklı permütasyon kombinasyonlarını oluşturmak için kullanılır.
- `math`: Matematiksel işlemler için kullanılır (bu kodda doğrudan kullanılmıyor).

## Kod Açıklaması
### 1. `allchances(atchcount)`
Bu fonksiyon, belirli bir sayıda ek bileşen ("attachment") için olası kombinasyonları oluşturur. Önce 1'lerin ve 0'ların farklı dizilimlerini içeren listeleri üretir, ardından bunların permütasyonlarını alarak tekrar etmeyen kombinasyonları belirler.

### 2. `atcdict(path)`
Belirtilen dizindeki dosyaları bir sözlüğe (dictionary) atar. Her dosyaya bir indeks numarası vererek dosya isimlerini saklar.

### 3. `factoryatc(finalimg)`
- Bu fonksiyon, daha önce oluşturulmuş temel NFT görsellerine ek bileşenleri (attachments) ekleyerek yeni NFT’ler üretir.
- `allchances` fonksiyonundan gelen kombinasyonlara göre ek bileşenler görsellere eklenir.
- Görseller, belirtilen dizine (`./NFTS/`) kaydedilir.

### 4. Ana Döngü
Kodun ana kısmında, `./Shoes/Ups/` klasöründeki üst ayakkabı görselleri ve `./Shoes/Soles/` klasöründeki taban görselleri birleştirilerek temel NFT görselleri oluşturulur. Her kombinasyon yeni bir dosya olarak `./NFTS/` klasörüne kaydedilir.

## Kullanım
1. `./Shoes/Ups/` klasörüne üst ayakkabı görsellerini ekleyin.
2. `./Shoes/Soles/` klasörüne taban görsellerini ekleyin.
3. `./traits/pre items/` klasörüne ek bileşenleri ekleyin.
4. Python kodunu çalıştırın.
5. Oluşturulan NFT'ler `./NFTS/` klasörüne kaydedilecektir.

## Çıktı
Program çalıştırıldığında, `./NFTS/` dizininde farklı kombinasyonlara sahip NFT görselleri oluşturulacaktır. Konsolda her bir NFT'nin ID'si ve eklenen bileşenler yazdırılır.

## Geliştirme Önerileri
- Rastgele bileşen seçimi eklenerek üretim süreci daha dinamik hale getirilebilir.
- Metadata oluşturularak her NFT’ye özgü özellikler JSON formatında kaydedilebilir.
- Görsellerin boyutlandırılması ve hizalanması için daha hassas konumlandırma eklenebilir.

