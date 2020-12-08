from game_of_greed.game_logic import GameLogic,Banker
# from game_logic import GameLogic,Banker
#from game_of_greed import GameLogic

class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice

    def new_round(self,remaining_dice,round):
        print(f'Starting round {round}')
        print(f'Rolling {remaining_dice} dice...')
        roll = self.roller(remaining_dice)
        #roll=GameLogic.roll_dice(remaining_dice)
        print(','.join([str(i) for i in roll]))
        #check the zilch
        if round ==1:
            if Game.zilch(round,roll,0):
                return ' ',self.roller(6)
        return input('Enter dice to keep (no spaces), or (q)uit: '),roll
    @staticmethod
    def quit_game(score):
        print(f'Total score is {score} points')
        print(f'Thanks for playing. You earned {score} points')

    @staticmethod
    def convert_input_to_tuple(user_input):
            digits = [int(x) for x in str(user_input)]
            return tuple(digits)

    @staticmethod
    def cheatting(rolled,input):
        t1 = list(rolled)
        t2 = list(input)
        for n in t2:
            try:
                index = (t1.index(n))
                t1.pop(index)
            except ValueError:
                return True
        return False
    @staticmethod
    def zilch(round,roll,bank=0):
        if GameLogic.calculate_score(roll)==0:
            print('Zilch!!! Round over')
            print(f'You banked 0 points in round {round}')
            print(f'Total score is {bank} points')
            return True
        return False

    def play(self):
        nope_player = Banker()
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')


        elif res == 'y':                                   # we have to path [new round - current round]
            
            #initializing Variable
            round = 1
            remaining_dice = 6
            new_round= True

            #looping until reach break ('q')
            while True:

                # run this code if we are in a new round                                     
                if new_round ==True:
                    remaining_dice=6                        
                    dice_to_keep,rolled=self.new_round(remaining_dice,round)
                    round+=1
                    #check the zilch
                if Game.zilch(round,rolled,nope_player.balance):
                    round+=1
                else:

                    # handeling the Integers -> If Not Integers handel execep where the inpu is string ['q' - 'b']
                    try:            
                        user_aside=Game.convert_input_to_tuple(dice_to_keep)

                        #checking cheat
                        cheat = Game.cheatting(rolled,user_aside)
                        while cheat:
                            print('Cheater!!! Or possibly made a typo...')
                            print(','.join([str(i) for i in rolled]))
                            dice_to_keep= input('Enter dice to keep (no spaces), or (q)uit: ')
                            user_aside=Game.convert_input_to_tuple(dice_to_keep)
                            cheat = Game.cheatting(rolled,user_aside)

                        nope_player.shelf(GameLogic.calculate_score(user_aside))

                        # decrese The Remainig Dice
                        if GameLogic.calculate_score(user_aside) ==1500:
                            remaining_dice=6
                            print(f"You have {nope_player.shelved} unbanked points and 0 dice remaining")

                        else:
                            remaining_dice-=len(dice_to_keep)
                            print(f"You have {nope_player.shelved} unbanked points and {remaining_dice} dice remaining")
                        dice_to_keep= input('(r)oll again, (b)ank your points or (q)uit ')

                        # To Prevent handel the new_round msg when back to hande ['b' or 'q']
                        if dice_to_keep == 'b' or dice_to_keep =='q' or dice_to_keep =='r' :
                            new_round =False
                    except ValueError:
                        if dice_to_keep == 'b':
                            current_round=round-1
                            print(f'You banked {nope_player.shelved} points in round {current_round}')
                            nope_player.bank()
                            print(f'Total score is {nope_player.balance} points')
                            new_round=True
                            remaining_dice=6

                        if dice_to_keep == 'r':
                            print(f'Rolling {remaining_dice} dice...')
                            rolled = self.roller(remaining_dice)
                            if len(str(rolled)) ==1:
                                rolled= () + (rolled,) 
                            print(','.join([str(i) for i in rolled]))
                            # print(round,rolled,nope_player.balance,"top")
                            if Game.zilch(round-1,rolled,nope_player.balance):
                                new_round=True
                            else:
                                dice_to_keep =input('Enter dice to keep (no spaces), or (q)uit: ')


                        if dice_to_keep == 'q':
                            Game.quit_game(nope_player.balance)
                            break


if __name__ == '__main__':
    game = Game()
    game.play()