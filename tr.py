#!/usr/bin/env python3
import os

# Şu anda giriş yapan kullanıcının ismini alır
kullanici = os.getlogin()

# Bağlantı dosyalarının oluşturulacağı yolu ayarlar
yol = f"/media/{kullanici}/"

def dosyaları_listele(index):
    print("Mevcut dosya isimleri")
    # Mevcut dosya isimlerini kullanıcıya gösterir
    dosyalar = os.listdir(yol)
    for dosya in dosyalar:
        index += 1
        print(f"{index}. {dosya}")
    return index

s = str
devam_et = True
while devam_et:
    # Çok yüksek bir değer seçilmesini önlemek için 'index' değişkeni kullanılır
    index = 0
    index = dosyaları_listele(index)
    print('Yeni dosya oluşturmak için "y" ye basın')
    s = input()
    # Kullanıcıdan alınan değerin bir sayı olup olmadığı kontrol edilir
    if s.isdigit():
        # Eğer kullanıcıdan alınan değer bir sayıysa, bu sayının index'ten küçük ve 0'dan büyük olup olmadığı kontrol edilir
        if int(s) <= index and int(s) > 0:
            devam_et = False
    # Eğer kullanıcıdan alınan değer bir sayı değilse, dosya oluşturma talimatı olarak değerlendirilir
    elif s == "y":
        print("Dosya ismi")
        # Dosya ismi talep edilir
        ad = input()
        # Dosya oluşturulur
        os.chdir(yol)
        os.system(f"sudo -S mkdir {ad}")

# Dosyaları tekrar listele ve bir dosya seç
dosyalar = os.listdir(yol)
# Listeden bir dosya seçilir
secili_dosya = dosyalar[int(s) - 1]
# Sürücünün port bilgisi alınır
print("Sürücünün port bilgisi")
surucu_port = input()
# Şifre talep edilir ve bağlantı koduyla dosya eşleştirilir
os.system(f"sudo -S mount -t ntfs-3g /dev/{surucu_port} /media/{kullanici}/{secili_dosya}")
