# ⚙️ Smart-Cycle: Sistem Mimarisi ve Donanım Listesi

Bu döküman, projenin fiziksel (donanım) katmanı ile yazılım (edge & cloud) katmanının birbirleriyle nasıl haberleştiğini detaylandırmaktadır.

## 🧰 Donanım Bileşenleri Tablosu (BOM - Bill of Materials)

| Bileşen (Komponent) | Tercih Edilen Model / Çip | Sistemdeki Görevi |
| :--- | :--- | :--- |
| **Edge AI İşlemci** | NVIDIA Jetson Nano 4GB | YOLOv8 modelini gecikmesiz (offline) çalıştırmak ve servo motorları sürmek. |
| **Görüntüleme Sensörü** | 8MP IMX219 (CSI Kamera) | Atıkların anlık RGB görüntülerini alıp işleme ünitesine aktarmak. |
| **Mesafe/Doluluk Sensörü** | HC-SR04 Ultrasonik Sensör | Konteynerin % doluluk oranını ölçerek büyük veri (Big Data) havuzuna yollamak. |
| **Fiziksel Ayrıştırıcılar** | MG996R Servo Motorlar | AI'dan gelen sonuca göre atığı doğru hazneye yönlendiren mekanizmayı hareket ettirmek. |
| **Haberleşme Modülü** | Quectel RM500Q-GL 5G/LTE | Sıkıştırılmış JSON veri paketlerini Turkcell Bulut sunucularına iletmek. |
| **Güç Yönetimi** | 5V 4A DC Power Supply & BMS | Tüm gömülü sistemin enerji optimizasyonunu sağlamak. |

---

## 📊 Sistem Akış Şeması (System Flow Diagram)

*Not: Aşağıdaki şema, atığın kutuya atıldığı andan itibaren donanım, yapay zeka ve bulut arasındaki veri akışını göstermektedir.*

```mermaid
graph TD
    A[Atık Atıldı] --> B[IMX219 Kamera RGB Görüntü Alır]
    A --> C[HC-SR04 Ultrasonik Sensör Doluluk Ölçer]
    
    B --> D{NVIDIA Jetson Nano<br>YOLOv8 İşleme}
    
    D -->|Sınıflandırma: Plastik| E[Servo Motor 1: Plastik Haznesini Aç]
    D -->|Sınıflandırma: Metal| F[Servo Motor 2: Metal Haznesini Aç]
    D -->|Sınıflandırma: Cam| G[Servo Motor 3: Cam Haznesini Aç]
    D -->|Sınıflandırma: Kağıt| H[Servo Motor 4: Kağıt Haznesini Aç]

    C --> I[Gömülü Sistem (Edge) JSON Veri Paketi Hazırlar]
    I --> J((Quectel 5G Modülü))
    
    J -->|MQTT/HTTPS| K[(Turkcell Bulut Sunucusu)]
    
    K --> L[Belediye Web Paneli<br>Rota Optimizasyonu]
    K --> M[Kullanıcı Mobil Uygulaması<br>Green-Coin Ödülü Ekle]
