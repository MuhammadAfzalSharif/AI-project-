


from utils.filemanager import FileManager
from utils.printer import Printer
from board import Board
from agent import Agent

from bfs import BFS
from dfs import DFS
from ucs import UCS
from greedysearch import GreedySearch
from astartsearch import AStartSearch


def main():
    FileManager.uploadFile("path.txt")
    Printer.showBoardNumbers(FileManager.getOutput())

    opmain = input("Do you want to run a search: \n Enter E:Exit or C:Continue ")
    while(opmain != "E"):
        print("--Welcome--")
        print("-----Menu------")
        print("1. BFS")
        print("2. DFS")
        print("3. UCS")
        print("4. Greedy")
        print("5. A*")
        op = input("Enter an option: ")
        
        aBoard = Board(FileManager.getOutput())
        aBoard.setup()
        agent = Agent("fireman")
        operators = "down,up,right,left"        
        if(op=="1"):
            BFS.search(aBoard, agent, operators) 
            print("Expanded Nodes = ",  BFS.getExpandedNodes())
            print("Tree Depth = ",  BFS.getTreeDeep())  
            print("Computing Time = ", BFS.getComputingTime()," s")
            print("Path = ", BFS.getPath())
            aBoard.reset()  
        elif(op=="2"):
           
            DFS.search(aBoard, agent, operators)
            print("Tree Depth = ",  DFS.getTreeDeep())  
            print("Computing Time = ", DFS.getComputingTime()," s")
            print("Path = ", DFS.getPath())
            aBoard.reset()  
        elif(op=="3"):
            
            UCS.search(aBoard, agent, operators) 
            print("Tree Depth = ",  UCS.getTreeDeep())  
            print("Computing Time = ", UCS.getComputingTime()," s")
            print("Path = ", UCS.getPath())
            aBoard.reset() 
        elif(op=="4"):
           
            GreedySearch.search(aBoard, agent, operators)         
            print("Expanded Nodes = ",  GreedySearch.getExpandedNodes())
            print("Tree Depth = ",  GreedySearch.getTreeDeep())  
            print("Computing Time = ", GreedySearch.getComputingTime()," s")
            print("Path = ", GreedySearch.getPath())
            aBoard.reset()   
        elif(op=="5"):
            
            AStartSearch.search(aBoard, agent, operators)  
            print("Tree Depth = ",  AStartSearch.getTreeDeep())  
            print("Computing Time = ", AStartSearch.getComputingTime()," s")
            print("Path = ", AStartSearch.getPath())
            aBoard.reset() 
        else:
            print("Invalid option") 
        
        opmain= input("Do you want to run a search: \n Enter E:Exit or C:Continue ")
    #Printer.showBoardDetails(aBoard.get())
    

   
    

    
    
main()