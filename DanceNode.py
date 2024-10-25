class DanceNode:

    def __init__(self, id, name, category, style):
        self.id = id
        self.name = name
        self.style = style
        self.category = category 
    
    def __eq__(self, otherDance):
        return otherDance.id == self.id
    
    def __str__(self):
        return "Name: " + self.name + "                           |     Style: " + self.style + "    |    Category: " + self.category