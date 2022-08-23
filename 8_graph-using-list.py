def add_node(v):
    if v in graph:
        print(v,"present in graph")
    else:
        graph[v] = []

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"not present in grapg")
    elif v1 not in graph:
        print(v2,"not present in grapg")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def delete_node(v):
    if v not in graph:
        print(v,"not resent in graph")
    else:
        
        for i in graph:
            lst1 = graph[i]
            if v in lst1:
                lst1.remove(v)
            
        graph.pop(v)

def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"not present in grapg")
    elif v1 not in graph:
        print(v2,"not present in grapg")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

def DFS(node,visited,graph):
    if node not in graph:
        print("node not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
              
def DFSiterative(node,graph):
    visited= set()
    if node not in graph:
        print("node not present")
    else:
        stack = []
        stack.append(node)
        while stack:
            curr = stack.pop()
            if curr not in visited:
                print(curr)
                visited.add(curr)
                for i in graph[curr]:
                    stack.append(i)

            
        
        
    
visited =set()
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_edge("A","C")
add_edge("A","B")
add_edge("B","C")
DFSiterative("C",graph)
#delete_node("A")
#print(graph)
#DFS("B",visited,graph)
