from random import randint
 
sayılar=randint(1, 100)
sayac=0
 
while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında değer girin (0 Çıkış):"))
    if(sayi==0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < sayılar:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > sayılar:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(sayılar))
        print("Tahmin sayınız {0}".format(sayac))