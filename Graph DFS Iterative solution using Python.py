class GraphNode(object):
    
    def __init__(self, val):
    
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
    
        self.children.append(new_node)
    
    def remove_child(self,del_node):
    
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    
    def __init__(self,node_list):
    
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
    
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
    
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


def dfs_search(root_node, search_value):
    
    stack = list()
    
    seen_elements = list()

    node = root_node

    node_value = node.value

    if node_value == search_value:
        return root_node

    seen_elements.append(node_value)

    stack.append(node_value)

    while len(stack) > 0:
        for node_next in node.children:  
            no_new_children = True

            if node_next.value not in seen_elements:
                node = node_next  
                node_value = node.value

                if node_value == search_value:  
                    return node

                seen_elements.append(node_value)
                stack.append(node_value)
                no_new_children = False
                break

        if no_new_children:  
            stack.pop()  
            for node_backwards in node.children:  
                if node_backwards.value is stack[len(stack) - 1]:
                    node = node_backwards
                    break

    return -1



nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)


if  nodeA == dfs_search(nodeS, 'A'):
    print("Pass")
else:
    print("Fail")

if  nodeS == dfs_search(nodeS, 'S'):
    print("Pass")
else:
    print("Fail")

if  nodeR == dfs_search(nodeS, 'R'):
    print("Pass")
else:
    print("Fail")
