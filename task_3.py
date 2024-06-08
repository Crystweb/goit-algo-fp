# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу.
# Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших
# шляхів від початкової вершини до всіх інших.


import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, src, dest, weight):
        self.vertices[src].append((dest, weight))

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.vertices[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
if __name__ == "__main__":
    # Створення графа
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')

    # Додавання ребер
    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 3)
    graph.add_edge('C', 'D', 7)
    graph.add_edge('C', 'E', 8)
    graph.add_edge('D', 'E', 4)

    start_vertex = 'A'
    shortest_distances = dijkstra(graph, start_vertex)
    print("Найкоротші відстані від вершини", start_vertex + ":")
    for vertex, distance in shortest_distances.items():
        print("До вершини", vertex + ":", distance)
