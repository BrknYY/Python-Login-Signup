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

users = load_user_data()

# Kullanıcı verilerini dosyaya kaydet
def save_user_data():
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

# Tkinter arayüzünü oluştur
arayuz = tk.Tk()
arayuz.title("Kayıt Ol")
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
sifre_kutusu = tk.Entry(textvariable=sifre, show="?")
sifre_kutusu.place(x=130, y=35)

# Kayıt ol butonu
def kayit_ol():
    kullanici_adi = kullanici_adi_kutusu.get()
    sifre = sifre_kutusu.get()
    if kullanici_adi in users:
        doğru_yanlis.config(text="Kullanıcı adı zaten alınmış!", fg="red")
    else:
        users[kullanici_adi] = sifre
        save_user_data()
        doğru_yanlis.config(text="Kayıt başarılı!", fg="green")

kayit_ol_butonu = tk.Button(text="Kayıt Ol", command=kayit_ol)
kayit_ol_butonu.place(x=150, y=65)

# Durum etiketi
doğru_yanlis = tk.Label(text="", font="Verdana 10 bold")
doğru_yanlis.place(x=100, y=95)

# Arayüzü başlat
arayuz.mainloop()
