print("-*-*-*-*-*-*-*-*-*-\nARMSTRONG SAYI PROGRAMI\n"
      "-*-*-*-*-*-*-*-*-*-")


alinan_deger =int(input("Bir sayı giriniz:"))

basamak_sayisi = str(alinan_deger)
toplam = 0

for i in basamak_sayisi:
      üs_alma_sonucu= int(i) ** len(basamak_sayisi)
      toplam+=üs_alma_sonucu

if(toplam == alinan_deger):
      print(alinan_deger,"Armstrong sayıdır...")
else:
      print(alinan_deger, "Armstrong sayı değildir...")


