from random import randint
from random import choice
import numpy as np
import time

import random
import numpy as np
class game(object):
    def __init__(self):
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.score = 0
        self.statics = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.addTile()
        self.addTile()
    def show(self):
        for row in self.board:
            print row
    def move(self, direction, printing=True):
        self.statics = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        if direction ==1:  moved = self.moveDir([1,2,3,1,2,1], False)
        elif direction ==2: moved = self.moveDir([2,1,0,2,1,2], True)
        elif direction ==3: moved = self.moveDir([2,1,0,2,1,2], False)
        elif direction ==4: moved = self.moveDir([1,2,3,1,2,1], True)
        if moved!=0: self.addTile()
        elif np.count_nonzero(self.board) == 16:
            saved = [[x for x in item] for item in self.board]
            canmove = self.moveDir([1,2,3], False)+self.moveDir([2,1,0], True)+self.moveDir([2,1,0], False)+self.moveDir([1,2,3], True)
            if canmove == 0:
                if printing:
                    print "you lose, your score was "+ str(self.score)
                    self.show()
                return self.score,np.max(self.board)
            else:
                self.board = saved
        elif printing: print "can't move that way"
        if printing:
            self.show()
            print ""
    def addTile(self):
        options = [(i,j) for i in xrange(4) for j in xrange(4) if self.board[i][j]==0]
        place = choice(options)
        self.board[place[0]][place[1]]=choice([2,2,2,2,4])
    def moveLine(self, start, direction, column):
        moved=0
        if column: self.board = [[self.board[j][i] for j in xrange(4)]for i in xrange(4)]
        for i in xrange(4):
            if self.board[start][i] !=0 and not self.statics[start+direction][i]:
                if self.board[start+direction][i]==0:
                    self.board[start+direction][i]=self.board[start][i]
                    self.board[start][i] =0
                    moved+=1
                elif not self.statics[start][i] and self.board[start+direction][i] == self.board[start][i]:
                    self.board[start+direction][i]*=2
                    self.statics[start+direction][i] = True
                    self.score+=self.board[start+direction][i]
                    self.board[start][i] =0
                    moved+=1
                
        if column: self.board = [[self.board[j][i] for j in xrange(4)]for i in xrange(4)]
        return moved
    def moveDir(self, lis, column):
        moved=0
        for i in lis:
            moved+=self.moveLine(i,2*lis[0]-3, column)
        return moved

def randomPlaying(printing):
    g = game()
    x = None
    while x==None:
        x = g.move(random.choice([1,2,3,4]), printing)
    return x
def downRightLeftUp(printing):
    g = game()
    x = None
    while x==None:
        x = g.move(3, printing)
        if x==None:
            x = g.move(2, printing)
            if x==None:
                x = g.move(4, printing)
                if x==None:
                    x = g.move(1, printing)
        if x!=None:
            return x
def downRightDownRight(printing):
    g = game()
    while True:
        x = g.move(3, printing)
        if x==None:
            x = g.move(2, printing)
            if x==None:
                x = g.move(4, printing)
                if x==None:
                    x = g.move(1, printing)
        x = g.move(2, False)
        if x==None:
            x = g.move(3, False)
            if x==None:
                x = g.move(4, False)
                if x==None:
                    x = g.move(1, False)
        if x!=None:
            return x
def test(times):
    starttime = time.time()
    print "random"
    score = []
    maxes = []
    for i in xrange(times):
        a,b=randomPlaying(False)
        score.append(a)
        maxes.append(b)
    print "mean is score was "+str(np.mean(score))+" biggest tile was "+str(np.mean(maxes))
    print "max score "+str(np.max(score))+" biggest tile was "+str(np.max(maxes))

    print "swirl"
    score = []
    maxes = []
    for i in xrange(times):
        a,b=downRightLeftUp(False)
        score.append(a)
        maxes.append(b)
    print "mean is score was "+str(np.mean(score))+" biggest tile was "+str(np.mean(maxes))
    print "max score "+str(np.max(score))+" biggest tile was "+str(np.max(maxes))

    print "down right"
    score = []
    maxes = []
    for i in xrange(times):
        a,b=downRightDownRight(False)
        score.append(a)
        maxes.append(b)
    print "mean is score was "+str(np.mean(score))+" biggest tile was "+str(np.mean(maxes))
    print "max score "+str(np.max(score))+" biggest tile was "+str(np.max(maxes))

    print "total time to run "+str(times)+" times was "+str(time.time()-starttime)
test(10000)  
#import profile
#profile.run("test(500)")
