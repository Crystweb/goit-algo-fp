# Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує
# обходи дерева: у глибину та в ширину.

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, Normalize
from matplotlib.cm import ScalarMappable, viridis


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def add(self, key):
        self.heap.append(Node(key))
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].val > self.heap[parent_index].val:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def build_tree(self):
        if not self.heap:
            return None

        nodes = [None] * len(self.heap)
        for i, node in enumerate(self.heap):
            nodes[i] = node

        for i in range(len(nodes) // 2):
            if 2 * i + 1 < len(nodes):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                nodes[i].right = nodes[2 * i + 2]

        return nodes[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, visited_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    if visited_nodes:
        for step, node in enumerate(visited_nodes):
            tree.nodes[node.id]['color'] = node.color
            colors = [node[1]['color'] for node in tree.nodes(data=True)]
            plt.figure(figsize=(8, 5))
            nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
            plt.title(f"Step {step+1}")
            plt.show()
    else:
        plt.show()


def assign_colors(nodes):
    cmap = viridis
    norm = Normalize(vmin=0, vmax=len(nodes)-1)
    sm = ScalarMappable(cmap=cmap, norm=norm)
    for i, node in enumerate(nodes):
        node.color = to_hex(sm.to_rgba(i))
    return nodes


def dfs(tree_root):
    stack = [tree_root]
    visited_nodes = []
    while stack:
        node = stack.pop()
        if node not in visited_nodes:
            visited_nodes.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return assign_colors(visited_nodes)


def bfs(tree_root):
    queue = [tree_root]
    visited_nodes = []
    while queue:
        node = queue.pop(0)
        if node not in visited_nodes:
            visited_nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return assign_colors(visited_nodes)


# Створення бінарної купи та додавання елементів
heap = BinaryHeap()
elements = [10, 4, 9, 1, 7, 5, 3]
for el in elements:
    heap.add(el)

# Побудова дерева з купи та його візуалізація
root = heap.build_tree()

# Обхід в глибину
dfs_visited = dfs(root)
draw_tree(root, dfs_visited)

# Обхід в ширину
bfs_visited = bfs(root)
draw_tree(root, bfs_visited)
