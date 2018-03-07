from collections import defaultdict

#---- Definitions ----#

#Graph
Graph = {}

#Transpose of Graph
Transpose_Graph = {}

#Visited Nodes for Graph
Visited_Nodes_Graph = {}

#Visited Nodes for Transpose Graph
Visited_Nodes_Transpose_Graph = {}

#Component Id
Component_Id = dict()

#Stack to process
Stack = []

#---- Definitions ----#

#Based on the number of verticies, create a dictionary where every vertex is the key, and the value are the edges from it to another vertex.
def Generate_Empty_Graphs(Number_of_Verticies):
    for Vertex in range(1, Number_of_Verticies+1):
        Graph[Vertex] = []
        Transpose_Graph[Vertex] = []
        Visited_Nodes_Graph[Vertex] = False
        Visited_Nodes_Transpose_Graph[Vertex] = False

#Populate Graph with edges
def Populate_Graphs(Head, Tail):
    Graph[Head].append(Tail)
    Transpose_Graph[Tail].append(Head)

#Run DFS on given Graph, at provided position.
#This is used for DFS #2 (
def Run_DFS(Vertex, Given_Graph, SCC_List):
    Visited_Nodes_Transpose_Graph[Vertex] = True
    SCC_List.append(Vertex)
    for Adjacent_Vertex in Transpose_Graph[Vertex]:
        if(Visited_Nodes_Transpose_Graph[Adjacent_Vertex] == False):
            Run_DFS(Adjacent_Vertex, Transpose_Graph[Adjacent_Vertex], SCC_List)
        #TODO something here to log it...
    return SCC_List


#Process Stack and run DFS
#This is used for DFS #1
def Populate_Stack(Vertex, Given_Graph):
    Visited_Nodes_Graph[Vertex] = True
    for Adjacent_Vertex in Given_Graph[Vertex]:
        if (Visited_Nodes_Graph[Adjacent_Vertex] == False):
            Populate_Stack(Adjacent_Vertex, Given_Graph)
    Stack.append(Vertex)


def Detect_SCCs(Given_Graph, Number_Of_Verticies):
    for Vertex in range(1, Number_Of_Verticies+1):
        if(Visited_Nodes_Graph[Vertex] == False):
            Populate_Stack(Vertex, Given_Graph)

    SCC = []

    Current_Component_Id = 0
    
    while(len(Stack) != 0):
        Current_Vertex = Stack.pop()
        if(Visited_Nodes_Transpose_Graph[Current_Vertex] == False):
            SCC = Run_DFS(Current_Vertex, Transpose_Graph, [])
            Current_Component_Id += 1
            for SCC_Vertex in SCC:
                Component_Id[SCC_Vertex] = Current_Component_Id
            
            print(SCC)


Number_Of_Verticies = 9
Generate_Empty_Graphs(Number_Of_Verticies)

Populate_Graphs(1, 2)
Populate_Graphs(2, 3)
Populate_Graphs(3, 1)
Populate_Graphs(3, 4)
Populate_Graphs(3, 7)
Populate_Graphs(4, 6)
Populate_Graphs(6, 5)
Populate_Graphs(5, 4)
Populate_Graphs(7, 8)
Populate_Graphs(8, 9)
Populate_Graphs(9, 7)

Detect_SCCs(Graph, Number_Of_Verticies)

#Components generated here. Now build new graph using component ids
#Component Graph
Component_Graph = {}

#Reset visited for next DFS
def Reset_Visited(Number_of_Verticies):
    for Vertex in range(1, Number_of_Verticies+1):
        Visited_Nodes_Graph[Vertex] = False

def Generate_Component_Graph_DFS(u, Given_Graph):
    if (Visited_Nodes_Graph[u]==True):
        return
    Visited_Nodes_Graph[u] = True

    for v in Given_Graph[u]:
        if (Component_Id[u] != Component_Id[v]):
            Component_U = Component_Id[u]
            Component_V = Component_Id[v]
            if Component_U not in Component_Graph:
                Component_Graph[Component_U] = []
            Component_Graph[Component_U].append(Component_V)
        Generate_Component_Graph_DFS(v, Given_Graph)

def Generate_Component_Graph(Given_Graph):
    for u in Given_Graph:
        Generate_Component_Graph_DFS(u, Given_Graph)

Reset_Visited(Number_Of_Verticies)
Generate_Component_Graph(Graph)

#Now for a given vertex, get component id of that vertex
#And travarse for number of reachable nodes in Component_Graph for this component id

def Reachable_SCC_DFS(Given_Component_Id, Generated_Component_Graph):
    Reachable_SCC_Count = 1
    if (Given_Component_Id not in Generated_Component_Graph):
        return Reachable_SCC_Count

    for Component_Vertex in Generated_Component_Graph[Given_Component_Id]:
        Reachable_SCC_Count += Reachable_SCC_DFS(Component_Vertex, Generated_Component_Graph)

    return Reachable_SCC_Count

def Reachable_SCC(Given_Vertex, Generated_Component_Graph):
    return Reachable_SCC_DFS(Component_Id[Given_Vertex], Generated_Component_Graph)

for Vertex in range(1, Number_Of_Verticies+1):
    print ('Vertex ' + str(Vertex) + ' => ' + str(Reachable_SCC(Vertex, Component_Graph)) + ' reachable SCC')


#Note: for Reachable_SCC_DFS visited falg will not be necessary because there will not be any loop in this graph. If there would be any loop then it would had been a merged SCC.