# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *                          TicTacToe_ML by Jacopx                         *
# *                  https://github.com/Jacopx/TicTacToe_ML                 *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Public Libraries
import random

# Basic element of the game
class Board:
    def __init__(self, p1='A', p2='B', dim=3):
        self.dim = dim
        self.p1 = p1
        self.p2 = p2
        self.board = [[0 for x in range(dim)] for y in range(dim)]

    # Clear variable board
    @staticmethod
    def clearboard(self):
        self.board = [[0 for x in range(self.dim)] for y in range(self.dim)]

    # Printing board
    def printboard(self, type=0):
        for i in range(self.dim):
            for j in range(self.dim):
                if type == 0:
                    if self.board[i][j] == 1:
                        print(self.p1, end=' ')
                    else:
                        print(self.p2, end=' ')
                else:
                    print("%d" % self.board[i][j], end=' ')
            print()
        print()
    def setvalue(self, value, i, j):
        self.board[i][j] = value

    def setrandomvalue(self):
        self.board[random.randrange(0, self.dim, 1)][random.randrange(0, self.dim, 1)] = random.randrange(0, 3, 1)

    def setboard(self, board):
        self.board = board

    def getboard(self):
        return self.board

# NN brain used for playing
class Brain:
    def __init__(self):
        self.hash = None
