sayilar=[]
tek=[]
while True:
    sayi = int(input('Tek bir Sayı gir : '))
    sayilar.append(sayi)
    if(int(sayi)%2!=0):
        tek.append(sayi)
    soru=input("Devam etmek istediğine emin misin? E/H: ")
    if soru=="e" or soru=="E":
        continue
    else:
        print("Girdiğiniz değerler= "+str(sayilar))
        tek.sort()
        print("En büyük tek değer= "+str(tek[-1]))
        break






