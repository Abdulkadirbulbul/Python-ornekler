# Örnek 26: Python ile bir liste içinde 5’in katları olan sayıları listeleme.


liste=[18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]
katlari=[]
for i in liste:
    if i%5==0:
        katlari.append(i)


print(katlari)
