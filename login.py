import tkinter as tk
import json

# Kullanıcı veritabanı oluştur
users = {}

# Kullanıcı verilerini kaydetmek için dosya adı
USER_DATA_FILE = "users.json"

# Kullanıcı verilerini dosyadan yükle
def load_user_data():
    try:
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Kullanıcı verilerini dosyaya kaydet
def save_user_data():
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

# Tkinter arayüzünü oluştur
arayuz = tk.Tk()
arayuz.title("Giriş Yap")
arayuz.geometry("400x200")

# Kullanıcı adı ve şifre için etiketler
kullanici_adi_etiketi = tk.Label(text="Kullanıcı Adı:")
kullanici_adi_etiketi.place(x=20, y=10)

sifre_etiketi = tk.Label(text="Şifre:")
sifre_etiketi.place(x=20, y=35)

# Kullanıcı adı ve şifre için giriş kutuları
kullanici_adi = tk.StringVar()
kullanici_adi_kutusu = tk.Entry(textvariable=kullanici_adi)
kullanici_adi_kutusu.place(x=130, y=10)

sifre = tk.StringVar()
sifre_kutusu = tk.Entry(arayuz, textvariable=sifre, show="?")
sifre_kutusu.place(x=130, y=35)

# Giriş yap butonu
def giris_yap():
    kullanici_adi = kullanici_adi_kutusu.get()
    sifre = sifre_kutusu.get()
    if kullanici_adi not in users:
        dogru_yanlis.config(text="Kullanıcı adı bulunamadı!", fg="red")
    elif users[kullanici_adi] != sifre:
        dogru_yanlis.config(text="Şifre yanlış!", fg="red")
    else:
        dogru_yanlis.config(text="Giriş başarılı!", fg="green")

giris_yap_butonu = tk.Button(text="Giriş Yap", command=giris_yap)
giris_yap_butonu.place(x=150, y=65)

# Durum etiketi
dogru_yanlis = tk.Label(text="", font="Verdana 10 bold")
dogru_yanlis.place(x=100, y=95)

# Kullanıcı verilerini dosyadan yükle
users = load_user_data()

# Arayüzü başlat
arayuz.mainloop()
