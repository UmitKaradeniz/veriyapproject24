class Graph:
    def __init__(self):  
        self.graph = {}
    
    def add_city(self, city):
        if city not in self.graph:
            self.graph[city] = []
    
    def add_route(self, city1, city2, distance):

        if city1 not in self.graph or city2 not in self.graph:
            raise ValueError("Her iki şehir de grafiğe eklenmiş olmalıdır.")
        self.graph[city1].append((city2, distance))
        self.graph[city2].append((city1, distance))
    
    def find_route(self, start, end):
        if start not in self.graph or end not in self.graph:
            raise ValueError("Hem başlangıç hem de hedef şehir grafikte bulunmalıdır.")
        
        visited = set()
        stack = [(start, [start])]
        
        while stack:
            (city, path) = stack.pop()
            if city not in visited:
                visited.add(city)
                
                for (neighbor, _) in self.graph.get(city, []):
                    if neighbor == end:
                        return path + [end]
                    else:
                        stack.append((neighbor, path + [neighbor]))
        return None


g = Graph()
g.add_city("Istanbul")
g.add_city("Ankara")
g.add_city("Izmir")
g.add_city("Bursa")


g.add_route("Istanbul", "Ankara", 450)
g.add_route("Istanbul", "Bursa", 150)
g.add_route("Bursa", "Izmir", 300)


route = g.find_route("Istanbul", "Izmir")
if route:
    print("Rota bulundu:", " -> ".join(route))
else:
    print("Rota bulunamadı.")
