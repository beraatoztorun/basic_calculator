import tkinter as tk
from tkinter import messagebox

def hesapla(event=None):
    try:
        ifade = ekran.get()  # Kullanıcının ekrana yazdığı ifadeyi alır
        sonuc = eval(ifade)  # İfadeyi değerlendir (örneğin 2+2'yi hesaplar)
        ekran.delete(0, tk.END)  # Ekranı temizler
        ekran.insert(tk.END, str(sonuc))  # Sonucu ekrana yazar
    except:
        messagebox.showerror("Hata", "Geçersiz işlem!")  # Hata durumunda mesaj gösterir

def ekrana_yaz(deger):
    ekran.insert(tk.END, deger)  # Girilen değeri ekrana ekler

def temizle(event=None):
    ekran.delete(0, tk.END)  # Ekranı temizler

def sil(event=None):
    mevcut = ekran.get()
    ekran.delete(len(mevcut) - 1, tk.END)  # Ekranın son karakterini siler

# Basma efekti için düğmenin rengini değiştir
def basma_efekti(buton):
    buton.config(bg="#dddddd")  # Bastığında açık griye dön
    pencere.after(150, lambda: buton.config(bg=buton.original_bg))  # Bir süre sonra orijinal renge döner

# Pencere oluştur
pencere = tk.Tk()
pencere.title("Basit Hesap Makinesi")
pencere.configure(bg="#2D2D2D")  # Arka plan koyu gri yapan kodlar
pencere.geometry("320x480")  # Sabit boyut yapan kodlar
pencere.resizable(False, False)  # Pencerenin boyutunu sabitler

# Ekran (giriş alanı)
ekran = tk.Entry(pencere, width=16, font=('Arial', 24, 'bold'), bd=5, justify='right', bg="#1C1C1C", fg="white")
ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# Klavye tuşlarını bağla
pencere.bind('<Return>', hesapla)  # Enter tuşu ile hesaplar
pencere.bind('<Escape>', temizle)  # Escape tuşu ile temizler
pencere.bind('<BackSpace>', sil)   # Backspace tuşu ile silme işlemi yapar

# Düğmelerin listesi
butonlar = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

# Renkleri ayarla
bg_color = "#4CAF50"  # Düğmeler için yeşil arka plan rengi
operator_color = "#FF9800"  # Operatör düğmeleri için turuncu rengi
text_color = "white"  # Yazı rengi beyaz

# Düğmeleri oluştur
for (yazi, satir, sutun) in butonlar:
    renk = bg_color if yazi not in ('/', '*', '-', '+') else operator_color
    buton = tk.Button(
        pencere, text=yazi, width=5, height=2, font=('Arial', 16, 'bold'),
        command=lambda y=yazi: ekrana_yaz(y), bg=renk, fg=text_color, bd=0,
        activebackground="#bbbbbb", activeforeground="black"
    )
    buton.original_bg = renk  # Orijinal rengini kaydet
    buton.config(command=lambda b=buton, y=yazi: [ekrana_yaz(y), basma_efekti(b)])  # Basma efekti ile ekrana yazma işlemi yapar
    buton.grid(row=satir, column=sutun, padx=5, pady=5)

# Sonucu hesaplayan '=' butonu
esittir_butonu = tk.Button(
    pencere, text='=', width=5, height=2, font=('Arial', 16, 'bold'),
    command=lambda: [hesapla(), basma_efekti(esittir_butonu)], bg="#2196F3", fg=text_color, bd=0,
    activebackground="#bbbbbb", activeforeground="black"
)
esittir_butonu.original_bg = "#2196F3"  # Orijinal rengi kaydeder
esittir_butonu.grid(row=4, column=3, padx=5, pady=5)

# Temizle butonu
temizle_butonu = tk.Button(
    pencere, text='C', width=23, height=2, font=('Arial', 16, 'bold'),
    command=lambda: [temizle(), basma_efekti(temizle_butonu)], bg="#f44336", fg=text_color, bd=0,
    activebackground="#bbbbbb", activeforeground="black"
)
temizle_butonu.original_bg = "#f44336"  # Orijinal rengi kaydet
temizle_butonu.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Klavye destekli giriş işlevi
def klavye_girisi(event):
    if event.char in '0123456789+-*/.':
        ekrana_yaz(event.char)
        # İlgili düğmeye basma efekti verir
        for widget in pencere.winfo_children():
            if isinstance(widget, tk.Button) and widget['text'] == event.char:
                basma_efekti(widget)

pencere.bind('<Key>', klavye_girisi)  # Tüm sayı ve operatör tuşlarına izin verir

# Pencereyi çalıştırır
pencere.mainloop()

#Coder by EvinDelisi
