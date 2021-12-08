# 24. Python ile say Tahmin Oyunu Yapımı. 0 ile 100 arasında
from random import randint

rand=randint(1,100)
print(rand)
x=int(input("Tahmin ediniz"))

while x!=rand:
    if x>rand:
        print(("Aşağıda..."))

    else:
        print("Yukarıda")

    x=int(input("Tekrar tahmin ediniz."))
print("Tebrikler buldunuz.")