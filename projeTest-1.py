class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_city(self, city):
        if city not in self.graph:
            self.graph[city] = []
    
    def add_route(self, city1, city2, distance):
        if city1 in self.graph and city2 in self.graph:
            self.graph[city1].append((city2, distance))
            self.graph[city2].append((city1, distance))
    
    def find_route(self, start, destination):
        visited = set()
        stack = [(start, [start], 0)]
        
        while stack:
            (city, path, total_distance) = stack.pop()
            if city not in visited:
                visited.add(city)
                
                for (neighbor, distance) in self.graph.get(city, []):
                    if neighbor == destination:
                        return path + [destination], total_distance + distance
                    else:
                        stack.append((neighbor, path + [neighbor], total_distance + distance))
        return None, None

g = Graph()

cities = input("Şehirleri virgülle ayırarak girin (örn. Istanbul, Ankara, Izmir): ").split(',')
for city in cities:
    g.add_city(city.strip())

num_routes = int(input("Kaç rota eklemek istersiniz? "))
for _ in range(num_routes):
    city1, city2, distance = input("Başlangıç şehri, varış şehri ve mesafeyi (örn. Istanbul, Ankara, 450) girin: ").split(',')
    g.add_route(city1.strip(), city2.strip(), int(distance.strip()))

start_city = input("Rota bulmak istediğiniz başlangıç şehri: ")
destination_city = input("Rota bulmak istediğiniz varış şehri: ")
route, distance = g.find_route(start_city, destination_city)
if route:
    print("Rota bulundu:", " -> ".join(route), f"Toplam Mesafe: {distance} km")
else:
    print("Rota bulunamadı.")

print("\nTüm Rotalar:")
for city, neighbors in g.graph.items():
    for (neighbor, distance) in neighbors:
        print(f"{city} - {neighbor}: {distance} km")
