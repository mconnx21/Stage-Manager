
class DanceNode():
    def __init__(self, Name, DanceriDs, Style, Type):
        self.danceiD = 00000
        self.name = Name
        copyOfDancers = DanceriDs.copy()
        self.danceriDs = copyOfDancers
        self.style = Style
        self.type = Type
    
    def setDiD(self, inputiDVar):
        #returns the increment of the input. Idea is that this returns the new next availiable ID.
        self.danceiD = inputiDVar
        nextFreeDiD = inputiDVar + 1
        return nextFreeDiD
    
    def getDiD(self):
        return self.danceiD
    
    def getName(self):
        return self.name
    
    def getDanceriDs(self):
        return self.danceriDs
    
    def getStyle(self):
        return self.style
    
    def getType(self):
        return self.type



class PersonNode():
    def __init__(self, Name):
        self.personiD = 00000
        self.name = Name

    def setPiD(self, inputiDVar):
        #returns the increment of the input. Idea is that this returns the new next availiable ID.
        self.personiD = inputiDVar
        nextFreeDiD = inputiDVar + 1
        return nextFreeDiD
    
    def getPiD(self):
        return self.personiD
    
    def getName(self):
        return self.name



    

    





    

