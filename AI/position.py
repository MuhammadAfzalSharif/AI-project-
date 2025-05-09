
class Position:

    def __init__(self,cordI:str, cordJ:str):
        self.cordI = cordI
        self.cordJ = cordJ

    def setCordI(self,cordI):
        self.cordI = cordI
    
    def setCordJ(self, cordJ):
        self.cordJ = cordJ
    
    def getCordI(self):
        return self.cordI
    
    def getCordJ(self):
        return self.cordJ
    
    def isSame(self,otherPos):
        isSameRow = self.cordI == otherPos.getCordI()
        isSameColunm = self.cordJ == otherPos.getCordJ()
        return isSameRow and isSameColunm


