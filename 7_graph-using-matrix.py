nodes = []
graphs = []
node_count = 0

def add_node(v):
    global node_count
    if v in nodes:
        print(v,"present in nodes")
    else:
        node_count +=1
        nodes.append(v)
        for i in graphs:
            i.append(0)
        temp = []
        for j in range(node_count):
            temp.append(0)
        graphs.append(temp)

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"not present")
    elif v2 not in nodes:
        print(v2,"not present")
    else:
        index1= nodes.index(v1)
        index2= nodes.index(v2)
        graphs[index1][index2] = 1
        graphs[index2][index1] = 1

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"not presenet")
    else:
        index = nodes.index(v)
        nodes.pop(index)
        
        
        graphs.pop(index)
        for i in graphs:
            i.pop(index)
        node_count -=1
            
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"not present")
    elif v2 not in nodes:
        print(v2,"not present")
    else:
        index1= nodes.index(v1)
        index2= nodes.index(v2)
        graphs[index1][index2] = 0
        graphs[index2][index1] = 0
        
    
    
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graphs[i][j] ,end=" ")
        print()


add_node("A")
add_node("B")
add_node("C")

add_edge("A","B")
add_edge("A","C")
add_edge("A","A")
#delete_node("B")
delete_edge("A","B")
delete_edge("A","C")
print_graph()
