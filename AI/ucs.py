from board import Board
from agent import Agent
from node import Node
from state import State
from utils.validation import Validation
from utils.printer import Printer
from move import Move
from utils.count import Count
from utils.selector import Selector
import time
#Uniform Cost Search
class UCS:
    
    queue:list =[]
    countExpandedNodes:int=1
    treeDeep:int=0
    computingTime:float =0.0
    finalNode= None
    costoTotal=0
    name="UCS"

    def search(board:Board, agent:Agent,operators):
        
        print("--- ",__class__.name," ---")
        state = State(board,agent)
        #state:State, father:'Node', operator:str, deep:int, cost:int
        father = Node(state, None,None,0,0)
 
        
        isGoal =Validation.isGoal(board)
        #preValues, currentValues  = {},{}
        index=0
   
        #countExpandedNodes=1
        startTime = time.time()
        while(not(isGoal)):
     
            UCS.generateCandidateNodes(operators,father)
          
            UCS.moveBack(father)
         
            index=UCS.getIndexLessCost(__class__.queue)
            father=__class__.queue[index]
            __class__.countExpandedNodes+=1
       
            UCS.moveToward(father)
            isGoal = Validation.isGoal(father.getState().getBoard())
            if(not(isGoal)):

                  __class__.queue.pop(index)
            else:
                __class__.costoTotal= father.getCost()
                __class__.treeDeep = father.getDeep()
                __class__.finalNode= father
               
                UCS.moveBack(father)
                __class__.queue.clear()
          
            
        endTime = time.time()
        __class__.computingTime = round(endTime -startTime,4)
  
    def getExpandedNodes():
         return __class__.countExpandedNodes
    
    def getTreeDeep():
         return __class__.treeDeep
    
    def getComputingTime():
         return __class__.computingTime
    
    def getCostoTotal():
         return __class__.costoTotal
    
    def getPath():
         return UCS.findPath(__class__.finalNode,"reverse")
    
    def generateCandidateNodes(moveCand,father):
        listofMoves = list(moveCand.split(","))
        #listResult= []
        agent = father.getState().getAgent()
        board = father.getState().getBoard()
        for operator in listofMoves:
            if Validation.moveIsAllowedAhead(Selector.choosePosition(operator, agent, board),agent,board):
                UCS.createNodes(operator, father)

    def createNodes(operator, father):
         node = Node(father.getState(), father, operator, father.getDeep()+1,UCS.g(father))
         if father.getOperator() == Selector.reverseOrientation(node.getOperator()):
                currentValues= Count.getStateValues(father)
                
                UCS.moveBack(father)
                UCS.moveToward(father.getFather())
                preValues= Count.getStateValues(father)
               
                if Validation.canReturn(preValues,currentValues):
                     __class__.queue.append(node)
                
                UCS.moveBack(father.getFather())
                UCS.moveToward(father)
         else:
               __class__.queue.append(node)
    
    def findPath(node, form):
            directios =[]
            if node != None:
                while(node.getFather() != None):
                    directios.append(node.getOperator())
                    node = node.getFather()
                if form == "reverse":
                 directios.reverse()
            return  directios
    
    def findNodePath(node, form):
            dirNodes =[]
            while(node.getFather() != None):
                dirNodes.append(node)
                node = node.getFather()
            if form == "reverse":
                dirNodes.reverse()
            return dirNodes
    
    def moveBack(node):
           dirNodes = UCS.findNodePath(node, "unreverse")
           for item in dirNodes:
               Move.back(item.getOperator(), item.getState())

    def moveToward(node):
            dirNodes = UCS.findNodePath(node, "reverse")
            for item in dirNodes:
               Move.toward(item.getOperator(), item.getState())
    
    def determineCost(state):
        bucket = state.getAgent().getBucket()
        cost = 1  
        if bucket.getLoad() > 0:
             cost += bucket.getLoad()

        return cost
    
    def getIndexLessCost(queue):
         index= 0
         lessCost = queue[0].getCost()
         for i in range(1,len(queue)):
              if queue[i].getCost()<lessCost:
                   lessCost = queue[i].getCost()
                   index = i
         return index
    

    def getAvailableDirections(movesCand:str,father):
        listofMoves = list(movesCand.split(","))
        listResult= []
        agent = father.getState().getAgent()
        board = father.getState().getBoard()
        for item in listofMoves:
            if Validation.moveIsAllowedAhead(Selector.choosePosition(item, agent, board),agent,board):
                listResult.append(item)
        return listResult  


    #cost function g(n) calculate the cost of the path in each node
    def g(node):
         return node.getCost()+UCS.determineCost(node.getState())           
         