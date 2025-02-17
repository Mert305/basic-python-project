import random

def sayi_tahmin_oyunu():
    print("🎯 Sayı Tahmin Oyununa Hoş Geldiniz! 🎯")
    
    # Zorluk seviyesi seçimi
    print("\nZorluk seviyesini seçin:")
    print("1 - Kolay (1-50 arası, 10 hak)")
    print("2 - Orta (1-100 arası, 7 hak)")
    print("3 - Zor (1-200 arası, 5 hak)")

    secim = input("Seçiminizi yapın (1, 2 veya 3): ")
    
    if secim == "1":
        alt_sinir, ust_sinir, hak = 1, 50, 10
    elif secim == "2":
        alt_sinir, ust_sinir, hak = 1, 100, 7
    elif secim == "3":
        alt_sinir, ust_sinir, hak = 1, 200, 5
    else:
        print("Geçersiz seçim! Oyun sonlandırılıyor.")
        return
    
    tutulan_sayi = random.randint(alt_sinir, ust_sinir)
    sayac = 0

    print(f"\n{alt_sinir} ile {ust_sinir} arasında bir sayı tuttum. Tahmin etmeye başla!")
    print(f"{hak} tahmin hakkın var. İyi şanslar! 🍀")

    while sayac < hak:
            sayi = int(input("\nTahmininizi girin: "))
            sayac += 1
            kalan_hak = hak - sayac

            if sayi < tutulan_sayi:
                print(f"🔼 Daha büyük bir sayı girin! (Kalan hakkınız: {kalan_hak})")
            elif sayi > tutulan_sayi:
                print(f"🔽 Daha küçük bir sayı girin! (Kalan hakkınız: {kalan_hak})")
            elif sayi == tutulan_sayi:
                print(f"🎉 Tebrikler! {sayac}. denemede doğru tahmin ettiniz: {tutulan_sayi} 🎯")
                break
            else:
                print(f"😢 Maalesef hakkınız bitti. Tutulan sayı: {tutulan_sayi}")

# Oyunu başlat
sayi_tahmin_oyunu()
