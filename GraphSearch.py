from Node import DanceNode as Node
import itertools
nextFreeiD = 0

x = Node("Defying Gravity", ["P01" , "P02", "P03", "P04", "P05"], "Wildcard", "Varsity" )
y = Node("In Fair Verona", ["P01" , "P03", "P05"], "Tap", "Varsity" )
z = Node("Cam Tap Solo", ["P01"], "Tap", "Solo" )
w = Node("Contemporary", ["P02", "P06"], "Contemp", "Duet" )
u = Node("Varsity Ballet", ["P03", "P05", "P06", "P08"], "Ballet", "Varsity" )
s = Node("Ballet Duet", ["P03", "P05"], "Ballet", "Small Group")
t = Node("Miranda Solo", ["P09"], "Contemp", "Solo")
a = Node("Zarmina Solo", ["P10"], "Contemp", "Solo")
opening = Node("Opening", ["P01" , "P02", "P03", "P04", "P05", "P06",  "P07", "P08", "P09", "P10"], "Jazz", "Troupe" )
finale = Node("Finale", ["P01" , "P02", "P03", "P04", "P05", "P06", "P07", "P08"], "Jazz", "Troupe" )
dummyNode = Node("Dummy", [], "", "")


nodes = [opening, x,y,z,w,u,s,t,a]  # MUST put opening first in this list for correctness
n = len(nodes)

edges = [None] * n 
for i in range(0,n): edges[i] = [[dummyNode , dummyNode, 100]] * n
print (edges)

for node in nodes:
    nextFreeiD = node.setDiD(nextFreeiD)

for node1 in nodes:
    
    node1iD = node1.getDiD()
    for node2 in nodes:
        node2iD = node2.getDiD()
        weight = 0
        dancerListOne = node1.getDanceriDs()
        dancerListTwo  = node2.getDanceriDs()
        for i in range(0, len(dancerListOne)):
            person1 = dancerListOne[i]
            """for j in range(0, len(dancerListTwo)):
                person2 = dancerListTwo[j]
                print(person2)
                if person1 == person2:  
                    weight = weight + 1"""
            if person1 in dancerListTwo: 
                print(str(person1) + " is in this dance: " + str(node2iD))
                weight+=1
        if node1.getStyle == node2.getStyle: weight = weight + 0.5
        if node1.getType == node2.getType: weight = weight + 0.25
        if node1iD == node2iD: weight = 100000
        if node1iD == 0: weight = weight /2.0
        edges[node1iD][node2iD] = [node1, node2, weight]
        edges[node2iD][node1iD] = [node2, node1, weight]

for i in range(0, len(nodes)):
    
    for j in range(0, len(nodes)):
        node1 = edges[i][j][0]
        node2 = edges[i][j][1]
        weight = edges[i][j][2]
        print(node1.getName() + ", " + node2.getName() + ", " + str(weight))



startNode = opening
endNode = x

print(str(edges[0]))

def crudeSolution():
    orders = itertools.permutations(range(1,n))
    minCost = 1000000000
    minCostOrder = None
    for order in orders:
        #print(order)
        totalcost = edges[0][order[0]][2]  #weight of going from opening to first number in order
        #print(totalcost)
        for position in range(0,n-2):
            thisDanceiD = order[position]
            nextDanceiD = order[position+1]
            totalcost = totalcost + edges[thisDanceiD][nextDanceiD][2] 
        if totalcost < minCost:
            minCost = totalcost
            minCostOrder = order
    print(minCostOrder)
    for id in minCostOrder:
        print(nodes[id].getName())
    print(minCost)
    return minCostOrder




crudeSolution()

    










        





