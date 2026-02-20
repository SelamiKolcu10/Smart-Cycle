import customtkinter as ctk

# --- UYGULAMA TEMA VE PENCERE AYARLARI ---
ctk.set_appearance_mode("dark")  # Koyu tema
ctk.set_default_color_theme("green")  # Yeşil renk paleti (Smart-Cycle konsepti)

# Ana pencereyi oluştur
app = ctk.CTk()
app.geometry("400x550")
app.title("Smart-Cycle | Masaüstü Uygulaması")
app.resizable(False, False) # Boyutu sabit tut

# --- GLOBAL DEĞİŞKENLER ---
puan = 150  # Başlangıç puanı

# --- FONKSİYONLAR ---
def guncelle_puan():
    lbl_puan.configure(text=f"Mevcut Puan: {puan} GC")

def atik_at(tur, kazanilan):
    global puan
    puan += kazanilan
    guncelle_puan()
    lbl_durum.configure(text=f"✅ {tur} algılandı! +{kazanilan} GC eklendi.", text_color="#2ecc71")

def odul_al():
    global puan
    if puan >= 300:
        puan -= 300
        guncelle_puan()
        lbl_durum.configure(text="🎉 Tebrikler! 1 GB İnternet Hattınıza Yüklendi!", text_color="#f1c40f")
    else:
        eksik = 300 - puan
        lbl_durum.configure(text=f"❌ Yetersiz Puan! {eksik} GC daha lazım.", text_color="#e74c3c")

# --- ARAYÜZ (UI) TASARIMI ---

# 1. Başlık ve Profil
lbl_baslik = ctk.CTkLabel(app, text="♻️ Smart-Cycle Green-Coin", font=("Arial", 22, "bold"))
lbl_baslik.pack(pady=(20, 5))

lbl_isim = ctk.CTkLabel(app, text="👤 Kullanıcı: Selami Kolcu", font=("Arial", 14))
lbl_isim.pack(pady=0)

lbl_puan = ctk.CTkLabel(app, text=f"Mevcut Puan: {puan} GC", font=("Arial", 20, "bold"), text_color="#2ecc71")
lbl_puan.pack(pady=(10, 20))

# 2. Atık Atma Bölümü (Çerçeve içinde)
frame_atik = ctk.CTkFrame(app, corner_radius=10)
frame_atik.pack(pady=10, padx=20, fill="x")

lbl_alt_baslik = ctk.CTkLabel(frame_atik, text="🗑️ Kameraya Atık Göster (Simülasyon)", font=("Arial", 14, "bold"))
lbl_alt_baslik.pack(pady=10)

btn_plastik = ctk.CTkButton(frame_atik, text="🧴 Plastik Şişe (+50 Puan)", height=40, 
                            command=lambda: atik_at("Plastik Şişe", 50))
btn_plastik.pack(pady=(0, 10), padx=20, fill="x")

btn_metal = ctk.CTkButton(frame_atik, text="🥫 Metal Kutu (+75 Puan)", height=40, 
                          command=lambda: atik_at("Metal Kutu", 75))
btn_metal.pack(pady=(0, 15), padx=20, fill="x")

# 3. Ödül Marketi Bölümü (Çerçeve içinde)
frame_odul = ctk.CTkFrame(app, corner_radius=10)
frame_odul.pack(pady=10, padx=20, fill="x")

lbl_odul = ctk.CTkLabel(frame_odul, text="🎁 Turkcell Ödül Marketi", font=("Arial", 14, "bold"))
lbl_odul.pack(pady=10)

btn_odul = ctk.CTkButton(frame_odul, text="🚀 1 GB İnternet Al (300 GC)", fg_color="#d35400", hover_color="#e67e22", height=40, command=odul_al)
btn_odul.pack(pady=(0, 15), padx=20, fill="x")

# 4. Durum Bildirim Alanı (En alt)
lbl_durum = ctk.CTkLabel(app, text="Sistem Hazır. Atık bekleniyor...", font=("Arial", 13))
lbl_durum.pack(pady=(20, 0))

# Uygulamayı sürekli açık tutan döngü
app.mainloop()
