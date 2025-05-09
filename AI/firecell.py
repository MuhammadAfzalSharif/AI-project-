
from cell import Cell
class FireCell(Cell):
    #Constructor
    def __init__(self, properties:dict):
        super().__init__(properties)

    def isFireOn(self):
        return self.properties["fireOn"]
    
    def fireOff(self):
        if self.properties["fireOn"]:
            self.properties["fireOn"] = False
            #print("¡Fire extinguished!")

    def fireOn(self):
          if not(self.properties["fireOn"]):
            self.properties["fireOn"] = True
            #print("¡Fire unextinguished!")   