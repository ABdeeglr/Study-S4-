# from pylab import *
# mpl.rcParams['font.sans-serif'] = ['文泉驿微米黑']
# 上述两行代码支持中文显示
# 尝试失败了，但这两行代码的目的应该是为了使用系统中的中文字体

import networkx as nx
import matplotlib.pyplot as plt
Graph = nx.Graph()
op = "Deep Learning"
# orogin point is written ba op

Booklist_1 = ["A Social History of Truth", "Liviathan And The Air-pump"]

Graph.add_node(op)
Graph.add_nodes_from(Booklist_1)
Graph.add_edge(op, Booklist_1[0])
Graph.add_edge(op, Booklist_1[1])

nx.draw(Graph, with_labels = True)
plt.show()