print("""

BAHŞİŞ YEMEK VERGİ HESAPLAMA PAROGRAMI

                    Hazırlayan : Mert Ergün
""")

totalFiyat = float(input("Vergi ve bahşiş dahil olmadan gelen hesap tutarını giriniz:  : "))
vergi  = float(totalFiyat *8  / 100)
bahsis = float(totalFiyat *10 / 100)
toplam = float(totalFiyat + vergi + bahsis)

print ("Ödediğin Vergi Miktarı : " , vergi, "TL" )
print ("Ödediğin Bahşiş Miktarı : " , bahsis, "TL" )
print ("Toplam ödemeniz gereken tutar : " , vergi + bahsis + totalFiyat , "TL")

