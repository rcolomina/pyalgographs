
class DGraph:
    def __init__(self,nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def add_node(self,node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self,node_x,node_y):
        # find whether it is already there
        new_edge = [node_x,node_y]
        if  new_edge not in self.edges:
            self.edges.append(new_edge)


    def __str__(self):
        snodes = [str(node) for node in self.nodes]
        sedges = [str(edge[0])+"->"+str(edge[1]) for edge in self.edges]
        return "Nodes:" + "-".join(snodes) + " Edges:" + ":".join(sedges)


    def get_neighbours(self, a):
        neighbours = []
        for x in self.edges:
            if x[0] == a:
                neighbours.append(x[1])
        return neighbours

    def connected(self,a, b, strategy="BFS"):
        # find the shortest path between two nodes of a directed graph
        # using Best First Search
        
        if a == b:
            return True

        visited = {}
        for n in self.nodes:
            visited[n] = False

        if strategy == "BFS":

            stack = []
            stack.append(a)
            while len(stack) > 0:
                p = stack.pop()
                visited[p] = True
                if p == b:
                    return True
                else:
                    neighbours = self.get_neighbours(p)
                    for n in neighbours:
                        if not visited[n]:
                            stack.append(n)

        if strategy == "DFS":
            pass

        return False



    def path(self, node_a, node_b):
        pass




if __name__ == "__main__":

    g = DGraph([1,2,3,4],[[1,2],[1,3],[2,3],[3,4],[4,1]])    
    print(g)
    print("connected: 1 to 4",g.connected(1,4))
    assert g.connected(1,4)     
    g.add_node(5)
    print(g)
    print("connected: 1 to 5",g.connected(1,5))
    assert not g.connected(1,5) 
    g.add_edge(1,5)
    print(g)
    print("connected: 1 to 5",g.connected(1,5))
    assert g.connected(1,5) 



    
