sayi = int(input("Lütfen Bir Sayı Giriniz: "))

faktoriyel = 1

if sayi < 1:
    print("Negatif Sayıların Faktoriyeli Hesaplanamaz")

elif sayi == 0:
    print("0'ın Faktoriyeli 1'dir")

else:
    for i in range(1,sayi + 1):
        faktoriyel = faktoriyel*i
    print("Cevap:",faktoriyel)