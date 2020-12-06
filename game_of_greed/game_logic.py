from abc import abstractmethod, ABC
from collections import Counter
import random


class GameLogic(ABC):

    def __init__(self,rules):
        self.rules=rules

    
    def calculate_score(self,tupleInt):          #input -> tuple(integers) 
        counter = Counter(tupleInt)
        result= counter.most_common()                             # output -> integer depend on the rules
        score=0

        if result [0][1] == 1:
            return self.rules[7]

        if len(tupleInt) == 6 and len(result)==3 and result[0][1] ==2:
            return self.rules[8]
            

        for i in result:
            score+=self.rules[i[0]][i[1]]
        return score

        #implement the rules



    def roll_dice(dice_result):         #input - >  integer (1-6)  //randint   for the dice number in the round          
        pass                            #output -> tuples of the values of theses dices


class Banker(ABC):

    def __init__(self):
        pass

    def shelf(amount):                  # input -> amount of point
        pass                                # shelf should temporarily store unbanked points.
    
    def bank():                             # The Total Points 
        pass                                 # add the amount of shelf to the bank and clear shelf
                                            # output -> the total of Point 
    
    def clear_shelf():                      #remove all unbanked points  //Falkel
        pass



if __name__ == "__main__":


    games_rules={
        1:{1:100,2:200,3:1000,4:2000,5:3000,6:4000},
        2:{1:0,2:0,3:200,4:400,5:600,6:800},
        3:{1:0,2:0,3:300,4:600,5:900,6:1200},
        4:{1:0,2:0,3:400,4:800,5:1200,6:1600},
        5:{1:50,2:100,3:500,4:1000,5:1500,6:2000},
        6:{1:0,2:0,3:600,4:1200,5:1800,6:2400},
        7:1500,             #stight
        8:750               #three pairs
    }
    greed = GameLogic(games_rules)
    tuple2 = (1, 2, 3, 4,5,5)
    print(greed.calculate_score(tuple2))
