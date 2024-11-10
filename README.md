# Basit Makinesi

Bu proje, **Python** ve **tkinter** kütüphanesi kullanılarak geliştirilmiş, klavye ve fare girişlerini destekleyen, modern ve estetik bir tasarıma sahip bir hesap makinesidir. Hem klavye hem de fare ile etkileşime geçebilir, basma efektleriyle daha gerçekçi bir kullanım deneyimi yaşayabilirsiniz.

## Özellikler

- **Modern ve Estetik Tasarım:** Koyu tema ve canlı renklerle tasarlanmış şık bir arayüze sahiptir.
- **Klavyeden ve Fareden Giriş Desteği:** Sayı ve operatörleri klavyeden veya düğmelere tıklayarak girebilirsiniz.
- **Basma Efekti:** Düğmelere tıkladığınızda veya klavyeden tuşlara bastığınızda düğmeler üzerinde basma efekti oluşur.
- **Silme İşlevi:** `Backspace` tuşu ile ekrandaki son karakteri silebilirsiniz.
- **Temizleme İşlevi:** `C` düğmesine tıklayarak veya `Escape` tuşuna basarak ekranı temizleyebilirsiniz.
- **Hata Yönetimi:** Geçersiz işlemlerde kullanıcıya hata mesajı gösterilir.

## Gereksinimler

- **Python 3.x**
- **tkinter** kütüphanesi (Genellikle Python ile birlikte gelir. Eğer sisteminizde yüklü değilse aşağıdaki komutla yükleyebilirsiniz):
  ```bash
  # Windows için
  python -m pip install tk

  # macOS/Linux için
  sudo apt-get install python3-tk
  ```

## Kurulum ve Çalıştırma

1. **Kodun Kaydedilmesi:**

   Verilen kodu bir metin editörüne kopyalayın ve dosyayı `basit_calculator.py` adıyla kaydedin.

2. **Çalıştırma:**

   Terminal veya komut istemcisini açın ve dosyanın bulunduğu dizine gidin. Aşağıdaki komutu kullanarak programı başlatın:

   ```bash
   basit_calculator.py
   ```

## Kullanım Kılavuzu

- **Sayı ve Operatör Girişi:**
  - **Fare ile:** Düğmelere tıklayarak sayıları ve operatörleri girebilirsiniz.
  - **Klavyeden:** Klavyenizdeki sayı ve operatör tuşlarını kullanabilirsiniz.

- **İşlemi Hesaplama:**
  - `=` düğmesine tıklayarak veya `Enter` tuşuna basarak işlemin sonucunu görebilirsiniz.

- **Silme İşlemi:**
  - `Backspace` tuşuna basarak ekrandaki son karakteri silebilirsiniz.

- **Ekranı Temizleme:**
  - `C` düğmesine tıklayarak veya `Escape` tuşuna basarak ekranı tamamen temizleyebilirsiniz.

- **Basma Efektleri:**
  - Düğmelere tıkladığınızda veya klavyeden tuşlara bastığınızda ilgili düğme kısa süreliğine renk değiştirerek basma efekti verir.

## Kod Açıklaması

- **Fonksiyonlar:**
  - `hesapla(event=None)`: Ekrandaki matematiksel ifadeyi değerlendirir ve sonucu gösterir.
  - `ekrana_yaz(deger)`: Girilen değeri ekrana ekler.
  - `temizle(event=None)`: Ekrandaki tüm verileri siler.
  - `sil(event=None)`: Ekrandaki son karakteri siler.
  - `basma_efekti(buton)`: Düğmelere basıldığında geçici renk değişimi sağlar.
  - `klavye_girisi(event)`: Klavyeden yapılan girişleri yakalar ve ekrana yansıtır.

- **Arayüz Özellikleri:**
  - **Pencere Ayarları:** Sabit boyutlu ve yeniden boyutlandırılamayan bir pencere oluşturulur.
  - **Ekran Alanı:** Büyük ve okunaklı bir yazı tipiyle giriş ve sonuçların gösterildiği ekran oluşturulur.
  - **Düğmeler:** Sayılar ve operatörler için renkli ve stilize edilmiş düğmeler oluşturulur.
  - **Basma Efektleri:** Kullanıcı deneyimini artırmak için düğmelerde basma efektleri eklenmiştir.

- **Klavye Bağlantıları:**
  - `'<Return>'`: Enter tuşu ile hesaplama işlemi yapılır.
  - `'<Escape>'`: Escape tuşu ile ekran temizlenir.
  - `'<BackSpace>'`: Backspace tuşu ile son karakter silinir.
  - `'<Key>'`: Sayı ve operatör tuşları ile ekrana giriş yapılır.

## Örnek Ekran Görüntüsü

![Hesap Makinesi Görüntüsü](https://i.hizliresim.com/hbfcr2h.png)



## İletişim

Herhangi bir soru veya geri bildirim için [contact@beraatoztorun.com](mailto:contact@beraatoztorun.com) adresinden iletişime geçebilirsiniz.
