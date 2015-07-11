import random
import numpy as np

class game(object):
    def __init__(self, info):
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.score = 0

    def start(self):
        value1 = random.choice([2,2,2,2,4])
        value2 = random.choice([2,2,2,2,4])
        start1 = (random.choice([0,1,2,3]),random.choice([0,1,2,3]))
        start2 = (random.choice([0,1,2,3]),random.choice([0,1,2,3]))
        while start2==start1:
            start2 = (random.choice([0,1,2,3]),random.choice([0,1,2,3]))
        self.board[start1[0]][start1[1]] = value1
        self.board[start2[0]][start2[1]] = value2
        
    def show(self):
        for row in self.board:
            print row
            
    def move(self, direction, printing = True):
        if direction ==1:
            moved = self.moveUp()
        elif direction ==2:
            moved = self.moveRight()
        elif direction ==3:
            moved = self.moveDown()
        elif direction ==4:
            moved = self.moveLeft()
        else:
            print "move must be called with 1, 2, 3,or 4"
        if self.gameOver():
            if printing:
                print "you lose, your score was"
                self.show()
                print self.score
            return self.score
        if moved:
            self.addTile()
            if printing:
                self.show()
        else:
            "can't move that way"
            return "can't move that way"
        
    def addTile(self):
        value = random.choice([2,2,2,2,4])
        place = (random.choice([0,1,2,3]),random.choice([0,1,2,3]))
        while self.board[place[0]][place[1]]!=0:
            place = (random.choice([0,1,2,3]),random.choice([0,1,2,3]))
        self.board[place[0]][place[1]]=value
        
    def gameOver(self):
        lose = True
        for row in self.board:
            for item in row:
                if item ==0:
                    lose = False
        return lose
    
    def moveRow(self, start, direction, cellsToMove):
        cells = []
        for i in cellsToMove:
            if self.board[start][i] !=0:
                if self.board[start+direction][i] == self.board[start][i]:
                    self.board[start+direction][i]*=2
                    self.board[start][i] =0
                    cells.append(i)
                    self.score+=2*i
                if self.board[start+direction][i]==0:
                    self.board[start+direction][i]=self.board[start][i]
                    self.board[start][i] =0
        return [item for item in cellsToMove if item not in cells]
    def moveColumn(self, start, direction, cellsToMove):
        cells = []
        for i in cellsToMove:
            if self.board[i][start] !=0:
                if self.board[i][start+direction] == self.board[i][start]:
                    self.board[i][start+direction]*=2
                    self.board[i][start] =0
                    cells.append(i)
                    self.score+=2*i
                if self.board[i][start+direction]==0:
                    self.board[i][start+direction]=self.board[i][start]
                    self.board[i][start] =0
        return [item for item in cellsToMove if item not in cells]
    def moveUp(self):
        start = [[item for item in x] for x in self.board]
        cells = self.moveRow(1,-1,range(4))
        cells = self.moveRow(2,-1,cells)
        cells = self.moveRow(3,-1,cells)
        cells = self.moveRow(1,-1,cells)
        cells = self.moveRow(2,-1,cells)
        cells = self.moveRow(1,-1,cells)
        if start == self.board:
            return False
        return True
    def moveDown(self):
        start = [[item for item in x] for x in self.board]
        cells = self.moveRow(2,1,range(4))
        cells = self.moveRow(1,1,cells)
        cells = self.moveRow(0,1,cells)
        cells = self.moveRow(2,1,cells)
        cells = self.moveRow(1,1,cells)
        cells = self.moveRow(2,1,cells)
        if start == self.board:
            return False
        return True
    def moveLeft(self):
        start = [[item for item in x] for x in self.board]
        cells = self.moveColumn(1,-1,range(4))
        cells = self.moveColumn(2,-1,cells)
        cells = self.moveColumn(3,-1,cells)
        cells = self.moveColumn(1,-1,cells)
        cells = self.moveColumn(2,-1,cells)
        cells = self.moveColumn(1,-1,cells)
        if start == self.board:
            return False
        return True
    def moveRight(self):
        start = [[item for item in x] for x in self.board]
        cells = self.moveColumn(2,1,range(4))
        cells = self.moveColumn(1,1,cells)
        cells = self.moveColumn(0,1,cells)
        cells = self.moveColumn(2,1,cells)
        cells = self.moveColumn(1,1,cells)
        cells = self.moveColumn(2,1,cells)
        if start == self.board:
            return False
        return True

def randomPlaying():
    g = game([])
    g.start()
    while True:
        x = g.move(random.choice([1,2,3,4]), False)
        if type(x)==int:
            return x
            break
def downRightLeftUp():
    g = game([])
    g.start()
    while True:
        x = g.move(3, False)
        if type(x)==str:
            x = g.move(2, False)
            if type(x)==str:
                x = g.move(4, False)
                if type(x)==str:
                    x = g.move(1, False)
        if type(x) == int:
            return x
def downRightDownRight():
    g = game([])
    g.start()
    while True:
        x = g.move(3, False)
        if type(x)==str:
            x = g.move(2, False)
            if type(x)==str:
                x = g.move(4, False)
                if type(x)==str:
                    x = g.move(1, False)
        x = g.move(2, False)
        if type(x)==str:
            x = g.move(3, False)
            if type(x)==str:
                x = g.move(4, False)
                if type(x)==str:
                    x = g.move(1, False)
        if type(x) == int:
            return x
"""
results = []
for i in range(10000):
    results.append(downRightDownRight())
print np.mean(results)
"""   
        
    
