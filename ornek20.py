# Örnek 20: 1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların
# toplamını ayrı ayrı bulan ve sonucu ekranda gösteren Python Örneği


sayi=int(input("Sayı giriniz."))
tektoplam=0
cifttoplam=0
for i in range (1,sayi+1):
    if i%2==0:
        cifttoplam+=i
    else:
        tektoplam+=i
print("Teklerin toplamı : "+str(tektoplam)+" \nÇiftlerin toplamı : "+str(cifttoplam))
