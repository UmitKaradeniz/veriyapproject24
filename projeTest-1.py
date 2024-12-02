class Graf:
    def __init__(self):  
        self.graf = {}
    
    def sehir_ekle(self, sehir):
        if sehir not in self.graf:
            self.graf[sehir] = []
    
    def rota_ekle(self, sehir1, sehir2, mesafe):
        if sehir1 in self.graf and sehir2 in self.graf:
            self.graf[sehir1].append((sehir2, mesafe))
            self.graf[sehir2].append((sehir1, mesafe))
    
    def rota_bul(self, baslangic, varis):
        ziyaret_edilen = set()
        yigin = [(baslangic, [baslangic], 0)]
        
        while yigin:
            (sehir, yol, toplam_mesafe) = yigin.pop()
            if sehir not in ziyaret_edilen:
                ziyaret_edilen.add(sehir)
                
                for (komsu, mesafe) in self.graf.get(sehir, []):
                    if komsu == varis:
                        return yol + [varis], toplam_mesafe + mesafe
                    else:
                        yigin.append((komsu, yol + [komsu], toplam_mesafe + mesafe))
        return None, None

g = Graf()

sehirler = input("Şehirleri virgülle ayırarak girin (örn. Istanbul, Ankara, Izmir): ").split(',')
for sehir in sehirler:
    g.sehir_ekle(sehir.strip())

num_rota = int(input("Kaç rota eklemek istersiniz? "))
for _ in range(num_rota):
    try:
        sehir1, sehir2, mesafe = input("Başlangıç şehri, varış şehri ve mesafeyi (örn. Istanbul, Ankara, 450) girin: ").split(',')
        g.rota_ekle(sehir1.strip(), sehir2.strip(), int(mesafe.strip()))
    except ValueError:
        print("Hatalı giriş! Başlangıç şehri, varış şehri ve mesafeyi doğru formatta girin.")

baslangic_sehri = input("Rota bulmak istediğiniz başlangıç şehri: ").strip()
varis_sehri = input("Rota bulmak istediğiniz varış şehri: ").strip()
rota, mesafe = g.rota_bul(baslangic_sehri, varis_sehri)
if rota:
    print("Rota bulundu:", " -> ".join(rota), f"Toplam Mesafe: {mesafe} km")
else:
    print("Rota bulunamadı.")

print("\nTüm Rotalar:")
for sehir, komsular in g.graf.items():
    for (komsu, mesafe) in komsular:
        print(f"{sehir} - {komsu}: {mesafe} km")
