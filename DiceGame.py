import random

class Die:
    def __init__(self):
        self._faceValue=random.randint(1,6)
    def GetFacevalue(self):
        return self._faceValue
    
class DiceGame:
    def __init__(self):
        print("What is your name?")
        name=input(">")
        print("Hello,{0}!".format(name,))
        sum=0
        print("Rolling the dice...")
        for i in range(2):
            d=Die()
            v=d.GetFacevalue()
            sum+=v
            print("Die {0}: {1}".format(i+1,v))
        print("Total value: {0}".format(sum))
        if sum>=7:
#           print("You won!")
            print("{0} won!".format(name))
        else:
#           print("You lose")
            print("{0} lost".format(name))

if __name__=="__main__":
    DiceGame()
        
