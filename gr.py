import pygame
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_edge('A', 'B', weight=4, color = 'blue')
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
nx.shortest_path(G, 'A', 'D', weight='weight')
print G['A']
nx.draw(G)
plt.savefig("mfs.png")
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.flip()
while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
