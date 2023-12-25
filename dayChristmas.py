#i cannot with cycles and graphs and how many cyclic graphs...thanks hyper neutrino!
#hyper uses a library to solve these networks 
#sudo pip3 install networkx

import networkx as nx

g = nx.Graph() # new graph

for line in open('christmas.txt'):
  #add edges to the graph 
  left, right = line.split(":")
  #each edge
  for node in right.strip().split():
    g.add_edge(left, node)

#find graph with two components, using 3 edges (find min edges to separate graph into two components)
#this is called min edge cut

g.remove_edges_from(nx.minimum_edge_cut(g))
component1, component2 = nx.connected_components(g)
#part1
print(len(component1) * len(component2))
