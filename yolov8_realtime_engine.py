# Smart-Cycle Uç Cihaz (Edge Computing) Gerçek Zamanlı AI Ayrıştırma Motoru
from ultralytics import YOLO
import cv2

def run_ai_sorter():
    print("[SİSTEM] YOLOv8 Yapay Zeka Modeli Yükleniyor...")
    
    # Kendi eğittiğimiz (Plastik, Metal, Cam, Kağıt) model dosyası (Prototip için yolov8n kullanılmıştır)
    # Gelecekte 'smart_cycle_best.pt' olarak güncellenecektir.
    model = YOLO('yolov8n.pt') 
    
    # Jetson Nano CSI Kamera veya USB WebCam başlat (Port 0)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[HATA] Kamera başlatılamadı. Donanım bağlantılarını kontrol edin.")
        return

    print("[SİSTEM] Kamera aktif. Nesne tespiti başlatıldı. Çıkmak için 'q' tuşuna basın.")
    
    while cap.isOpened():
        success, frame = cap.read()
        if success:
            # Görüntüyü YOLOv8 modeline sok ve %75 doğruluk eşiği altındakileri yoksay
            results = model(frame, conf=0.75) 
            
            # Sınır kutularını (Bounding Box) görüntünün üzerine otomatik çiz
            annotated_frame = results[0].plot()
            
            # TODO: Tespit edilen nesne (results) 'Plastik' ise servo motor_1'i tetikle
            # TODO: Tespit edilen nesne 'Metal' ise servo motor_2'yi tetikle
            
            # Ekranda izleme penceresi
            cv2.imshow("Smart-Cycle AI Sorter", annotated_frame)
            
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_ai_sorter()
