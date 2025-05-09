
from board import Board
from agent import Agent

class State:
    def __init__(self,board:Board, agent:Agent):
        self.board = board
        self.agent = agent

    def getBoard(self):
        return self.board
    
    def getAgent(self):
        return self.agent
    
  