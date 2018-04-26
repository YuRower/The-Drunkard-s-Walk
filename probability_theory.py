#Shvidkoy Yura
#version 3.6 Python
import random
position=0
class Location(object):
    def __init__(self, state, left, stay, right):
        self.state = state
        self.left = left
        self.right= right
        self.stay = stay
    @property
    def Left(self):
        return self.left
    @property
    def Right(self):
        return self.right
    @property
    def NameState(self):
        return self.state
    @NameState.setter
    def NameState(self, value):
        self.state = value
    @property
    def Stay(self):
        return self.stay
    def __str__(self):
        return '<' + str(self.left) + ', ' + str(self.right) + '>'
    
class Executor(object):
     def __init__(self, i,j,k):
         self.i=i
         self.j=j
         self.k=k
     def takeStep(self,n):
            absorbing_state_P=Location("P",0,1,0)
            one=Location("1",  self.i  / ( self.i +  self.j +  self.k),  self.j/( self.i+ self.j+ self.k),  self.k / ( self.i +  self.j +  self.k))
            two=Location("2",  self.i / ( self.i +  self.k), 0,  self.k / ( self.i +  self.k))
            three=Location("3", self.j / ( self.i +  self.j), 0,  self.i / ( self.i +  self.j))
            absorbing_state_K=Location("K",0,1,0)
            self.field = [absorbing_state_P, one, two, three, absorbing_state_K]
            global position 
            position=n
            moves=0
            while ( (not (self.field[position].NameState==("P"))) and (not (self.field[position].NameState==("K")))):
                 self.walk()
                 moves+=1
            return moves
     def walk(self):
            global position 
            r =  random.uniform(0, 1)
            current=self.field[position]
            if(r < current.Left):
                position-=1
            elif(r < (current.Right+current.Left)):
                position+=1
                
class Field(object):
    def __init__(self):
        self.homers = {}
    def addHomer(self, homer,name):
        if homer in self.homers:
            raise ValueError('Duplicate drunk')
        else:
            self.homers[homer] = name
    def moveHomer(self, homer, n,name):
        result=0
        if not name in self.homers[homer]:
            raise ValueError('Drunk not in field')
        result+=homer.takeStep(n)
        return result
    
    
def startSim():
    homer = Executor(1,6,24)
    nameHomer="Drunk"
    distance=0
    numTrials=2000
    f=Field()
    f.addHomer(homer,nameHomer)
    for num in range(1,4):
            distance=0
            for j in range(numTrials):
                distance += f.moveHomer(homer,num,nameHomer) 
            print("Time of total number of state in non-absorbing state from position " + str(num) + " = " + str(distance /numTrials) )
        
startSim()         
