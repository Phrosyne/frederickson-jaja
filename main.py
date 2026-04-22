import networkx as nx

#Input. G (V, A) a complete directed graph with cost function c: A -> ℤ⁺, and
# G0 = (V,A') a subgraph of G.

def algorithm(G, links, root):
    H = nx.Graph() #this should be a copy of G but for the autocomplete suggestions we will mark this as a graph for now

#       1. For each edge 〈u, v〉 in A, let d〈u, v〉=0 if 〈v, u〉A' and let d〈u, v〉 = c〈v, u〉,
#       otherwise.


    for u, v in H.edges:
        H[u][v]['weight'] = 0

    for u, v, w in links:
        H.add_edge(u, v, weight=w)