
def kontrol(mail):
    miktar = 0
    for a in mail:
        if a == '@':
            miktar = miktar + 1

    if miktar == 1:
        return True
    else:
        return False


mail = input('Mail Adresi: ')
if (kontrol(mail) == True):
    print(mail+'\nMail adresi doğru')
else:
    print(mail+'\nMail adresi yanlış')