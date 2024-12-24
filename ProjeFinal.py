import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import heapq  # Dijkstra algoritması için öncelik kuyruğu
import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self, yonlu=True):
        self.graf = {}
        self.yonlu = yonlu

    def sehir_ekle(self, sehir):
        self.graf.setdefault(sehir, [])

    def rota_ekle(self, sehir1, sehir2, mesafe):
        self.graf[sehir1].append((sehir2, mesafe))
        if not self.yonlu:
            self.graf[sehir2].append((sehir1, mesafe))

    def rota_bul(self, baslangic, varis):
        ziyaret_edilen = set()
        yigin = [(baslangic, [baslangic], 0)]

        while yigin:
            sehir, yol, toplam_mesafe = yigin.pop()
            if sehir not in ziyaret_edilen:
                ziyaret_edilen.add(sehir)
                for komsu, mesafe in self.graf.get(sehir, []):
                    if komsu == varis:
                        return yol + [varis], toplam_mesafe + mesafe
                    yigin.append((komsu, yol + [komsu], toplam_mesafe + mesafe))
        return None, None

    def en_kisa_yol(self, baslangic, varis):
        mesafeler = {sehir: float('inf') for sehir in self.graf}
        mesafeler[baslangic] = 0
        pq = [(0, baslangic)]
        onceki = {}

        while pq:
            mevcut_mesafe, mevcut_sehir = heapq.heappop(pq)

            if mevcut_sehir == varis:
                yol = []
                while mevcut_sehir:
                    yol.insert(0, mevcut_sehir)
                    mevcut_sehir = onceki.get(mevcut_sehir)
                return yol, mesafeler[varis]

            for komsu, mesafe in self.graf.get(mevcut_sehir, []):
                yeni_mesafe = mevcut_mesafe + mesafe
                if yeni_mesafe < mesafeler[komsu]:
                    mesafeler[komsu] = yeni_mesafe
                    onceki[komsu] = mevcut_sehir
                    heapq.heappush(pq, (yeni_mesafe, komsu))

        return None, None

    def grafi_gorsellestir(self):
        G = nx.DiGraph() if self.yonlu else nx.Graph()

        for sehir, komsular in self.graf.items():
            for komsu, mesafe in komsular:
                G.add_edge(sehir, komsu, weight=mesafe)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

def ekle(giris, islem, mesaj):
    veri = giris.get().strip()
    if veri:
        islem(veri)
        messagebox.showinfo("Başarılı", mesaj.format(veri))
        giris.delete(0, tk.END)
    else:
        messagebox.showerror("Hata", "Boş giriş yapılamaz!")

def sehir_ekle():
    ekle(sehir_giris, g.sehir_ekle, "{} şehri eklendi.")

def rota_ekle():
    try:
        sehir1, sehir2 = sehir1_giris.get().strip(), sehir2_giris.get().strip()
        mesafe = int(mesafe_giris.get().strip())
        g.rota_ekle(sehir1, sehir2, mesafe)
        messagebox.showinfo("Başarılı", f"Rota eklendi: {sehir1} - {sehir2}, {mesafe} km")
        sehir1_giris.delete(0, tk.END)
        sehir2_giris.delete(0, tk.END)
        mesafe_giris.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Mesafe sayısal olmalıdır!")

def rota_bul():
    rota, mesafe = g.rota_bul(baslangic_giris.get().strip(), varis_giris.get().strip())
    if rota:
        sonuc_label.config(text=f"Rota: {' -> '.join(rota)}, Toplam Mesafe: {mesafe} km")
    else:
        messagebox.showinfo("Sonuç", "Rota bulunamadı.")

def kisa_rota_bul():
    rota, mesafe = g.en_kisa_yol(baslangic_giris.get().strip(), varis_giris.get().strip())
    if rota:
        sonuc_label.config(text=f"En Kısa Rota: {' -> '.join(rota)}, Toplam Mesafe: {mesafe} km")
    else:
        messagebox.showinfo("Sonuç", "En kısa rota bulunamadı.")

def grafi_goster():
    g.grafi_gorsellestir()

def tum_rotalari_goster():
    rotalar = "\n".join(
        f"{sehir} - {komsu}: {mesafe} km"
        for sehir, komsular in g.graf.items()
        for komsu, mesafe in komsular
    )
    tum_rotalar_text.delete(1.0, tk.END)
    tum_rotalar_text.insert(tk.END, rotalar)

g = Graf()

root = tk.Tk()
root.title("Graf Rota Yönetimi Uygulaması")
root.geometry("500x700")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

sehir_giris = ttk.Entry(frame, width=30)
sehir_giris.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(frame, text="Şehir Ekle:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
ttk.Button(frame, text="Ekle", command=sehir_ekle).grid(row=0, column=2, padx=5, pady=5)

sehir1_giris, sehir2_giris, mesafe_giris = (ttk.Entry(frame, width=30) for _ in range(3))
for i, text in enumerate(["Başlangıç Şehri:", "Varış Şehri:", "Mesafe (km):"]):
    ttk.Label(frame, text=text).grid(row=i+1, column=0, padx=5, pady=5, sticky="e")
    [sehir1_giris, sehir2_giris, mesafe_giris][i].grid(row=i+1, column=1, padx=5, pady=5)
ttk.Button(frame, text="Rota Ekle", command=rota_ekle).grid(row=4, column=1, pady=10)

baslangic_giris, varis_giris = ttk.Entry(frame, width=30), ttk.Entry(frame, width=30)
for i, text in enumerate(["Başlangıç Şehri:", "Varış Şehri:"]):
    ttk.Label(frame, text=text).grid(row=i+5, column=0, padx=5, pady=5, sticky="e")
    [baslangic_giris, varis_giris][i].grid(row=i+5, column=1, padx=5, pady=5)
ttk.Button(frame, text="Rota Bul", command=rota_bul).grid(row=7, column=1, pady=10)
ttk.Button(frame, text="En Kısa Rotayı Bul", command=kisa_rota_bul).grid(row=8, column=1, pady=10)
ttk.Button(frame, text="Grafi Görselleştir", command=grafi_goster).grid(row=10, column=1, pady=10)

sonuc_label = ttk.Label(frame, text="", foreground="blue")
sonuc_label.grid(row=11, column=0, columnspan=3)

ttk.Button(frame, text="Tüm Rotaları Göster", command=tum_rotalari_goster).grid(row=12, column=1, pady=10)

tum_rotalar_text = tk.Text(frame, width=60, height=10, wrap="word")
tum_rotalar_text.grid(row=13, column=0, columnspan=3, pady=10)

root.mainloop()
