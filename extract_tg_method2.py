import networkx as nx
import numpy as np

# return an array of array type:
# [
#   [(GO12_1, ego),(GO12_2, ego),(GO12_3, ego), ...],
#   [(G123_1, ego),(G123_2, ego),(G123_3, ego), ....]
# ]
def extract_graphs(graphs):
    res = []
    for i in range(len(graphs)-2):
        g0 = graphs[i]
        g1 = graphs[i+1]
        g2 = graphs[i+2]
        ### at time t0 get nodes not isolated
        not_isolated_nodes = []
        for i in g0.nodes():
            if not(list(nx.neighbors(g0,i)) == []):
                not_isolated_nodes.append(i)
        three_times_graphs = []
        # for each non isolated node, build the temporal structure
        for node in not_isolated_nodes:
            G0,G1,G2 = build_3_static_graphs(g0,g1,g2,node)
            H = compose_graphs(G0,G1,G2,node)
            three_times_graphs.append(H)
        res.append(three_times_graphs)

    return(res)


def compose_graphs(G0,G1,G2,node):
    H = nx.compose_all([G0,G1,G2])
    nodes_G0 = [n[0:-3] for n in list(G0.nodes())]
    nodes_G1 = [n[0:-3] for n in list(G1.nodes())]
    nodes_G2 = [n[0:-3] for n in list(G2.nodes())]

    for n in nodes_G1:
        if (n in nodes_G0):
            H.add_edge(n+"_t0",n+"_t1")
    for n in nodes_G2:
        if (n in nodes_G1):
            H.add_edge(n+"_t1",n+"_t2")

    mapping = {str(node)+"_t0": str(node)+"_t0*",str(node)+"_t1": str(node)+"_t1*",str(node)+"_t2": str(node)+"_t2*"}
    H = nx.relabel_nodes(H, mapping)
    return(H)

def build_3_static_graphs(g0,g1,g2,node):
    ### build 3 static graphsdef plot_3temporal_ego_graph(H,node):
    G_0 = nx.Graph() 
    for n0 in list(nx.neighbors(g0,node)):
        ego = str(node)+"_t0"
        n0 = str(n0)+"_t0"
        G_0.add_edge(ego,n0)
    G_1 = nx.Graph()
    for n1 in list(nx.neighbors(g1,node)):
        ego = str(node)+"_t1"
        n1 = str(n1)+"_t1"
        G_1.add_edge(ego,n1)
    G_2 = nx.Graph()
    for n2 in list(nx.neighbors(g2,node)):
        ego = str(node)+"_t2"
        n2 = str(n2)+"_t2"
        G_2.add_edge(ego,n2)
        
    #### check graphs are not empty
    if(len(G_0)== 0):
        ego = str(node)+"_t0"
        G_0.add_node(ego)
    if(len(G_1)== 0):
        ego = str(node)+"_t1"
        G_1.add_node(ego)
    if(len(G_2)== 0):
        ego = str(node)+"_t2"
        G_2.add_node(ego)
    return (G_0,G_1,G_2)


