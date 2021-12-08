# Örnek 23: Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplayan Python örneği:

genislik=int(input("Genişliği giriniz."))
yukseklik=int(input("Yüksekliği giriniz."))

def alanhesapla(yukseklik, genislik):
    return  yukseklik*genislik

print("Dikdörtgenin alanı : "+str(alanhesapla(yukseklik,genislik)))