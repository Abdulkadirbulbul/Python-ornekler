# Örnek 9: Girilen Sayının Pozitif, Negatif, ya da 0 Olduğunu Bulan Python Örneği

sayi=int(input("Sayıyı giriniz"))
if sayi>0:
    print("Sayınız pozitifdir.")
elif sayi==0:
    print("Sayınız ne negatif nede pozitifdir.")
else:
    print("Sayınız negatifdir.")