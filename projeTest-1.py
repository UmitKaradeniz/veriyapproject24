class Graf:
    def __init__(self):  
        self.graf = {}
    
    def sehir_ekle(self, sehir):
        if sehir not in self.graf:
            self.graf[sehir] = []
    
<<<<<<< HEAD
    def rota_ekle(self, sehir1, sehir2, mesafe):
        if sehir1 in self.graf and sehir2 in self.graf:
            self.graf[sehir1].append((sehir2, mesafe))
            self.graf[sehir2].append((sehir1, mesafe))
    
    def rota_bul(self, baslangic, varis):
        ziyaret_edilen = set()
        yigin = [(baslangic, [baslangic], 0)]
=======
    def add_route(self, city1, city2, distance):

        if city1 not in self.graph or city2 not in self.graph:
            raise ValueError("Her iki şehir de grafiğe eklenmiş olmalıdır.")
        self.graph[city1].append((city2, distance))
        self.graph[city2].append((city1, distance))
    
    def find_route(self, start, end):
        if start not in self.graph or end not in self.graph:
            raise ValueError("Hem başlangıç hem de hedef şehir grafikte bulunmalıdır.")
>>>>>>> e6740d9019b35450c0f7e4598de79bcedb408fa6
        
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
