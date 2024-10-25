class PersonNode:

    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __eq__ (self,otherPerson):
        return self.id == otherPerson.id