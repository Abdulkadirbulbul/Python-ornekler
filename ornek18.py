# Örnek 18: Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python Örneği.

ilk=int(input("İlk sayıyı giriniz."))
iki=int(input(("İkinci sayıyı giriniz.")))

toplam=0

for i in range(ilk,iki):
    toplam+=i
print(toplam)