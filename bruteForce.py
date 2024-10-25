from loadData import loadData
from PersonNode import PersonNode
from DanceNode import DanceNode
import numpy as np
import itertools


def findDancersIn(dance, dancesIn):
    dancers = set()
    numPeople = len(dancesIn)
    for i in range (0, numPeople):
        if dancesIn[i][dance]:
            dancers.add(i)

    return dancers

def generateGraph(dances, people, dancesIn):

    numDances = len(dances)
    numNodes = numDances+1
    edges = np.array( [[float('inf') for i in range (0,numNodes)] for i in range (0, numNodes)])
    #deal with dummyNode 0
    dummyIndex =  0
    openingIndexInEdges = None
    for i in range (0, numDances):
        if dances[i].name.lower() == "opening":
            openingIndexInEdges = i+1  #therefore opening index in dances = openinIndexInEdges -1
            edges[0][i+1] = 0
        edges[i+1][0] = 0
        for j in range (i+1, numDances):
            cost = 0
            di = findDancersIn(i, dancesIn)
            dj = findDancersIn(j, dancesIn)
            numInBoth = len(di.intersection(dj))
            cost += numInBoth
            if dances[i].style == dances[j].style:
                cost+= 0.4
            if dances[i].category == dances[j].category:
                cost += 0.4
            edges[i+1][j+1] = cost  #the +1 accounts for first row and column of edges being for dummyNode
            edges[j+1][i+1] = cost
    
    return edges, openingIndexInEdges

def calculateCost(edges, openingIndex, op):
    #op is an order of dances, represented by their indexes in edges
    cost = 0
    cost += edges[openingIndex][op[0]]
    for i in range (0, len(op)-1):
        thisDance = op[i]
        nextDance = op[i+1]
        thisCost = edges[thisDance][nextDance]
        cost += thisCost
    return cost


def bruteForce(edges, openingIndex):
    numNodes = len(edges)
    #ignore the dummy node in this solution
    danceIndexes = [] #these are the dance indexes in edges, NOT their ids, their ids are one less than this index
    for i in range (1, numNodes):
        if i != openingIndex:
            danceIndexes.append(i)
    options = itertools.permutations(danceIndexes)

    minCostOption = []
    minCost = float('inf')
    i = 0
    for op in options:
        print(i)
        i+=1
        thisCost = calculateCost(edges, openingIndex, op)
        if thisCost < minCost:
            minCost = thisCost
            minCostOption = op
    return minCostOption, minCost


# Define the Nearest Neighbor Algorithm
def nearest_neighbor(edges):
    n = edges.shape[0]
    route = [0] # Start at dummyNode
    routeCost = 0
    visited = set([0])
    while len(visited) < n:
        current_city = route[-1]

        nearest_city_andCost = min([(i, edges[current_city][i]) for i in range(n) if i not in visited], key=lambda x: x[1])
        nearest_city, costOfStep = nearest_city_andCost
        route.append(nearest_city)
        routeCost += costOfStep
        visited.add(nearest_city)
    route.append(0) # Return to city A
    return route, routeCost


def displayOrder(runningOrder, dances):
    n = len(runningOrder)
    for i in range (1, n-1) : #ignore dummy node either end
        indexInDances = runningOrder[i]-1
        print(str(dances[indexInDances]))



#to-do next: incorporate interval, a way to pick which dance goes last/before interval; and a way to view who has a quick change
#for future: a way to specify that quick changes with the opening have lower weight than quick changes later on


dances, people, dancesIn = loadData( 'Cleansed Show Data.csv')
#print(dancesIn)
edges, openingIndex = generateGraph(dances, people, dancesIn)
#bestSol, bestSolCost = bruteForce(edges, openingIndex)
bestSol, bestSolCost = nearest_neighbor(edges)
print(bestSolCost)

displayOrder(bestSol, dances)


