# Örnek 22: Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesaplayan Python örneği.

r = int(input("Yarı çapı giriniz."))
pi = 3


def alanhesapla(r):
    return pi * r * r

print("Dairenin alanı : " + str(alanhesapla(r)))
