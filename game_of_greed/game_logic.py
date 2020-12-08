from abc import abstractmethod, ABC
from collections import Counter
import random


class GameLogic(ABC):
    

    def __init__(self):
        pass

    @staticmethod
    def calculate_score(tupleInt):  
        rules={
            1:{1:100,2:200,3:1000,4:2000,5:3000,6:4000},
            2:{1:0,2:0,3:200,4:400,5:600,6:800},
            3:{1:0,2:0,3:300,4:600,5:900,6:1200},
            4:{1:0,2:0,3:400,4:800,5:1200,6:1600},
            5:{1:50,2:100,3:500,4:1000,5:1500,6:2000},
            6:{1:0,2:0,3:600,4:1200,5:1800,6:2400},
            7:1500,                                                   #stight
            8:1500                                                     #three pairs
    }                                                             #input -> tuple(integers) 
        counter = Counter(tupleInt)
        result= counter.most_common()                             # output -> integer depend on the rules
        score=0

        if len(tupleInt) == 0:
            return 0
        if counter.most_common(1)[0][1] == 1 and len(tupleInt) == 6:
            return rules[7]

        if len(tupleInt) == 6 and len(result)==3 and result[0][1] == 2:
            return rules[8]
            

        for i in result:
            score+=rules[i[0]][i[1]]
        return score

        #implement the rules

    
    @staticmethod
    def roll_dice(dice_result=6):
        '''#input - >  integer (1-6)  //randint for the dice number in the round 
        #output -> tuples of the values of theses dices
        '''
        rand = [random.randint(1,6) for i in range(dice_result)]
        return tuple(rand)                                     

class Banker(ABC):
   
    def __init__(self):
        self.balance=0
        self.shelved=0

    def shelf(self,amount):                  # input -> amount of point
        self.shelved+=amount                                # shelf should temporarily store unbanked points.
    
    def bank(self):                             # The Total Points 
        self.balance+=self.shelved 
        self.clear_shelf()                                        # add the amount of shelf to the bank and clear shelf
                                            # output -> the total of Point 
    
    def clear_shelf(self):                      #remove all unbanked points  //Falkel
        self.shelved=0



if __name__ == "__main__":


  
    greed = GameLogic()
    tuple2 = (5,)
    print(GameLogic.roll_dice())
    print(GameLogic.roll_dice(2))
    print(GameLogic.roll_dice(5))
    print(GameLogic.roll_dice(6))
    print(dir(Banker))