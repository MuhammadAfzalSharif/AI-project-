
from tkinter import *
import time
import os 
from tkinter import filedialog
from utils.filemanager import FileManager
from utils.printer import Printer
from utils.selector import Selector
from board import Board
from agent import Agent
from position import Position
from bfs import BFS
from dfs import DFS
from ucs import UCS
from greedysearch import GreedySearch
from astartsearch import AStartSearch

#---------------------------------------------------MAIN WINDOW PARAMETERS --------------------------
# Create main window
root = Tk()
root.title("Smart Firefighter 🚒")
root.geometry("1400x850")
root.resizable(True, False)
root.configure(bg='#FFE082')  # Bright amber background

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------DATA---------------------------------------------

# Images (Assuming same paths, consider adding colorful icons)
searchImage = PhotoImage(file='./images/search.png')
fileImage = PhotoImage(file='./images/upload.png')

# Lists
searchNames = ["BFS", "Uniform Cost", "DFS", "Greedy", "A*"]
searchResults = []
searchSelected = []
environment = []

# Tkinter variable for radiobuttons
radioV = IntVar()
radioV.set("1")  # Default to BFS

#-------------------------------------------------------------------------------------------------
#----------------------------------------FRAMES CREATIONS---------------------------------------

# Title frame
titleFrame = LabelFrame(root, highlightthickness=0, borderwidth=0, bg='#FFE082')
titleFrame.pack(pady=10)

# Main frame
mainFrame = LabelFrame(root, padx=20, pady=20, bg='#FFF3E0', relief="flat")
mainFrame.pack(padx=10, pady=10)

# World frame
worldFrame = LabelFrame(mainFrame, padx=10, pady=10, bg='#212121', relief="solid", bd=2)
worldFrame.grid(padx=20, pady=20, row=0, rowspan=75, column=45, columnspan=90)

# Options frame
optionsFrame = LabelFrame(mainFrame, padx=20, pady=20, bg='#FFF3E0', relief="flat")
optionsFrame.grid(padx=20, pady=20, row=0, rowspan=60, column=0, columnspan=45)

# Button frame
buttonFrame = LabelFrame(mainFrame, bg='#FFF3E0', relief="flat")
buttonFrame.grid(padx=10, row=76, rowspan=140, column=45, columnspan=90)
showButton = Button(buttonFrame, text="Show Path 🌟", font=("Comic Sans MS", 14, "bold"), 
                    command=lambda: showAnimation(), fg="#FFFFFF", bg="#F06292", 
                    activebackground="#EC407A", bd=0, padx=20, pady=10, state=DISABLED)
showButton.pack(pady=10)

# Search title frame
searchTitleFrame = LabelFrame(mainFrame, highlightthickness=0, borderwidth=0, bg='#FFF3E0')
searchTitleFrame.grid(padx=10, row=61, column=0, columnspan=45)

# Report frame
reportFrame = LabelFrame(mainFrame, highlightthickness=0, borderwidth=0, bg='#FFF3E0')
reportFrame.grid(padx=10, row=64, rowspan=150, column=0, columnspan=45)

#---------------------------------------------------------------------------------------------------
#-----------------------------------------TITLEFRAME WIDGETS--------------------------------------

def showGameTitle(title):
    titleLabel = Label(titleFrame, text=f"{title} 🔥", font=("Comic Sans MS", 36, "bold"), 
                       fg="#D81B60", bg="#FFE082", pady=10)
    titleLabel.pack()

#-------------------------------------------------------------------------------------------------
#------------------------------------------OPTIONSFRAME WIDGET------------------------------------

def showMenuOptions(img, sNames):
    # Options main image
    searchImageLabel = Label(optionsFrame, image=img, bg="#FFF3E0")
    # Options main title
    searchTitle = Label(optionsFrame, text="Search Strategies 🧠", 
                        font=("Comic Sans MS", 24, "bold"), fg="#0288D1", bg="#FFF3E0")
    
    # Uninformed options title
    uninformedTitle = Label(optionsFrame, text="Uninformed Search 🔍", 
                            font=("Comic Sans MS", 18, "bold"), fg="#388E3C", bg="#FFF3E0")
    # Informed options title
    informedTitle = Label(optionsFrame, text="Informed Search 🌈", 
                          font=("Comic Sans MS", 18, "bold"), fg="#388E3C", bg="#FFF3E0")

    # Layout
    searchImageLabel.grid(row=0, column=0, columnspan=4, pady=10)
    searchTitle.grid(row=1, column=0, columnspan=4, pady=5)
    uninformedTitle.grid(row=2, column=1, pady=10)
    showUninformedOptions(sNames)
    informedTitle.grid(row=4, column=1, pady=10)
    showInformedOptions(sNames)
    
    for child in optionsFrame.winfo_children():
        child.configure(state=DISABLED)

def showUninformedOptions(sNames: list) -> None:
    for i in range(1, 4):
        uninformeSearchOption = Radiobutton(optionsFrame, text=f"{sNames[i-1]} 🛠️", 
                                            font=("Comic Sans MS", 16, "bold"), 
                                            variable=radioV, value=i, bg="#FFF3E0", 
                                            fg="#0288D1", activebackground="#B3E5FC",
                                            selectcolor="#81D4FA",
                                            command=lambda: showSearchSelected(searchNames[radioV.get()-1]))
        uninformeSearchOption.grid(row=3, column=i, padx=10, pady=5)

def showInformedOptions(sNames: list) -> None:
    columValue = 1
    for i in range(4, 6):
        informeSearchOption = Radiobutton(optionsFrame, text=f"{sNames[i-1]} ✨", 
                                          font=("Comic Sans MS", 16, "bold"), 
                                          variable=radioV, value=i, bg="#FFF3E0", 
                                          fg="#0288D1", activebackground="#B3E5FC",
                                          selectcolor="#81D4FA",
                                          command=lambda: showSearchSelected(searchNames[radioV.get()-1]))
        informeSearchOption.grid(row=5, column=columValue, padx=10, pady=5)
        columValue += 2

#--------------------------------------------------------------------------------------------------
#---------------------------------------------------WORLDFRAME WIDGETS----------------------------        

def showWorld(environment: list) -> None:
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            number = environment[i][j]
            a_label = Label(worldFrame, padx=12, pady=8, 
                            bg=Selector.chooseColor(number), border=1, 
                            relief="solid", font=("Comic Sans MS", 12))
            a_label.grid(row=i, column=j)

def showWorldEmtyWorld() -> None:
    e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    eList = [e, e, e, e, e, e, e, e, e, e]
    for i in range(len(eList)):
        for j in range(len(eList[i])):
            number = eList[i][j]
            a_label = Label(worldFrame, padx=12, pady=8, 
                            bg=Selector.chooseColor(number), border=1, 
                            relief="solid", font=("Comic Sans MS", 12))
            a_label.grid(row=i, column=j)

def showWorldNotExecute(environment: list) -> None:
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            number = environment[i][j]
            a_label = Label(worldFrame, padx=12, pady=8, 
                            bg=Selector.chooseColor(number), border=1, 
                            relief="solid", font=("Comic Sans MS", 12))
            a_label.grid(row=i, column=j)

def showWorldAnimation(positions, environment) -> None:
    for pos in positions: 
        a_label = Label(worldFrame, padx=12, pady=8, bg="#E91E63", 
                        border=1, relief="solid", font=("Comic Sans MS", 12))
        a_label.grid(row=pos.getCordI(), column=pos.getCordJ())
        time.sleep(0.2)
        root.update()
        number = environment[pos.getCordI()][pos.getCordJ()]
        a_label = Label(worldFrame, padx=12, pady=8, 
                        bg=Selector.chooseColor(number), border=1, 
                        relief="solid", font=("Comic Sans MS", 12))
        a_label.grid(row=pos.getCordI(), column=pos.getCordJ())
        time.sleep(0.2)
        root.update()

#--------------------------------------------------------------------------------------------------
#--------------------------------------------BUTTONFRAME WIDGETS----------------------------------

def showAnimation():
    showWorldNotExecute(environment[0])
    path = searchResults[0][4]
    showWorldAnimation(getPositions(environment[0], path), environment[0])

def getStartPosition(environment):
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            number = environment[i][j]
            if number == 5:
                pos = Position(i, j)
    return pos

def getPositions(environment, path):
    posInit = getStartPosition(environment)
    positions = []
    positions.append(posInit)
    for i in range(len(path)):
        posInit = Selector.chooseNewPosition(path[i], posInit)
        positions.append(posInit)
    return positions

def showUploadFileImage(img):
    uploadButton = Button(mainFrame, text="Upload Map 📁", image=img, compound="left", 
                         font=("Comic Sans MS", 14, "bold"), fg="#FFFFFF", 
                         bg="#4CAF50", activebackground="#388E3C", bd=0, 
                         padx=20, pady=10, 
                         command=lambda: chooseFile(os.getcwd()))
    uploadButton.grid(column=0, row=0, pady=10)

#------------------------------------------- SEARCHTITLEFRAME WIDGETS-----------------------------

def showSearchSelected(searchName: str):
    # Clear previous widgets in searchTitleFrame
    for widget in searchTitleFrame.winfo_children():
        widget.destroy()
    
    # Add new search title
    searchLabel = Label(searchTitleFrame, text=f"{searchName} 🚀", 
                        font=("Comic Sans MS", 22, "bold"), fg="#D81B60", 
                        bg="#FFF3E0", pady=10)
    searchLabel.grid(row=0, column=1, columnspan=4)
    
    showWorldNotExecute(environment[0])
    searchSelected.clear()
    searchSelected.append(searchName)
    
    if searchName == "BFS":
        executeSearch(environment[0], searchName)
        showReport()
    elif searchName == "Uniform Cost":
        executeSearch(environment[0], searchName)
        showReport()
    elif searchName == "DFS":
        executeSearch(environment[0], searchName)
        showReport()
    elif searchName == "Greedy":
        executeSearch(environment[0], searchName)
        showReport()
    else:
        executeSearch(environment[0], searchName)
        showReport()

    showButton.config(state=NORMAL)

#--------------------------------------------------------------------------------------------------   
#------------------------------------------------------REPORTFRAME WIDGETS-------------------------

def showReport():
    # Clear previous widgets in reportFrame
    for widget in reportFrame.winfo_children():
        widget.destroy()
    
    columsTitles = ["Expanded Nodes 📊", "Tree Depth 🌳", "Time ⏱️", "Cost 💰"]
    searchs = searchResults[0]

    for i in range(len(columsTitles)):
        a_title = Label(reportFrame, text=columsTitles[i], 
                        font=("Comic Sans MS", 12, "bold"), fg="#FFFFFF", 
                        bg="#0288D1", padx=10, pady=5, relief="raised")
        a_title.grid(row=1, column=i, padx=5, pady=2)
        a_answer = Label(reportFrame, text=searchs[i], 
                         font=("Comic Sans MS", 12), fg="#212121", 
                         bg="#B3E5FC", padx=10, pady=5)
        a_answer.grid(row=2, column=i, padx=5, pady=2)

def showReportEmpty():
    # Clear previous widgets in searchTitleFrame and reportFrame
    for widget in searchTitleFrame.winfo_children():
        widget.destroy()
    for widget in reportFrame.winfo_children():
        widget.destroy()
    
    # Add empty report title
    searchLabel = Label(searchTitleFrame, text="Report 📋", 
                        font=("Comic Sans MS", 22, "bold"), fg="#D81B60", 
                        bg="#FFF3E0", pady=10)
    searchLabel.grid(row=0, column=1, columnspan=4)

    columsTitles = ["Expanded Nodes 📊", "Tree Depth 🌳", "Time ⏱️", "Cost 💰"]
    for i in range(len(columsTitles)):
        a_title = Label(reportFrame, text=columsTitles[i], 
                        font=("Comic Sans MS", 12, "bold"), fg="#FFFFFF", 
                        bg="#0288D1", padx=10, pady=5, relief="raised")
        a_title.grid(row=1, column=i, padx=5, pady=2)
        a_answer = Label(reportFrame, text=" ", 
                         font=("Comic Sans MS", 12), fg="#212121", 
                         bg="#B3E5FC", padx=10, pady=5)
        a_answer.grid(row=2, column=i, padx=5, pady=2)

#--------------------------------------------------------------------------------------------------   
def executeSearch(environment, searchName):
    searchResults.clear()
    aBoard = Board(environment)
    aBoard.setup()
    agent = Agent("fireman")
    operators = "down,up,right,left"
    
    if searchName == "BFS":
        BFS.search(aBoard, agent, operators)
        search = []
        search.append(BFS.getExpandedNodes())
        search.append(BFS.getTreeDeep())
        search.append(BFS.getComputingTime())
        search.append("No aplica")
        search.append(BFS.getPath())
        searchResults.append(search)
        aBoard.reset()
    elif searchName == "Uniform Cost":
        UCS.search(aBoard, agent, operators)
        search = []
        search.append(UCS.getExpandedNodes())
        search.append(UCS.getTreeDeep())
        search.append(UCS.getComputingTime())
        search.append(UCS.getCostoTotal())
        search.append(UCS.getPath())
        searchResults.append(search)
        aBoard.reset()
    elif searchName == "DFS":
        DFS.search(aBoard, agent, operators)
        search = []
        search.append(DFS.getExpandedNodes())
        search.append(DFS.getTreeDeep())
        search.append(DFS.getComputingTime())
        search.append("No aplica")
        search.append(DFS.getPath())
        searchResults.append(search)
        aBoard.reset()
    elif searchName == "Greedy":
        GreedySearch.search(aBoard, agent, operators)
        search = []
        search.append(GreedySearch.getExpandedNodes())
        search.append(GreedySearch.getTreeDeep())
        search.append(GreedySearch.getComputingTime())
        search.append("No aplica")
        search.append(GreedySearch.getPath())
        searchResults.append(search)
        aBoard.reset()  
    else:
        AStartSearch.search(aBoard, agent, operators)
        search = []
        search.append(AStartSearch.getExpandedNodes())
        search.append(AStartSearch.getTreeDeep())
        search.append(AStartSearch.getComputingTime())
        search.append(AStartSearch.getCostoTotal())
        search.append(AStartSearch.getPath())
        searchResults.append(search)
        aBoard.reset() 

#--------------------------------------------------------------------------------------------------   

def chooseFile(currentpath):
    filepath = filedialog.askopenfilename(initialdir=currentpath, title="Select a Map", 
                                         filetypes=(('text files', '*.txt'),))
    FileManager.uploadFile(filepath)
    environment.clear()
    environment.append(FileManager.getOutput())
    showWorld(environment[0])
    for child in optionsFrame.winfo_children():
        child.configure(state=NORMAL)
    showReportEmpty()

#-----------------------------------------------------------------------------------------------
#------------------------------------------GUI CREATION------------------------------------------

def main():
    showGameTitle("Smart Firefighter")
    showUploadFileImage(fileImage)
    showMenuOptions(searchImage, searchNames)
    showWorldEmtyWorld()
    showReportEmpty()
    root.mainloop()

main()

#------------------------------------------------------------------------------------------------
#---------------------------------------GUI EXECUTION------------------------------------------
#---------------------------------------------------------------------------------------------