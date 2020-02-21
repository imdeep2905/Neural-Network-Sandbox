import graphviz
from subprocess import check_call

# Thanks to
# https://github.com/martisak/dotnets/blob/master/dotnets.py
# https://tgmstat.wordpress.com/2013/06/12/draw-neural-network-diagrams-graphviz/

class NetworkDrawer:
    def __init__(self):
        pass
    
    def draw(self,layers=[1,1],weighted=False,weights=None):
        if weighted:
            pass #For future versions
        
        else:
            with open('network_graph.txt','w') as f:
                layers_str = ["Input"] + ["Hidden"] * (len(layers) - 2) + ["Output"]
                layers_col = ["none"] + ["none"] * (len(layers) - 2) + ["none"]
                layers_fill = ["black"] + ["gray"] * (len(layers) - 2) + ["black"]
                penwidth = 15
                font = "Sans 10"

                f.write("digraph G {")
                f.write("\tfontname = \"{}\"".format(font))
                f.write("\trankdir=LR")
                f.write("\tsplines=line")
                f.write("\tnodesep=.08;")
                f.write("\tranksep=1;")
                f.write("\tedge [color=black, arrowsize=.5];")
                f.write("\tnode [fixedsize=true,label=\"\",style=filled," + \
                    "color=none,fillcolor=gray,shape=circle]\n")

                # Clusters
                for i in range(0, len(layers)):
                    f.write(("\tsubgraph cluster_{} {{".format(i)))
                    f.write(("\t\tcolor={};".format(layers_col[i])))
                    f.write(("\t\tnode [style=filled, color=white, penwidth={},"
                        "fillcolor={} shape=circle];".format(
                            penwidth,
                            layers_fill[i])))

                    f.write(("\t\t"))

                    for a in range(layers[i]):
                        f.write("l{}{} ".format(i + 1, a))

                    f.write(";")
                    f.write(("\t\tlabel = {};".format(layers_str[i])))

                    f.write("\t}\n")

                # Nodes
                for i in range(1, len(layers)):
                    for a in range(layers[i - 1]):
                        for b in range(layers[i]):
                            f.write("\tl{}{} -> l{}{}".format(i, a, i + 1, b))

                f.write("}")
        
        #graphviz.Digraph(filename='network_graph.txt')
        check_call(['dot','-Tpng','network_graph.txt','-o','Network_Drawing.png'])