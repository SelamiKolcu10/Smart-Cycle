import time
import random
import json

def measure_distance():
    # Jetson Nano GPIO üzerinden HC-SR04 ultrasonik sensör okuması (Simülasyon: 0-100 cm)
    return random.uniform(5.0, 95.0)

def calculate_fullness(distance, bin_height=100.0):
    # Boşluk mesafesini % doluluk oranına çevir
    fullness = max(0, min(100, 100 - (distance / bin_height * 100)))
    return round(fullness, 2)

def send_data_to_cloud(sensor_data):
    # Turkcell 5G/LTE modülü üzerinden buluta JSON verisi basma simülasyonu
    payload = json.dumps(sensor_data)
    print(f"[IoT Modülü 5G] Veri Buluta İletiliyor: {payload}")
    # Gerçek projede aktif edilecek kısım: 
    # requests.post('http://api.smart-cycle.com/iot-data', json=sensor_data)

print("--- Smart-Cycle IoT Sensör Node Başlatıldı ---")
try:
    while True:
        dist = measure_distance()
        doluluk = calculate_fullness(dist)
        
        # Büyük Veri (Big Data) ve Rota Optimizasyonu için hazırlanmış veri paketi
        veri_paketi = {
            "cihaz_id": "JETSON_NANO_KAMPUS_01",
            "doluluk_orani_yuzde": doluluk,
            "batarya_durumu_yuzde": 88,
            "zaman_damgasi": time.time()
        }
        
        send_data_to_cloud(veri_paketi)
        
        if doluluk > 80.0:
            print("⚠️ UYARI: Konteyner eşik değerini aştı! Çöp toplama rotasına acil eklendi.\n")
        
        time.sleep(3) # 3 saniyede bir veri gönder
except KeyboardInterrupt:
    print("IoT Sistemi durduruldu.")
