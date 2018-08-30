
# coding: utf-8

# In[1]:


#Read the csv file and store it as a dictonary

with open('nodes.csv', "r") as f:
    lines = f.readlines()
Edge_graph = {}
Val_graph = {}
previous_num = -1
for line in lines:
    node1 = line.split(",")[0].strip()[1:-1]
    node2 = line.split(",")[1].strip()[1:-1]
    node1_num = int(node1.split(":")[0])
    node1_val = int(node1.split(":")[1])
    node2_num = int(node2.split(":")[0])
    node2_val = int(node2.split(":")[1])
    Val_graph[node1_num] = node1_val
    Val_graph[node2_num] = node2_val
    if node1_num == previous_num:
        Edge_graph[node1_num] = Edge_graph[node1_num]+[node2_num]
    else:
        Edge_graph[node1_num] = [node2_num]
    previous_num = node1_num


# In[2]:


# Raising the resusion limit to a big number
import sys
sys.setrecursionlimit(50000)

# Define the function recursive BFS
def recursive_BFS(graph,queue,seen,min_val,min_node):
    if (len(queue)!=0):
        node = queue.pop(0)
        if min_val>Val_graph[node]:
            min_val = Val_graph[node]
            min_node = node
        else:
            min_val = min_val
            #min_node = min_node
        seen.add(node)
        if node not in graph.keys():
            neighbors = []
        else:
            neighbors = graph[node]
        for w in neighbors:
            if (w not in seen) & (w not in queue):
                queue.append(w)
        recursive_BFS(graph,queue,seen,min_val,min_node)
    else:
        print "Node %d has smallest number value %d\n" %(min_node,min_val)

# Initialize some variables in the function
queue = []
queue.append(Edge_graph.keys()[0])
seen = set()
min_val = 'Inf'
min_node = 0

# Call function
recursive_BFS(Edge_graph,queue,seen,min_val,min_node)

