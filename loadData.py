from PersonNode import PersonNode
from DanceNode import DanceNode
import numpy as np
#load data from ane excel to generate:
# - an array dances of danceNodes, satisfying dances[i].id == i
# - an array people of PersonNodes, satisfying people[i].id == i
# - a 2D array dancesIn s.t. dancesIn[i][j] == True iff people[i] is a dancer in dances[j]

import csv
def loadData(csvPath):
    dances =[]
    people = []
    dancesIn = None

    with open(csvPath, 'r') as file:
        danceInfoReader = csv.reader(file)
        rows= []
        for row in danceInfoReader:
            if not any(row):
                pass
            else:
                rows.append(row)
        
        danceInfo = np.array(rows)
        n = len(danceInfo)
        numDances = n-1
        headerRow = danceInfo[0]
        m = len(headerRow)
        numPeople = m-3
        dancesIn = [[False for i in range (0, numDances)] for i in range (0, numPeople)]
        for i in range(3, len(headerRow)):
            people.append(PersonNode(i-3, headerRow[i]))
        for i in range(1, n):
            danceRow = danceInfo[i]
            dances.append(DanceNode(i-1, danceRow[0], danceRow[1], danceRow[2]))
            #now we find which people are in this dance
            for j in range (3, m):
                if '1' in danceRow[j]:
                    #then person with id j-3 is in dance with id i-1
                    dancesIn[j-3][i-1] = True
        dancesIn = np.array(dancesIn)
        people = np.array(people)
        dances = np.array(dances)
    return dances, people, dancesIn






