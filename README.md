# Sistem Panosu Uygulaması

Bu proje, Ubuntu sisteminde CPU, RAM ve disk kullanımını izleyen ve bu verileri bir PostgreSQL veritabanına kaydeden bir Python uygulaması içerir. Veriler, bir Streamlit uygulaması aracılığıyla görselleştirilir.

## Proje Bileşenleri

1. **`main.py`**: Sistem kaynaklarını izler ve PostgreSQL veritabanına kaydeder.
2. **`app.py`**: Streamlit kullanarak verileri görselleştirir.
3. **`requirements.txt`**: Projeyi çalıştırmak için gerekli Python kütüphanelerini listeler.

## Başlangıç

### Gereksinimler

- Python 3.x
- PostgreSQL veritabanı
- Gerekli Python kütüphaneleri

### Kurulum

1. **Python Kütüphanelerini Yükleyin:**

   ```bash
   pip install -r requirements.txt

2.  **PostgreSQL Veritabanını Ayarlayın:**

Veritabanı bağlantı bilgilerini ve yapılandırmasını main.py dosyasında güncelleyin.


3. **Sistem Verilerini Toplamaya Başlayın:**

   ```bash
   python main.py


4. **Streamlit Uygulamasını Çalıştırın:**


   ```bash
   streamlit run app.py

### Kullanım

Sistem Bilgisi Panosu: Streamlit uygulamasında CPU, RAM ve disk kullanım verilerini görselleştirir. Ayrıca, en güncel veriler tablo halinde görüntülenir.

### Kod Yapısı
#### main.py
##### Fonksiyonlar:
    get_system_info(): Sistem bilgilerini toplar.
    create_table(): Veritabanında tablo oluşturur.
    insert_data(info): Toplanan verileri veritabanına ekler.
    start_collecting(interval): Verileri belirli aralıklarla toplar.

#### app.py
##### Fonksiyonlar:
    get_data_from_postgres(): Veritabanından veri çeker.
    Streamlit bileşenleri kullanarak verileri görselleştirir (tablo, grafikler).

    