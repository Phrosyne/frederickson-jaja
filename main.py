import networkx as nx

#Input. G (V, A) a complete directed graph with cost function c: A -> ℤ⁺, and
# G0 = (V,A') a subgraph of G.

def algorithm(G, links, root):
    H = G.copy() #this should be a copy of G but for the autocomplete suggestions we will mark this as a graph for now

#       1. For each edge 〈u, v〉 in A, let d〈u, v〉=0 if 〈v, u〉A' and let d〈u, v〉 = c〈v, u〉,
#       otherwise.


    for u, v in H.edges:
        H[u][v]['weight'] = 0

    for u, v, w in links:
        H.add_edge(u, v, weight=w)
        
    # 2. Find a minimum weight spanning arborescence T=(V,Aa') with root r element of V on (V, A) using d. Set Aa={〈u, v〉|〈v, u〉Aa'}.
        
    RSA = H.reverse(copy=True)
    
            #root shouldnt have any leaving edges so we can force that by making its leaving edge inf. even if it does have leaving edges for all intents and purposes they might as well not be there
    for u, v in list(RSA.out_edges(root)):
        RSA[u][v]['weight'] = float('inf')
    
    
    RSA = nx.minimum_spanning_arborescence(RSA, 'weight', True)

    rsaEdges = [(v, u) for u, v in RSA.edges()]
    
    print(f"Pass 1 (RSA) found: {rsaEdges}")

    for u, v in rsaEdges:
        if H.has_edge(v, u):
            H[u][v]['weight'] = 0
            
    for u, v in list(H.in_edges(root)):
        H[u][v]['weight'] = float('inf')

    sa = nx.minimum_spanning_arborescence(H, 'weight', 'weight', True)
        
    saEdges = list(sa.edges())

    print(f"Pass 2 (SA) found: {saEdges}")

    final_links = set(rsaEdges) | set(saEdges)
    tree_edges = set(G.edges())
    
    return final_links - tree_edges
    
    
    
# Create the Tree (Adjacency list of edges you already have)
G_tree = nx.DiGraph()
G_tree.add_edges_from([(0, 1), (1, 2)])

# Define Candidate Links (u, v, weight)
candidates = [
    (2, 0, 10),
    (2, 3, 5),
    (3, 0, 5),
    (0, 3, 20)
]

# Run your function
result = algorithm(G_tree, candidates, root=0)

print(f"Algorithm suggests buying: {result}")
# EXPECTED OUTPUT: {(3, 0), (2, 3)}