import random
import numpy as np
class game(object):
    def __init__(self, board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]):
        self.board = board; self.score = 0
        self.statics = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
        self.addTile(); self.addTile()
    def show(self):
        for row in self.board:
            print row
    def move(self, direction):
        self.statics = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
        s = [[item for item in x] for x in self.board]
        if direction ==1:  moved = self.moveDir(s,[1,2,3,1,2,1], False)
        elif direction ==2: moved = self.moveDir(s,[2,1,0,2,1,2], True)
        elif direction ==3: moved = self.moveDir(s,[2,1,0,2,1,2], False)
        elif direction ==4: moved = self.moveDir(s,[1,2,3,1,2,1], True)
        if np.count_nonzero(self.board) == 16:
            saved = [[x for x in item] for item in self.board]
            canmove = self.moveDir([1,2,3,1,2,1], False)+self.moveDir([2,1,0,2,1,2], True)+self.moveDir([2,1,0,2,1,2], False)+self.moveDir([1,2,3,1,2,1], True)
            if canmove == 0: print "you lose your score was "+str(self.score)
            else: self.board = saved
        elif moved: self.addTile()
        else: print "can't move that way"
        self.show()
    def addTile(self):
        place = (random.randint(0,3),random.randint(0,3))
        while self.board[place[0]][place[1]]!=0:
            place = (random.choice([0,1,2,3]),random.choice([0,1,2,3]))
        self.board[place[0]][place[1]]=random.choice([2,2,2,2,4])
    def moveLine(self, start, direction, column):
        if column: self.board = np.transpose(self.board)
        for i in range(4):
            if self.board[start][i] !=0 and not self.statics[start+direction][i]:
                if not self.statics[start][i] and self.board[start+direction][i] == self.board[start][i]:
                    self.board[start+direction][i]*=2
                    self.statics[start+direction][i] = True
                    self.score+=self.board[start+direction][i]
                    self.board[start][i] =0
                if self.board[start+direction][i]==0:
                    self.board[start+direction][i]=self.board[start][i]
                    self.board[start][i] =0
        if column: self.board = np.transpose(self.board).tolist()
    def moveDir(self, start, lis, column):
        for i in lis:
            self.moveLine(i,2*lis[0]-3, column)
        if start ==self.board: return False
        return True
