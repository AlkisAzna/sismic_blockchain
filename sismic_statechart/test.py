import networkx as nx
import matplotlib.pyplot as plt
from sismic.io import import_from_yaml

# Import statechart from YAML file
with open('blockchain_agriculture_statechart.yaml') as f:
    statechart = import_from_yaml(f)

# Create a NetworkX DiGraph
G = nx.DiGraph()

# Add states and transitions
for state in statechart.states:
    G.add_node(state)
for transition in statechart.transitions:
    G.add_edge(transition.source, transition.target)

# Visualize using Matplotlib
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

# Save the plot to a file
plt.savefig('statechart_plot.png')
