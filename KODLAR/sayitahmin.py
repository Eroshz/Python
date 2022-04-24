import random

sayi = random.randint(1,10)
sayi_gir = int(input("Lütfen Bir Sayı Giriniz: "))


if sayi_gir == sayi :
    print("✔️  Tebrikler")

if sayi_gir > 10 :
    print("❌ 1 İle 10 Arasında Bir Sayı Gir...")

if sayi_gir < 1 :  
    print("❌ 1 İle 10 Arasında Bir sayı Gir...")

if sayi_gir != sayi : 
    print("❌ Doğru Cevap:",sayi)
