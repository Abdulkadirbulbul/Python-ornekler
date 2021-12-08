#  Örnek 25: Verilen bir tarihin yılın kaçıncı günü olduğunu bulan Python Örneği.

def ArtıkYıl(yıl):
    artık = False
    if yıl % 400 == 0 or (yıl % 4 == 0 and yıl % 100 != 0): artık = True
    return artık


def YılınGünü(Ay, Gün, Yıl):
    günler = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if ArtıkYıl(Yıl):
        günler[1] = 29
    sıra = 0
    for a in range(Ay - 1):
        sıra += günler[a]
    sıra += Gün
    return sıra


print(YılınGünü(4, 9, 2018))