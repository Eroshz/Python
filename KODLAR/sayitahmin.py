import random

sayi = range(1,11)
sayi_gir = int(input("Lütfen Bir Sayı Giriniz: "))



if sayi_gir == sayi :
    print("✔️ Tebrikler")

if sayi_gir > 10 :
    print("❌ 1 İle 10 Arasında Bir Sayı Gir...")

if sayi_gir < 1 :  
    print("❌ 1 İle 10 Arasında Bir sayı Gir...")

if sayi_gir != sayi : 
    print("❌ Tekrar Dene")
