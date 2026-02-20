import customtkinter as ctk
import webbrowser

# --- AYARLAR ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class BelediyePaneli(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart-Cycle | Bursa Nilüfer Operasyon Merkezi")
        self.geometry("650x550")

        # --- BAŞLIK ---
        lbl_baslik = ctk.CTkLabel(self, text="🗺️ Nilüfer Belediyesi Canlı Atık Takibi", font=("Arial", 22, "bold"))
        lbl_baslik.pack(pady=20)

        # --- KONTEYNER LİSTESİ ---
        self.frame_veriler = ctk.CTkFrame(self)
        self.frame_veriler.pack(pady=10, padx=20, fill="both", expand=True)

        # Bursa Nilüfer Stratejik Noktaları
        self.konteyner_olustur("Görükle Yerleşkesi (Kampüs)", "85%", "Kritik", "#e74c3c")
        self.konteyner_olustur("İhsaniye Meydanı (Merkez)", "40%", "Normal", "#2ecc71")
        self.konteyner_olustur("Özlüce Metro İstasyonu", "95%", "Dolu", "#e74c3c")
        self.konteyner_olustur("Nilüfer Belediye Hizmet Binası", "15%", "Boş", "#3498db")

        # --- HARİTA VE ROTA BUTONLARI ---
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=20)

        btn_harita = ctk.CTkButton(btn_frame, text="📍 Konteynırları Haritada Gör", 
                                       fg_color="#d35400", hover_color="#e67e22",
                                       command=self.haritayi_ac)
        btn_harita.pack(side="left", padx=10)

        self.btn_rota = ctk.CTkButton(btn_frame, text="🚚 Optimize Rota Oluştur", 
                                     fg_color="#27ae60", hover_color="#2ecc71",
                                     command=self.rota_hesapla)
        self.btn_rota.pack(side="left", padx=10)

    def konteyner_olustur(self, lokasyon, doluluk, durum, renk):
        row = ctk.CTkFrame(self.frame_veriler, fg_color="#2c3e50")
        row.pack(pady=3, padx=10, fill="x")
        ctk.CTkLabel(row, text=lokasyon, width=250, anchor="w").pack(side="left", padx=10)
        ctk.CTkLabel(row, text=doluluk, width=100).pack(side="left")
        ctk.CTkLabel(row, text=durum, text_color=renk, font=("Arial", 12, "bold")).pack(side="right", padx=10)

    def haritayi_ac(self):
        # Belediye Binası Merkezli Görünüm
        url = "https://www.google.com/maps/dir/Nilüfer+Belediyesi/İhsaniye+Meydanı/Özlüce+Metro/Görükle"
        webbrowser.open(url)

    def rota_hesapla(self):
        # BAŞLANGIÇ: Nilüfer Belediyesi
        # DURAK 1: Özlüce (En dolu konteyner)
        # VARIŞ: Görükle (Kritik konteyner)
        rota_url = "https://www.google.com/maps/dir/Nil%C3%BCfer+Belediyesi,+%C4%B0hsaniye,+Ahmet+Vefik+Pa%C5%9Fa+Caddesi+No:21,+Ni%CC%87l%C3%BCfer%2FBursa,+T%C3%BCrkiye/%C3%96zl%C3%BCce+%2F+29+Ekim+Metro+%C4%B0stasyonu,+29+Ekim,+U%C4%9Fur+Mumcu+Bulvar%C4%B1+25a,+Ni%CC%87l%C3%BCfer%2FBursa,+T%C3%BCrkiye/G%C3%B6r%C3%BCkle,+Nil%C3%BCfer%2FBursa,+T%C3%BCrkiye/data=!4m20!4m19!1m5!1m1!19sChIJNzg9OyUUyhQRGqFlUKEuikU!2m2!1d28.985695999999997!2d40.2169612!1m5!1m1!19sChIJhTWBufcRyhQRtJgKdOelx0U!2m2!1d28.9122314!2d40.2203413!1m5!1m1!19sChIJTSeuaBQOyhQR8umaE_Yj5KY!2m2!1d28.837971399999997!2d40.232330399999995!3e0"
        webbrowser.open(rota_url)
        self.btn_rota.configure(text="✅ Rota İletildi", fg_color="#16a085")
        print("[SİSTEM] Belediye binasından başlayan optimize rota araçlara iletildi.")

if __name__ == "__main__":
    app = BelediyePaneli()
    app.mainloop()
