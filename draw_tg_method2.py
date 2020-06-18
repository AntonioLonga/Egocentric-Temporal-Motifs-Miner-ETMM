import networkx as nx
import matplotlib.pyplot as plt
import numpy as np



# plot all graphs
def plot_all_graphs(res):
    for graphs in res:
        plot_3temporal_ego_graphs(graphs)
        print("************************************************************************************************************")


# plot graphs in an array
def plot_3temporal_ego_graphs(graphs_in):
    figure_per_row = 3
    splitted = []
    l = len(graphs_in)
    for i in np.arange(0,l,figure_per_row):
        tmp = graphs_in[i:(figure_per_row+i)]
        splitted.append(tmp)

    for graphs in splitted:
        plt.figure(figsize=(15,2))
        pos = dict()
        for j in range(len(graphs)):
            g = graphs[j]

            plt.subplot(1,figure_per_row,j+1)
            nodes = list(g.nodes())
            pos = dict()
            for i in nodes:
                n = i.split("_")[0]
                if(i.split("_")[1].split("*")[0] == "t0"):
                    x = np.random.rand()/4
                    pos[i] = [x,int(n)/100]

                elif(i.split("_")[1].split("*")[0] == "t1"):
                    x = np.random.rand()/4 + 1
                    pos[i] = [x,int(n)/100]

                elif(i.split("_")[1].split("*")[0] == "t2"):
                    x = np.random.rand()/4 +2
                    pos[i] = [x,int(n)/100]

                if (len(i.split("_")[1].split("*")) == 2):
                    ego = int(i.split("_")[0])
                    
            nx.draw(g,pos=pos,with_labels=True)
            nx.draw_networkx_nodes(g,pos=pos,
                                nodelist=[str(ego)+"_t0*",str(ego)+"_t1*",str(ego)+"_t2*"],
                                node_color='r',
                                node_size=900,
                                alpha=1)


        plt.show()


# draw a single graph
def plot_3temporal_ego_graph(H):
    nodes = list(H.nodes())
    pos = dict()
    for i in nodes:
        n = i.split("_")[0]
        if(i.split("_")[1].split("*")[0] == "t0"):
            x = np.random.rand()/4
            pos[i] = [x,int(n)/100]

        elif(i.split("_")[1].split("*")[0] == "t1"):
            x = np.random.rand()/4 + 1
            pos[i] = [x,int(n)/100]

        elif(i.split("_")[1].split("*")[0] == "t2"):
            x = np.random.rand()/4 +2
            pos[i] = [x,int(n)/100]

        if (len(i.split("_")[1].split("*")) == 2):
            ego = int(i.split("_")[0])
            
    nx.draw(H,pos=pos,with_labels=True)
    nx.draw_networkx_nodes(H,pos=pos,
                        nodelist=[str(ego)+"_t0*",str(ego)+"_t1*",str(ego)+"_t2*"],
                        node_color='r',
                        node_size=900,
                        alpha=1)
    plt.show()
