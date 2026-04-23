import networkx as nx

#Input. G (V, A) a complete directed graph with cost function c: A -> ℤ⁺, and
# G0 = (V,A') a subgraph of G.

def algorithm(G, links, root):
    H = nx.DiGraph() #this should be a copy of G but we'll leave it like this for the autocomplete
    H.add_nodes_from(G.nodes())

    """
    1. For each edge 〈u, v〉 in A, let d〈u, v〉=0 if 〈v, u〉A' and let d〈u, v〉 = c〈v, u〉,
    otherwise.

    """
    
    for u, v in G.edges():
        if u != root and v != root:
            H.add_edge(u, v, weight=0)

    for u, v, w in links:
        H.add_edge(u, v, weight=w)

        """
        2. Find a minimum weight spanning arborescence T=(V,Aa') with root rV on (V, A) using d. Set Aa={〈u, v〉|〈v, u〉Aa'}.

        """

    RSA = nx.minimum_spanning_arborescence(H.reverse(copy=True), attr='weight')
    
    rsaEdges = [(v, u) for u, v in RSA.edges()]
    print(f"Pass 1 (RSA) found: {rsaEdges}")

    # SA = nx.DiGraph()

    SA = G.copy()
    SA.add_edges_from(rsaEdges)
        
    """
    3. For each edge 〈u, v〉 in A, let d'〈u, v〉 = c〈u, v〉. If 〈u, v〉A'Aa, then set d'〈u, v〉=0. For all u, set d'〈u, r〉=∞.

    """
    for u, v, w in links:
        if not SA.has_edge(u, v):
            SA.add_edge(u, v, weight=w)

    for u, v in list(SA.in_edges(root)):
        SA[u][v]['weight'] = float('inf')

    """
    4. Find a minimum weight spanning arborescence T'=(V, Ab) on (V, A) using d'.

    """

    SA = nx.minimum_spanning_arborescence(SA, attr='weight')
    saEdges = list(SA.edges())
    print(f"Pass 2 (SA) found: {saEdges}")

    """
    5. Set A''=(Aa U Ab)-A'.
    """
    # final union - original
    return (set(rsaEdges) | set(saEdges)) - set(G.edges())
    
    
    
G = nx.DiGraph()
G.add_edges_from([(0, 1), (0, 2)])

candidates = [
    (1, 0, 50),
    (2, 0, 50),
    (1, 2, 5),
    (2, 0, 10),
]

result = algorithm(G, candidates, root=0)
print(f"Algorithm suggests buying: {result}")