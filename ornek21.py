# Örnek 21: Maaşı ve zam oranı girilen işçinin zamlı maaşını
# hesaplayarak ekranda gösteren Python örneği:

maas = int(input("Maaşınızı Girin."))
zamorani = int(input("Zam oranını girin."))

guncelmaas = maas + (maas * zamorani) / 100
print(guncelmaas)
