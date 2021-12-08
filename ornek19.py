# Örnek 19: Girilen Sayının Asal Sayı mı Değil mi olduğunu bulan Python Örneği

sayi=int(input("Sayıyı giriniz"))

bolensayisi=0
for i in range(2,sayi):
    if sayi%i==0:
        bolensayisi+=1
    
if bolensayisi==0:
    print("Asaldır.")
else:
    print("Asal Değildir.")


