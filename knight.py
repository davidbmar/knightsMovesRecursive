#!/usr/bin/python
import sys

def translateFromNumberToRowCol(position):
  returnList=[]
  # 0 = 1,1
  # 1 = 1,2
  # 2 = 1,3 
  x = position/8+1
  y = position%8+1
  returnList.append(x)
  returnList.append(y) 
  return returnList

def possibleMoves(row,col):
   rowList=[]
   colList=[]
   # MOVE 0. UP 2 right 1
   rowList.append(row-2) 
   colList.append(col+1) 
   # MOVE 1: Up 1 right 2
   rowList.append(row-1) 
   colList.append(col+2) 
   # MOVE 2: Right 2 down 1.
   rowList.append(row+1) 
   colList.append(col+2) 
   # MOVE 3: Right 1 down 2.
   rowList.append(row+2) 
   colList.append(col+1) 
   # MOVE 4: Left 1 down 2.
   rowList.append(row+2) 
   colList.append(col-1) 
   # MOVE 5: Left 2 down 1.
   rowList.append(row+1) 
   colList.append(col-2) 
   # MOVE 6: Left 2 up 1.
   rowList.append(row-1) 
   colList.append(col-2) 
   # MOVE 7: Left 1 up 2.
   rowList.append(row-2) 
   colList.append(col-1) 

   positionList=[rowList,colList]
   return positionList

def validMoves(rowList,colList):
   validPositionList=[]
   validRowList=[]
   validColList=[]
   i=0
   for i in range(8):
      #print ("{} {}".format(rowList[i],colList[i]))
      if(rowList[i]>0 and rowList[i] <9 and colList[i]>0 and colList[i]<9):
         validRowList.append(rowList[i])
         validColList.append(colList[i])
   validPositionList=[validRowList,validColList]
   return validPositionList

def allValidMoves(row,col):
   myMoveList=[]
   mathPossibleRowList,mathPossibleColList=possibleMoves(row,col)
   validRowList,validColList=validMoves(mathPossibleRowList,mathPossibleColList)
   myMoveList=(validRowList,validColList)
   return myMoveList

def formatRowCol(aStartRow,aStartCol):
   row=[]
   col=[]
   allMoves=[]
   row,col=allValidMoves(aStartRow,aStartCol)
   
   counter=0
   for counter in range(len(row)):
      #print ("({},{})".format(row[counter],col[counter])) 
      allMoves.append((row[counter],col[counter])) 
   return allMoves

def recurseIt(depth,x,y,findx,findy,lowest,historyStack):
   #print ("depth:{} x:{},y:{} findx:{} findy:{} LOWEST:{} History:{}".format(depth,x,y,findx,findy,lowest,historyStack))

   if (depth==10):
      #print ("depth > search amount returning!")
      return lowest

   if (findx==x and findy==y):
      #print ("FOUND")
      # be careful, if you find a solution later after where you find the square you are searching for
      # and its a match you have to make sure that you dont replace the lowest # unless the new find is truely the lowest.
      if (depth<lowest):
         lowest=depth
      return lowest

   moves=[]
   moves=formatRowCol(x,y)
   #print moves


   counter=0
   for counter in range(len(moves)):
      x,y=moves[counter]
      historyStack.append((x,y))
      lowest=recurseIt(depth+1,x,y,findx,findy,lowest,historyStack)
      historyStack.pop(len(historyStack)-1)
   return lowest

# (starting depth, x position start, y position start, find x, find y)

def search(start,finish):

   (xStart,yStart)=translateFromNumberToRowCol(start)
   historyStack=[(xStart,yStart)]
   (xFinish,yFinish)=translateFromNumberToRowCol(finish)
   # (starting depth, x position start, y position start, find x, find y)
   count=recurseIt(0,xStart,yStart,xFinish,yFinish,99,historyStack)
   return count

output=search(0,1)
print output

#i=1
#for i in range(65): 
#   if i%8==0:
#      sys.stdout.write("\n")
#   (x,y)=translateFromNumberToRowCol(i)
#   sys.stdout.write(str(i)+":("+str(x)+","+str(y)+")")

   



   


