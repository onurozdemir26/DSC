sayilar=[]
sifirlar = []
sonuc=[ ]
while True:
    sayi=int(input("Lütfen bir adet sayı girin: "))
    sayilar.append(sayi)
    for sayii in sayilar:
        if sayii==0:
            sifirlar.append(sayii)
            sayilar.remove(0)
            sonuc=sifirlar+sayilar
    soru=input("Devam etmek istediğine emin misin? E/H: ")
    if soru=="e" or soru=="E":
        continue
    else:
        print(sonuc)
        break







