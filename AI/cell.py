
from position import Position

class Cell:
    
    #Constructor
    def __init__(self, properties:dict):
        # Instance attribute
        self.properties=properties   

    def getPosition(self):
        return self.properties["position"]
    
    def getNumber(self):
        return self.properties["number"]
    
    def getColor(self):
        return self.properties["color"]
    
    def getName(self):
        return self.properties["name"]
    
    def isAgentHere(self):
        return self.properties["agentHere"]
    
    def changeAgentHere(self):
        self.properties["agentHere"] = not(self.properties["agentHere"])

    #New Code
    def changeAgentToHere(self):
        self.properties["agentHere"] = True
    
    def removeAgentFromHere(self):
        self.properties["agentHere"] = False