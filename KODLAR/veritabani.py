database = ["admin"]


#Fonksiyonlar //başlangıç
def giris_yap():
  giris = str(input("Kullanıcı Adınızı Giriniz: "))
  if giris in database:
    print("Sisteme '{}' Olarak Başarıyla Giriş Yaptınız".format(giris))
  else:
    print("Sistemde Böyle Bir Kullanıcı Bulunmuyor")


def kayit_ol():
  new_user = str(input("Yeni Kullanıcı Kaydı\nİsim: "))
  if new_user in database:
    print("Bu Kullanıcı Zaten Kayıtlı")
  else:
    database.append(new_user)
    print("Sisteme Başarıyla Kayıt Oldunuz")


def database_list():
  print(database)
#Fonksiyonlar //bitiş

while True:
  print(
    "Yapmak istediğiniz işlemi seçiniz:\n1-) GİRİŞ YAP\n2-) KAYIT OL\n3-) ÇIKIŞ YAP\n4-) KULLANICI LİSTESİ"
  )
  islem = int(
    input("Seçiminizi 1, 2 veya 3 olarak girin\nYapmak istediğiniz seçim: "))

  if islem == 2:
    kayit_ol()
  elif islem == 1:
    giris_yap()
  elif islem == 3:
    print("Programdan Başarıyla Çıkış Yapıldı")
  elif islem == 4:
    database_list()
  else:
    print("Lütfen Geçerli Bir Sayı Giriniz")
